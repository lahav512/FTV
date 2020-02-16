import abc

from AppPackage.Experiments.Log import Log
from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.LogManager import LogManager
from FTV.Managers.UIManager import UIManager


# global variableManager
# global featureManager


class DynamicModule(object):
    type = "Module"
    is_potential_parent = False

    em = ExecutionManager()
    lm = LogManager()

    def __init__(self):
        # if "ModuleFeature" not in map(lambda bases: bases.__name__,self.__class__.__bases__):
        #     Log.i("initModule: " + str(self.__class__.__name__))
        self.setupVariables()
        self.setupTriggers()

    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass

    def addTrigger(self, *args):
        pass

class ModuleFeature(DynamicModule):
    from FTV.Managers.VariableManager import VariableManager
    from FTV.Managers.FeatureManager import FeatureManager

    type = "ModuleFeature"
    is_potential_parent = True

    vm: VariableManager = None
    fm: FeatureManager = None

    def __init__(self):
        Log.i("initFeature: " + str(self.__class__.__name__))

        if self.__class__.vm is None:
            self.__class__.vm = self.__class__.VariableManager()
        if self.__class__.fm is None:
            self.__class__.fm = self.__class__.FeatureManager()

        self.settings = self.__class__._Settings()
        self.setupSettings()
        self.__setupTriggers()
        super().__init__()
        self.setupFeatures()

    def __setupTriggers(self):
        self.addTrigger(self.vm.PRE_LOAD_FEATURES, True, self.addFeatures)
        self.addTrigger(self.addFeatures, "finish", self.vm.POST_LOAD_FEATURES)

    def setupFeatures(self):
        pass

    def addFeatures(self, *features):
        self.fm.addFeatures(*features)

    def setupSettings(self):
        pass

    class _Settings:
        ui_platform = None

        def __init__(self):
            self.enabled = True

        def setEnabled(self):
            self.enabled = True

        def setDisabled(self):
            self.enabled = False

class UIFeature(ModuleFeature):
    type = "UIFeature"

    uim = UIManager()

    def __init__(self):
        super().__init__()
        self.settings: __class__._Settings
        self.setupUITriggers()
        self.startUIServices()
        self.vm.POST_SETUP = True

    def setupUITriggers(self):
        pass

    def setupContainers(self):
        pass

    def startUIServices(self):
        pass

    class _Settings(ModuleFeature._Settings):
        @classmethod
        def setUIPlatform(cls, ui_platform):
            cls.ui_platform = ui_platform
