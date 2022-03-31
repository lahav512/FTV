from Experiments.Examples.BIUAutomation.Features.DataCollection import DataCollection
from Experiments.Examples.BIUAutomation.Features.DataSharing import DataSharing
from FTV.FrameWork.Apps import NIApp
from FTV.Managers.ExecutionManager import ExecutionManager
from FTV.Managers.FeatureManager import FeatureManager
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.SystemObjects.Executions import DyThread
from FTV.Objects.Variables.DynamicObjects import DyInt, DySwitch, DyList


class VM(VariableManager):
    def setupVariables(self):
        self.onStartCollection = DySwitch()
        self.onCollectedEventsUpdated = DySwitch()
        self.onCalendarEventsUpdated = DySwitch()
        self.collectedEvents = DyList()
        self.calendarEvents = DyList()

    def setupTriggers(self):
        pass


class EM(ExecutionManager):
    def setupThreads(self):
        self.MainUI = DyThread()


class FM(FeatureManager):
    def setupFeatures(self):
        self.addFeature(DataCollection)
        self.addFeature(DataSharing)


class BIUApp(NIApp):
    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setExecutionManager(EM)
        self.setFeatureManager(FM)
        self.setVariableManager(VM)

    def setupTriggers(self):
        self.addTrigger(self.vm.START).setAction(self.vm.onStartCollection)
