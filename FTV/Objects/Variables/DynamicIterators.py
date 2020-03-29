from AppPackage.Experiments.Log import Log
from FTV.Objects.SystemObjects.TriggerObjects import Condition
from FTV.Objects.Variables.AbstractDynamicObject import DySetMagicMethods, DyBoolMagicMethods
from FTV.Objects.Variables.DynamicMethods import DyMethod, DyBuiltinMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DyInt, DyBool


class DyBoolList(DySetMagicMethods, DyBoolMagicMethods, DyModule):

    def _setupBuiltinVariables(self):
        super(DyBoolList, self)._setupBuiltinVariables()
        self.__value__: bool
        self.__len__: int = 0
        self.__iterator__ = []
        self.__len_true__ = DyInt(0, builtin=True)

    def setupTriggers(self):
        super(DyBoolList, self).setupTriggers()

        self.addTrigger(self.__len_true__)\
            .setCondition(DyBoolList.IsEqualToLenOf, self)\
            .setAction(self._update_value, True)

        self.addTrigger(self.__len_true__)\
            .setCondition(DyBoolList.IsNotEqualToLenOf, self)\
            .setAction(self._update_value, False)

    @DyMethod()
    def add(self, *dy_bools):
        self.__iterator__ += dy_bools
        self.__len__ = len(self.__iterator__)
        self._update_len_true(len(list(filter(lambda dy_bool: dy_bool, dy_bools))))

        for dy_bool in dy_bools:
            self.addTrigger(dy_bool).setCondition(DyBool.IsChangedTo, True).setAction(self._update_len_true, 1)
            self.addTrigger(dy_bool).setCondition(DyBool.IsChangedTo, False).setAction(self._update_len_true, -1)

    def set(self, value):
        Log.p("This object is a dependent variable. Therefore, it cannot be updated directly.", Log.color.RED)

    def getList(self):
        return self.__iterator__

    @DyBuiltinMethod()
    def _update_len_true(self, change):
        self.__len_true__ += change

    @DyBuiltinMethod()
    def _update_value(self, value):
        super(DyBoolList, self).set(value)

    def __condition__(self, old_val, new_val, *args, **kwargs):
        return new_val

    def __action__(self, *args, **kwargs):
        self.set(args[0])

    class IsEqualToLenOf(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val == len(args[0])

    class IsNotEqualToLenOf(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val != len(args[0])
