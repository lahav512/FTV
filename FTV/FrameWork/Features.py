import abc

from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.FeatureManager import FeatureManager
from FTV.Managers.LogManager import LogManager
from FTV.Managers.UIManager import UIManager
from FTV.Managers.VariableManager import VariableManager


class ModuleFeature(object):
    fm = FeatureManager()
    em = ExecutionManager()
    vm = VariableManager()
    lm = LogManager()

    def __init__(self):
        self.setupFeatures()
        # self.setupManagers()
        self.__setups()

    # def setupManagers(self):
    #     pass

    def __setups(self):
        self.settings = self.__class__._Settings()
        self.setupSettings()
        self.setupTriggers()
        self.setupParents()

    def setupTriggers(self):
        pass

    def addTrigger(self):
        pass

    def setupFeatures(self):
        pass

    def addFeatures(self, *features):
        self.fm.addFeatures(*features)

    def setupParents(self):
        pass

    def addParent(self, parent):
        pass

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
