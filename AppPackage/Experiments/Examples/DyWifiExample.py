from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DySwitch


class DyWifiExample(DyModule):
    @DyMethod()
    def turnWifiOn(self):
        self.onWifiTurnedOn.activate()

    @DyMethod()
    def connectSSID(self):
        self.onWifiConnected.activate()

    @DyMethod()
    def requestData(self):
        self.onDataReceived.activate()

    @DyMethod()
    def displayData(self, message):
        Log.p(message)

    def setupVariables(self):
        self.onStartWifiConnection = DySwitch()
        self.onWifiTurnedOn = DySwitch()
        self.onWifiConnected = DySwitch()
        self.onDataReceived = DySwitch()

    def setupTriggers(self):
        self.addTrigger(self.POST_LOAD).setAction(self.onStartWifiConnection)
        self.addTrigger(self.onStartWifiConnection).setAction(self.turnWifiOn)
        self.addTrigger(self.onWifiTurnedOn).setAction(self.connectSSID)
        self.addTrigger(self.onWifiConnected).setAction(self.requestData)
        self.addTrigger(self.onDataReceived).setAction(self.displayData, "New data !!!")


DyWifiExample()
