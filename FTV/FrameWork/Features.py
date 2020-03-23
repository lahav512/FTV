import abc

# global variableManager
# global featureManager
from FTV.Objects.Variables.AbstractDynamicObject import DynamicModuleParent
from FTV.Objects.Variables.DynamicObject import DyBool, DySwitch


class Feature(DynamicModuleParent):
    type = "Feature"

    def __init__(self):
        self.settings = self._Settings()
        self.setupSettings()

        if self.settings.enabled:
            super(Feature, self).__init__()

    def _setupEnvironment(self):
        self._loadBuiltinSelf()

    def _loadBuiltinSelf(self):
        self._setupBuiltinManagers()
        self._setupBuiltinVariables()
        self._setupBuiltinTriggers()

    def _loadSelf(self):
        self.setupManagers()
        self.vm.setupVariables()
        self.vm.setupTriggers()
        self.setupTriggers()
        self.vm.IS_SELF_LOADED = True

    @abc.abstractmethod
    def setupSettings(self):
        pass

    @classmethod
    def _setupBuiltinManagers(cls):
        from FTV.Managers.VariableManager import VariableManager
        from FTV.Managers.FeatureManager import FeatureManager

        cls.vm: VariableManager = VariableManager()
        cls.fm: FeatureManager = FeatureManager()

    def _setupBuiltinVariables(self):
        self.fm.POST_BUILTIN_INIT = DySwitch()
        self.fm.PRE_INIT = DySwitch()
        self.fm.IS_SELF_LOADED = DyBool(False)
        self.fm.POST_INIT = DySwitch()
        self.fm.START = DySwitch()
        self.fm.EXIT = DySwitch()

        self.fm.PRE_LOAD_FEATURES = DySwitch()
        self.fm.IS_CHILDREN_LOADED = DyBool(False)
        self.fm.POST_LOAD_FEATURES = DySwitch()

    def _setupBuiltinTriggers(self):
        self.addTrigger(self._loadBuiltinSelf, True, self.fm.POST_BUILTIN_INIT, "thread.main")
        self.addTrigger(self.fm.POST_BUILTIN_INIT, True, self.fm.PRE_INIT)
        self.addTrigger(self.fm.PRE_INIT, True, self._loadSelf)
        self.addTrigger(self._loadSelf, True, self.fm.POST_INIT)

        self.addTrigger(self.fm.POST_INIT, True, self.fm.PRE_LOAD_FEATURES)  # Must be overridden in the UIFeature

        self.addTrigger(self.fm.PRE_LOAD_FEATURES, True, self._loadChildren)
        self.addTrigger(self._loadChildren, True, self.fm.POST_LOAD_FEATURES)
        self.addTrigger(self.fm.POST_LOAD_FEATURES, True, self.fm.START)

    def _loadChildren(self):
        self.setupFeatures()
        self.fm.IS_CHILDREN_LOADED = DyBool(False)

    @classmethod
    @abc.abstractmethod
    def setupManagers(cls):
        pass

    def setupTriggers(self):
        pass

    def setupFeatures(self):
        pass

    def addFeatures(self, *features):
        for feature in features:
            self.addFeature(feature)

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
    type = "NIFeature"

    @abc.abstractmethod
    def setupSettings(self):
        pass

    @classmethod
    @abc.abstractmethod
    def setupManagers(cls):
        pass


class UIFeature(NIFeature):
    type = "UIFeature"

    @classmethod
    def _setupBuiltinManagers(cls):
        super(UIFeature, cls)._setupBuiltinManagers()
        from FTV.Managers.UIManager import UIManager

        cls.uim: UIManager = UIManager()

    def _setupBuiltinVariables(self):
        super(UIFeature, self)._setupBuiltinVariables()
        self.uim.PRE_UI_LOAD = DySwitch()
        self.uim.IS_SELF_UI_LOADED = DyBool(False)
        self.uim.POST_UI_LOAD = DySwitch()

    def _setupBuiltinTriggers(self):
        super(NIFeature, self)._setupBuiltinTriggers()
        self.removeTrigger(self.fm.POST_INIT, self.fm.PRE_LOAD_FEATURES)  # Must be redefined
        self.addTrigger(self.fm.POST_INIT, self.uim.PRE_UI_LOAD)
        self.addTrigger(self.uim.PRE_UI_LOAD, self.fm.PRE_LOAD_FEATURES)

        self.addTrigger(self.fm.POST_INIT, True, self.uim.PRE_UI_LOAD)
        self.addTrigger(self.uim.PRE_UI_LOAD, True, self._loadUISelf)
        self.addTrigger(self._loadUISelf, True, self.uim.POST_UI_LOAD)
        self.addTrigger(self.uim.POST_UI_LOAD, True, self.fm.PRE_LOAD_FEATURES)

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
