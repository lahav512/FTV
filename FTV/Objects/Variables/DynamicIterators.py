from AppPackage.Experiments.Log import Log
from FTV.Objects.SystemObjects.TriggerObjects import Condition
from FTV.Objects.Variables.AbstractDynamicObject import DyListMagicMethods, DyBoolMagicMethods
from FTV.Objects.Variables.DynamicMethods import DyMethod, DyBuiltinMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DyInt, DyBool


class DyBoolList(DyListMagicMethods, DyBoolMagicMethods, DyModule):

    def _setupBuiltinMethods(self):
        self._BUILTIN_METHODS |= {"_update_len_true", "_update_value"}
        super(DyBoolList, self)._setupBuiltinMethods()

    def _setupBuiltinVariables(self):
        super(DyBoolList, self)._setupBuiltinVariables()
        self.__value__: bool
        # self.__len__: int = 0
        self.__iterator__ = []
        self.__len_true__ = DyInt(0, builtin=True)

    def _setupBuiltinTriggers(self):
        super(DyBoolList, self)._setupBuiltinTriggers()
        self.addTrigger(self.__len_true__)\
            .setCondition(DyBoolList.IsEqualToLenOf, self)\
            .setAction(self._update_value, True)

        self.addTrigger(self.__len_true__)\
            .setCondition(DyBoolList.IsNotEqualToLenOf, self)\
            .setAction(self._update_value, False)

    @DyMethod()
    def add(self, *dy_bools):
        self.__iterator__ += dy_bools
        # self.__len__ = len(self.__iterator__)
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


class DySwitchList(DyBoolList):
    def __init__(self):
        super(DySwitchList, self).__init__(False)

    def setupTriggers(self):

        self.addTrigger(self.__len_true__) \
            .setCondition(DySwitchList.IsEqualToLenOf, self) \
            .setAction(self.deactivateAll)

        self.addTrigger(self.__len_true__) \
            .setCondition(DySwitchList.IsEqualToLenOf, self) \
            .setAction(self._update_value, True)

    @DyMethod()
    def add(self, *dy_bools):
        # super(DySwitchList, self).add(*dy_bools)
        self.__iterator__ += dy_bools
        # self.__len__ = len(self.__iterator__)
        self._update_len_true(len(list(filter(lambda dy_bool: dy_bool, dy_bools))))

        for dy_bool in dy_bools:
            if isinstance(dy_bool, (DyBool, DyBoolList)):
                # dy_bool._is_child = True
                self.addTrigger(dy_bool).setCondition(DyBool.IsChangedTo, True).setAction(self._update_len_true, 1)
                self.addTrigger(dy_bool).setCondition(DyBool.IsChangedTo, False).setAction(self._update_len_true, -1)
            else:
                Log.p("This object is a DySwitchList iterator. Therefore, it cannot add child that is not DyBool or DyBoolList.", Log.color.RED)

    def activate(self):
        self.set(True)

    @DyBuiltinMethod()
    def deactivateAll(self):
        for item in self.__iterator__:
            item._set(False)
        # DyObject.set(self, False)
        self._set(False)
        self.__len_true__._set(0)

    @DyBuiltinMethod()
    def _update_value(self, value):
        super(DySwitchList, self)._set_empty(value)


if __name__ == '__main__':
    magic_methods = list(filter(lambda method: method.startswith("__") and method.endswith("__"), dir(list)))
    dy_int_magic_methods = list(filter(lambda method: method not in dir(DyBoolList), magic_methods))

    print("\n".join(dy_int_magic_methods))
