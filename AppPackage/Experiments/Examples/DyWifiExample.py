from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DynamicMethod
from FTV.Objects.Variables.DynamicModuleObject import DynamicModule
from FTV.Objects.Variables.DynamicObjects import DySwitch


class DyWifiExample(DynamicModule):
    @DynamicMethod()
    def turnWifiOn(self):
        self.onWifiTurnedOn.activate()

    @DynamicMethod()
    def connectSSID(self):
        self.onWifiConnected.activate()

    @DynamicMethod()
    def requestData(self):
        self.onDataReceived.activate()

    @DynamicMethod()
    def displayData(self):
        Log.p("Displaying the data :)")

    def setupVariables(self):
        self.onStartWifiConnection = DySwitch()
        self.onWifiTurnedOn = DySwitch()
        self.onWifiConnected = DySwitch()
        self.onDataReceived = DySwitch()

    def setupTriggers(self):
        self.addTrigger(self.POST_INIT, True, self.onStartWifiConnection)
        self.addTrigger(self.onStartWifiConnection, True, self.turnWifiOn)
        self.addTrigger(self.onWifiTurnedOn, True, self.connectSSID)
        self.addTrigger(self.onWifiConnected, True, self.requestData)
        self.addTrigger(self.onDataReceived, True, self.displayData)


DyWifiExample()
