import abc
# global variableManager
# global featureManager
import importlib

from FTV.Objects.Variables.AbstractDynamicModule import DynamicModuleParent
from FTV.Objects.Variables.DynamicMethods import DyBuiltinMethod
from FTV.Objects.Variables.DynamicObjects import DyBool, DySwitch


class Feature(DynamicModuleParent):
    type = "Feature"

    _builtin_managers = {
        "em": "ExecutionManager",
        "vm": "VariableManager",
        "fm": "FeatureManager",
    }

    def __init__(self):
        # Log.p(f"init{self.__class__.type}: " + str(self.__class__.__name__))
        self.__name__ = self.__class__.__name__

        self._managers = {}

        self.settings = self._Settings()
        self._fm_setupSettings()

        if self.settings.enabled:
            super(Feature, self).__init__()

    def _setupEnvironment(self):
        self._loadBuiltinSelf()

    @DyBuiltinMethod()
    def _loadBuiltinSelf(self):
        self._setupBuiltinManagers()
        self._setupBuiltinVariables()
        self._setupBuiltinMethods()
        self._setupBuiltinTriggers()

    @DyBuiltinMethod()
    def _loadSelf(self):
        self._setupResumeManagers()
        self._setupMethods()
        self.setupTriggers()
        self.vm.IS_SELF_LOADED.set(True)

    def _setupBuiltinMethods(self):
        self._BUILTIN_METHODS |= {"_loadChildren"}
        super(Feature, self)._setupBuiltinMethods()

    @abc.abstractmethod
    def setupSettings(self):
        pass

    def _setupBuiltinManagers(self):
        self.setupManagers()
        from FTV.FrameWork.Apps import NIApp

        for var_name in self.__class__._builtin_managers.keys():
            if var_name in self._managers.keys():
                continue

            cls_name = self.__class__._builtin_managers[var_name]
            is_parent_app = issubclass(self.__class__, NIApp)
            manager = self._getBaseAbstractManagerClass(cls_name)(_is_parent_app=is_parent_app)
            setattr(self.__class__, var_name, manager)

        for var_name, cls_name in self._managers.items():
            is_parent_app = issubclass(self.__class__, NIApp)
            manager = cls_name(_is_parent_app=is_parent_app)
            setattr(self.__class__, var_name, manager)

    @classmethod
    def _setupResumeManagers(cls):
        for key in cls._builtin_managers.keys():
            getattr(getattr(cls, key), "PRE_INIT").activate()

    def _setupBuiltinVariables(self):
        self.vm.POST_BUILTIN_LOAD = DySwitch(builtin=True)
        self.vm.PRE_LOAD = DySwitch(builtin=True)
        self.vm.IS_SELF_LOADED = DyBool(True, builtin=True)
        self.vm.POST_LOAD = DySwitch(builtin=True)
        # self.vm.START = DySwitch()
        # self.vm.EXIT = DySwitch()

        self.vm.PRE_LOAD_FEATURES = DySwitch(builtin=True)
        self.vm.IS_CHILDREN_LOADED = DyBool(False, builtin=True)
        self.vm.POST_LOAD_FEATURES = DySwitch(builtin=True)

    def _setupBuiltinTriggers(self):
        self.addTrigger(self._loadBuiltinSelf).setAction(self.vm.POST_BUILTIN_LOAD)
        self.addTrigger(self.vm.POST_BUILTIN_LOAD).setAction(self.vm.PRE_LOAD)
        self.addTrigger(self.vm.PRE_LOAD).setAction(self._loadSelf)
        self.addTrigger(self._loadSelf).setAction(self.vm.POST_LOAD)

        self.addTrigger(self.vm.POST_LOAD).setAction(self.vm.PRE_LOAD_FEATURES)
        self.addTrigger(self.vm.PRE_LOAD_FEATURES).setAction(self._loadChildren)
        self.addTrigger(self._loadChildren).setAction(self.vm.POST_LOAD_FEATURES)
        # self.addTrigger(self._loadChildren).setAction(self.fm.loading_progress, 1)
        # self.addTrigger(self.fm.loading_progress).setAction(self.vm.POST_LOAD_FEATURES)
        # self.addTrigger(self.vm.POST_LOAD_FEATURES).setAction(self.vm.START)

    def _fm_setupFeatures(self):
        self.fm.setupFeatures()
        self.setupFeatures()

    def _fm_setupSettings(self):
        # self.fm.setupSettings()
        self.setupSettings()

    @DyBuiltinMethod()
    def _loadChildren(self):
        self._fm_setupFeatures()
        self.vm.IS_CHILDREN_LOADED.set(True)

    # @classmethod
    @abc.abstractmethod
    def setupManagers(self):
        pass

    def _getBaseAbstractManagerClass(self, cls_name):
        # manager_class = __import__(f"FTV.Managers.{cls_name}")
        manager_class = importlib.import_module(f"FTV.Managers.{cls_name}")
        manager_class = getattr(manager_class, cls_name)
        return manager_class

    def _setAbstractManager(self, manager_name, Manager):
        self._managers[manager_name] = Manager
        # manager = Manager()
        # methods_list = [method for method in dir(manager) if callable(getattr(manager, method))
        #                 and not (method.startswith("__") and method.endswith("__"))]
        #
        # abstract_manager.__dict__.update(manager.__dict__)
        # for method in methods_list:
        #     setattr(abstract_manager, method, getattr(manager, method))

    # @classmethod
    def setVariableManager(self, Manager):
        self._setAbstractManager("vm", Manager)

    # @classmethod
    def setExecutionManager(self, Manager):
        self._setAbstractManager("em", Manager)

    # @classmethod
    def setFeatureManager(self, Manager):
        self._setAbstractManager("fm", Manager)

    def setupTriggers(self):
        pass

    """This method is deprecated. Please use the method "setupFeatures" in the FeatureManager instead."""
    def setupFeatures(self):
        pass

    """This method is deprecated. Please use the method "addFeatures" in the FeatureManager instead."""
    def addFeatures(self, *features):
        self.fm.addFeatures(*features)

    """This method is deprecated. Please use the method "addFeature" in the FeatureManager instead."""
    def addFeature(self, feature):
        self.fm.addFeatures(feature)

    class _Settings:
        ui_platform = None

        def __init__(self):
            self.enabled = True

        def setEnabled(self):
            self.enabled = True

        def setDisabled(self):
            self.enabled = False


