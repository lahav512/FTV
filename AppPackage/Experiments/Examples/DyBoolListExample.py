from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DyListMagicMethods
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DyInt, DyBool


class DyBoolList(DyListMagicMethods, DyModule):

    def _setupBuiltinVariables(self):
        super(DyBoolList, self)._setupBuiltinVariables()
        self.__value__: bool
        self.__list__: list = []
        self.__len_true__ = DyInt(0)

    def setupTriggers(self):
        super(DyBoolList, self).setupTriggers()
        self.addTrigger(self.__len_true__).setAction(self._update_value)

    @DyMethod()
    def add(self, *dy_bools):
        self.__list__ += dy_bools
        self._update_len_true(len(list(filter(lambda dy_bool: dy_bool, dy_bools))))

        for dy_bool in dy_bools:
            self.addTrigger(dy_bool).setCondition(DyBool.IsChangedTo, True).setAction(self._update_len_true, 1)
            self.addTrigger(dy_bool).setCondition(DyBool.IsChangedTo, False).setAction(self._update_len_true, -1)

    def set(self, value):
        Log.p("This object is a dependent variable. Therefore, it cannot be updated directly.", Log.color.RED)

    def getList(self):
        return self.__list__

    @DyMethod()
    def _update_len_true(self, change):
        self.__len_true__ += change

    @DyMethod()
    def _update_value(self):
        super(DyBoolList, self).set(self.__len_true__ == len(self))
        # Log.p(self, Log.color.PURPLE)


class VariableManager(DyModule):

    def setupVariables(self):
        self.a = DyBool(False)
        self.b = DyBool(False)
        self.c = DyBool(False)
        self.list = DyBoolList()

    def setupTriggers(self):
        self.list.add(self.a, self.b, self.c)

        self.addTrigger(self.POST_INIT).setAction(self.updateABC, True, True, True)
        self.addTrigger(self.list).setAction(self.printWorks)

    @DyMethod()
    def printWorks(self):
        Log.p("DyBoolList Works!")
        Log.p(len(self.list))

    @DyMethod()
    def updateABC(self, a, b, c):
        self.a.set(a)
        self.b.set(b)
        self.c.set(c)


vm = VariableManager()
