from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.DynamicMethods import DyMethod, DyBuiltinMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DyInt, DyBool, DySwitch


class DyBoolList(DyModule):

    def __init__(self, parent=None):
        self.parent = parent
        super(DyBoolList, self).__init__()

    def _setupBuiltinVariables(self):
        super(DyBoolList, self)._setupBuiltinVariables()
        self.__value__: bool
        self.__list__ = []
        self.__len__ = 0
        self.__len_true__ = DyInt(0)
        self.__len_true_change__ = DyInt()
        # self.__on_len_true_change__ = DySwitch()

    def setupTriggers(self):
        super(DyBoolList, self).setupTriggers()
        self.addTrigger(self.__len_true_change__).setAction(self._update_len_true, self.__len_true_change__)
        self.addTrigger(self.__len_true__).setAction(self._update_value)

    @DyMethod()
    def add(self, *dy_bools):
        self.__list__ += dy_bools
        self.__len__ = len(self.__list__)

        self.__len_true_change__.set(len(list(filter(lambda dy_bool: dy_bool, dy_bools))))

        for dy_bool in dy_bools:
            self.addTrigger(dy_bool).setAction(self._update_len_true, 1)
            # self.addTrigger(dy_bool, False, self._len_true_minus)
            # self.addTrigger(self, False, dy_bool)

    def set(self, value):
        Log.p("This object is a dependent variable. Therefore, it cannot be updated directly.", Log.color.RED)

    @DyMethod()
    def _update_len_true(self, change):
        self.__len_true__ += change

    @DyMethod()
    def _update_value(self):
        super(DyBoolList, self).set(self.__len_true__ == self.__len__)
        Log.p(self, Log.color.PURPLE)


class VariableManager(DyModule):

    def setupVariables(self):
        self.a = DyBool(False)
        self.b = DyBool(False)
        self.c = DyBool(False)
        self.list = DyBoolList()

    def setupTriggers(self):
        self.list.add(self.a, self.b, self.c)

        self.addTrigger(self.POST_INIT).setAction(self.updateBC, True, True, True)
        self.addTrigger(self.list).setAction(self.printWorks)

    @DyMethod()
    def printWorks(self):
        Log.p("DyBoolList Works!")

    @DyMethod()
    def updateBC(self, a, b, c):
        self.a.set(a)
        self.b.set(b)
        self.c.set(c)


vm = VariableManager()
