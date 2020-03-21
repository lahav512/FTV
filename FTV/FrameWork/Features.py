import abc

# global variableManager
# global featureManager
from FTV.Objects.Variables.DynamicVariable import DyBool, DySwitch


class DynamicModule(object):
    type = "NIFeature"

    def __init__(self):
        self.settings = self._Settings()
        self.setupSettings()

        if self.settings.enabled:
            self._setupEnvironment()

    def _setupEnvironment(self):
        self._loadBuiltinSelf()
        self.vm.POST_BUILTIN_LOAD = True

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

        cls.vm: VariableManager = VariableManager()

    def _setupBuiltinVariables(self):
        self.vm.POST_BUILTIN_LOAD = DySwitch()
        self.vm.PRE_LOAD = DySwitch()
        self.vm.IS_SELF_LOADED = DyBool(False)
        self.vm.POST_LOAD = DySwitch()
        self.vm.START = DySwitch()
        self.vm.EXIT = DySwitch()

    def _setupBuiltinTriggers(self):
        self.addTrigger()

    @classmethod
    def setupManagers(cls):
        pass

    def setupTriggers(self):
        pass

    def addTrigger(self, *args):
        pass

    class _Settings:
        ui_platform = None

        def __init__(self):
            self.enabled = True

        def setEnabled(self):
            self.enabled = True

        def setDisabled(self):
            self.enabled = False
    
class NIFeature(DynamicModule):
    def __init__(self):
        super(NIFeature, self).__init__()
        self.setupSettings()

    @classmethod
    def _setupBuiltinManagers(cls):
        super(NIFeature, cls)._setupBuiltinManagers()
        from FTV.Managers.FeatureManager import FeatureManager

        cls.fm: FeatureManager = None

    def _setupBuiltinVariables(self):
        super(NIFeature, self)._setupBuiltinVariables()
        self.vm.PRE_LOAD_FEATURES = DySwitch()
        self.vm.IS_CHILDREN_LOADED = DyBool(False)
        self.vm.POST_LOAD_FEATURES = DySwitch()

    def _loadChildren(self):
        self.setupFeatures()
        self.vm.IS_CHILDREN_LOADED = DyBool(False)

    @classmethod
    @abc.abstractmethod
    def setupManagers(cls):
        pass

    @abc.abstractmethod
    def setupSettings(self):
        pass

    @abc.abstractmethod
    def setupFeatures(self):
        pass

    def addFeatures(self, *features):
        for feature in features:
            self.addFeature(feature)

    def addFeature(self, feature):
        self.fm.add(feature)

class UIFeature(NIFeature):

    type = "UIFeature"

    @classmethod
    def _setupBuiltinManagers(cls):
        super(UIFeature, cls)._setupBuiltinManagers()
        from FTV.Managers.UIManager import UIManager

        cls.uim: UIManager = None

    def _setupBuiltinVariables(self):
        super(UIFeature, self)._setupBuiltinVariables()
        self.vm.PRE_UI_LOAD = DySwitch()
        self.vm.IS_SELF_UI_LOADED = DyBool(False)
        self.vm.POST_UI_LOAD = DySwitch()

    def _loadUISelf(self):
        self.uim.setupUIVariables()
        self.uim.setupUITriggers()
        self.setupUITriggers()
        self.vm.IS_SELF_UI_LOADED = DyBool(False)

    @classmethod
    @abc.abstractmethod
    def setupManagers(cls):
        pass

    @abc.abstractmethod
    def setupSettings(self):
        pass

    @abc.abstractmethod
    def setupFeatures(self):
        pass

    def setupUITriggers(self):
        pass

    def addUITrigger(self):
        pass