# TODO lahav Add a proper mechanism for the loaded features tree.
class NIFeature(Feature):
    # type = "NIFeature"

    """This method is deprecated. Please use the method "setupSettings" in the FeatureManager instead."""
    # @abc.abstractmethod
    def setupSettings(self):
        pass

    """This method is deprecated. Please use the method "setupManagers" in the FeatureManager instead."""
    @classmethod
    # @abc.abstractmethod
    def setupManagers(cls):
        pass


class UIFeature(NIFeature):
    # type = "UIFeature"

    @classmethod
    def _setupBuiltinManagers(cls):
        super(UIFeature, cls)._setupBuiltinManagers()
        from FTV.Managers.UIManager import UIManager

        cls.uim: UIManager = UIManager()

    def _setupBuiltinVariables(self):
        super(UIFeature, self)._setupBuiltinVariables()
        self.vm.PRE_UI_LOAD = DySwitch()
        self.vm.IS_SELF_UI_LOADED = DyBool(False)
        self.vm.POST_UI_LOAD = DySwitch()

    def _setupBuiltinTriggers(self):
        super(NIFeature, self)._setupBuiltinTriggers()
        self.removeTrigger(self.vm.POST_LOAD, self.vm.PRE_LOAD_FEATURES)  # Must be redefined
        self.addTrigger(self.vm.POST_LOAD, True, self.vm.PRE_UI_LOAD)
        self.addTrigger(self.vm.PRE_UI_LOAD, True, self.vm.PRE_LOAD_FEATURES)

        self.addTrigger(self.vm.POST_LOAD, True, self.vm.PRE_UI_LOAD)
        self.addTrigger(self.vm.PRE_UI_LOAD, True, self._loadUISelf)
        self.addTrigger(self._loadUISelf, True, self.vm.POST_UI_LOAD)
        self.addTrigger(self.vm.POST_UI_LOAD, True, self.vm.PRE_LOAD_FEATURES)

    @DyBuiltinMethod()
    def _loadUISelf(self):
        self.uim.setupVariables()
        self.uim.setupVariables()
        self.uim.setupTriggers()
        self.setupUITriggers()
        self.uim.IS_SELF_UI_LOADED = DyBool(False)

    """This method is deprecated. Please use the method "setupManagers" in the FeatureManager instead."""
    @classmethod
    # @abc.abstractmethod
    def setupManagers(cls):
        pass

    """This method is deprecated. Please use the method "setupSettings" in the FeatureManager instead."""
    # @abc.abstractmethod
    def setupSettings(self):
        pass

    def setupUITriggers(self):
        pass

    def addUITrigger(self):
        pass
