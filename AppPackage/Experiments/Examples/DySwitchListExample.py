from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.DynamicIterators import DySwitchList
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DySwitch


class VariableManager(DyModule):

    def setupVariables(self):
        self.a_master = DySwitch()
        self.master = DySwitchList()

        self.a = DySwitch()
        self.b = DySwitch()
        self.c = DySwitch()
        self.list = DySwitchList()

    def setupTriggers(self):
        self.master.add(self.a_master)
        self.list.add(self.a, self.b, self.c, self.master)

        self.addTrigger(self.POST_INIT).setAction(self.updateABC)
        self.addTrigger(self.list).setAction(self.printWorks)

    @DyMethod()
    def printWorks(self):
        Log.p("DyBoolList Works!")
        for item in self.list:
            Log.p(item.__name__)
        Log.p(len(self.list))
        # self.list.set(False)
        Log.p(self.list)

    @DyMethod()
    def updateABC(self):
        self.a.activate()
        self.b.activate()
        self.c.activate()
        self.a_master.set(True)


vm = VariableManager()
