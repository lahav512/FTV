from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.DynamicMethod import DynamicMethod
from FTV.Objects.Variables.DynamicModule import DynamicModule
from FTV.Objects.Variables.DynamicObjects import DyInt, DyBool, DySwitch


class DyBoolList(DynamicModule):

    def __init__(self, parent):
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

    def _setupBuiltinTriggers(self):
        super(DyBoolList, self)._setupBuiltinTriggers()
        self.addTrigger(self.__len_true_change__, True, self._update_len_true)
        self.addTrigger(self.__len_true__, True, self._update_value)

    @DynamicMethod()
    def add(self, *dy_bools):
        self.__list__ += dy_bools
        self.__len__ = len(self.__list__)

        self.__len_true_change__.set(len(list(filter(lambda dy_bool: dy_bool, dy_bools))))

        for dy_bool in dy_bools:
            self.addTrigger(dy_bool, True, self._len_true_plus_one)
            # self.addTrigger(dy_bool, False, self._len_true_minus)
            # self.addTrigger(self, False, dy_bool)

    def set(self, value):
        Log.p("This object is a dependent variable. Therefore, it cannot be updated directly.", Log.color.RED)

    @DynamicMethod()
    def _len_true_plus_one(self):
        self._update_len_(1)

    @DynamicMethod()
    def _update_len_true(self):
        self._update_len_(self.__len_true_change__)

    def _update_len_(self, change):
        self.__len_true__ += change

    # @DynamicMethod()
    # def _len_true_minus(self):
    #     self.__len_true__.set(self.__len_true__.get() - 1)

    @DynamicMethod()
    def _update_value(self):
        super(DyBoolList, self).set(self.__len_true__ == self.__len__)
        Log.p(self, Log.color.PURPLE)


class VariableManager(DynamicModule):

    def setupVariables(self):
        self.a = DyBool(True)
        self.b = DyBool(False)
        self.c = DyBool(False)
        self.list = DyBoolList(self)

    def setupTriggers(self):
        self.list.add(self.a, self.b, self.c)

        self.addTrigger(self.POST_INIT, True, self.updateBC)
        self.addTrigger(self.list, True, self.printWorks)

    @DynamicMethod()
    def printWorks(self):
        Log.p("DyBoolList Works!")
        # self.list.set(False)

    @DynamicMethod()
    def updateBC(self):
        # self.a.set(True)
        self.b.set(True)
        self.c.set(True)
        # list = self.list.__list__
        # for item in list:
        #     print(item.get())

        # Log.i(len(self.list))


vm = VariableManager()

# class DyModule(DynamicModule):
#     def setupVariables(self):
#         self.a = DyBool(True)
#         self.b = DyBool(True)
#
#         self.c = {self.a, self.b}
#         self.a.set(False)
#         self.c.add(self.a)
#         Log.p(len(self.c))
#
#
# DyModule()
