import abc

from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.FeatureManager import FeatureManager
from FTV.Managers.LogManager import LogManager
from FTV.Managers.UIManager import UIManager


class Module(object):
    em = ExecutionManager()
    lm = LogManager()

    def __init__(self):
        self.setupTriggers()

    def setupTriggers(self):
        pass

    def addTrigger(self):
        pass

class ModuleFeature(Module):
    from FTV.Managers.VariableManager import VariableManager

    vm = VariableManager()
    fm = FeatureManager()

    def __init__(self):
        self.settings = self.__class__._Settings()
        self.setupSettings()
        super().__init__()
        self.setupFeatures()

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
    uim = UIManager()

    def __init__(self):
        super().__init__()
        self.settings: __class__._Settings
        self.setupUITriggers()
        self.setupContainers()

    # def __createSettings(self):
    #     self.settings = Module._Settings()

    def setupUITriggers(self):
        pass

    def setupContainers(self):
        pass

    class _Settings(ModuleFeature._Settings):
        @classmethod
        def setUIPlatform(cls, ui_platform):
            cls.ui_platform = ui_platform
