from FTV.FrameWork.Apps import NIApp
from FTV.Managers.ExecutionManager import ExecutionManager
from FTV.Managers.FeatureManager import FeatureManager
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.SystemObjects.Executions import DyThread
from FTV.Objects.Variables.DynamicObjects import DyInt


class VM(VariableManager):
    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass


class EM(ExecutionManager):
    def setupThreads(self):
        self.MainUI = DyThread()


class FM(FeatureManager):
    def setupFeatures(self):

        self.addFeature(IntegratedClock)
        self.addFeature(VisualClock)


class ClockApp(NIApp):

    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setExecutionManager(EM)
        self.setFeatureManager(FM)
        self.setVariableManager(VM)
