from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Apps import NIApp
from FTV.FrameWork.Features import NIFeature
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DySwitch


class VM(VariableManager):
    def setupVariables(self):
        self.onStartWifiConnection = DySwitch()
        self.onWifiTurnedOn = DySwitch()
        self.onWifiConnected = DySwitch()
        self.onDataReceived = DySwitch()

    def setupTriggers(self):
        pass


class DyWifiExample(NIFeature):
    def setupSettings(self):
        pass

    @classmethod
    def setupManagers(cls):
        cls.setVariableManager(VM)

    @DyMethod()
    def turnWifiOn(self):
        self.vm.onWifiTurnedOn.activate()

    @DyMethod()
    def connectSSID(self):
        self.vm.onWifiConnected.activate()

    @DyMethod()
    def requestData(self):
        self.vm.onDataReceived.activate()

    @DyMethod()
    def displayData(self, message):
        Log.p(message)

    def setupTriggers(self):
        self.addTrigger(WifiApp.vm.START).setAction(self.vm.onStartWifiConnection)
        self.addTrigger(self.vm.onStartWifiConnection).setAction(self.turnWifiOn)
        self.addTrigger(self.vm.onWifiTurnedOn).setAction(self.connectSSID)
        self.addTrigger(self.vm.onWifiConnected).setAction(self.requestData)
        self.addTrigger(self.vm.onDataReceived).setAction(self.displayData, "New data !!!")


class WifiApp(NIApp):

    def setupFeatures(self):
        self.addFeature(DyWifiExample)

    def setupSettings(self):
        pass

    @classmethod
    def setupManagers(cls):
        pass


WifiApp()
