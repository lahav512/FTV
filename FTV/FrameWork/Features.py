import abc

# global variableManager
# global featureManager
from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicModule import DynamicModuleParent
from FTV.Objects.Variables.DynamicMethods import DyBuiltinMethod
from FTV.Objects.Variables.DynamicObjects import DyBool, DySwitch


class Feature(DynamicModuleParent):
    type = "Feature"

    def __init__(self):
        Log.p(f"init{self.__class__.type}: " + str(self.__class__.__name__))

        self.settings = self._Settings()
        self.setupSettings()

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
        self.setupManagers()
        self.vm.setupVariables()
        self.vm._setupMethods()
        self.vm.setupTriggers()

        self._setupMethods()
        self.setupTriggers()

        self.vm.IS_SELF_LOADED = True

    def _setupBuiltinMethods(self):
        self._BUILTIN_METHODS |= {"_loadChildren"}
        super(Feature, self)._setupBuiltinMethods()

    @abc.abstractmethod
    def setupSettings(self):
        pass

    @classmethod
    def _setupBuiltinManagers(cls):
        from FTV.Managers.VariableManager import VariableManager
        from FTV.Managers.FeatureManager import FeatureManager

        cls.vm: VariableManager = VariableManager()
        cls.fm: FeatureManager = FeatureManager()

        # cls.vm.setBuiltin(True)
        # cls.fm.setBuiltin(True)

    def _setupBuiltinVariables(self):
        self.vm.POST_BUILTIN_LOAD = DySwitch(builtin=True)
        self.vm.PRE_LOAD = DySwitch(builtin=True)
        self.vm.IS_SELF_LOADED = DyBool(False)
        self.vm.POST_LOAD = DySwitch(builtin=True)
        # self.vm.START = DySwitch()
        # self.vm.EXIT = DySwitch()

        self.vm.PRE_LOAD_FEATURES = DySwitch()
        self.vm.IS_CHILDREN_LOADED = DyBool(False, builtin=True)
        self.vm.POST_LOAD_FEATURES = DySwitch()

    def _setupBuiltinTriggers(self):
        self.addTrigger(self._loadBuiltinSelf).setAction(self.vm.POST_BUILTIN_LOAD)  # .setThread("thread.main")
        self.addTrigger(self.vm.POST_BUILTIN_LOAD).setAction(self.vm.PRE_LOAD)
        self.addTrigger(self.vm.PRE_LOAD).setAction(self._loadSelf)
        self.addTrigger(self._loadSelf).setAction(self.vm.POST_LOAD)

        self.addTrigger(self.vm.POST_LOAD).setAction(self.vm.PRE_LOAD_FEATURES)
        self.addTrigger(self.vm.PRE_LOAD_FEATURES).setAction(self._loadChildren)
        self.addTrigger(self._loadChildren).setAction(self.vm.POST_LOAD_FEATURES)
        # self.addTrigger(self.vm.POST_LOAD_FEATURES).setAction(self.vm.START)

    @DyBuiltinMethod()
    def _loadChildren(self):
        self.setupFeatures()
        self.vm.IS_CHILDREN_LOADED.set(True)

    @classmethod
    @abc.abstractmethod
    def setupManagers(cls):
        pass

    @staticmethod
    def _setAbstractManager(abstract_manager, Manager):
        manager = Manager()
        methods_list = [method for method in dir(manager) if callable(getattr(manager, method))
                        and not (method.startswith("__") and method.endswith("__"))]

        abstract_manager.__dict__.update(manager.__dict__)
        for method in methods_list:
            setattr(abstract_manager, method, getattr(manager, method))

    @classmethod
    def setVariableManager(cls, Manager):
        cls._setAbstractManager(cls.vm, Manager)

    @classmethod
    def setFeatureManager(cls, Manager):
        cls._setAbstractManager(cls.fm, Manager)

    def setupTriggers(self):
        pass

    def setupFeatures(self):
        pass

    def addFeatures(self, *features):
        self.fm.add(*features)

    def addFeature(self, feature):
        self.fm.add(feature)

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

    @abc.abstractmethod
    def setupSettings(self):
        pass

    @classmethod
    @abc.abstractmethod
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
        self.uim.setupTriggers()
        self.setupUITriggers()
        self.uim.IS_SELF_UI_LOADED = DyBool(False)

    @classmethod
    @abc.abstractmethod
    def setupManagers(cls):
        pass

    @abc.abstractmethod
    def setupSettings(self):
        pass

    def setupUITriggers(self):
        pass

    def addUITrigger(self):
        pass
