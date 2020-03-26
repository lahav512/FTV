from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DynamicObject, DynamicMethod


class DyBool(DynamicObject):
    def __init__(self, value):
        super().__init__(value)
        self.__value__: bool


class DySwitch(DynamicObject):
    def __init__(self):
        super().__init__(False)
        self.__value__: bool

    def set(self, value):
        if value:
            super(DySwitch, self).set(True)

        super(DySwitch, self)._set(False)

    def activate(self):
        self.set(True)


class DyInt(DynamicObject):
    def __init__(self, value):
        super().__init__(value)
        self.__value__: int


if __name__ == '__main__':
    from FTV.Objects.Variables.DynamicModuleObject import DynamicModule

    class DyBoolList(DynamicModule):
        def __init__(self, parent):
            self.parent = parent
            super(DyBoolList, self).__init__()

        def _setupBuiltinVariables(self):
            super(DyBoolList, self)._setupBuiltinVariables()
            self.__value__: bool
            self.__list__ = []
        
        def setupVariables(self):
            self._len_true = DyInt(0)

        def setupTriggers(self):
            self.addTrigger(self._len_true, True, self._update_value)

        def add(self, dy_bool):
            self.__list__.append(dy_bool)
            self.__len__ = len(self.__list__)

            if dy_bool.get():
                self._len_true_plus()
            # else:
            #     self._len_true_minus()

            self.addTrigger(dy_bool, True, self._len_true_plus)
            # self.addTrigger(dy_bool, False, self._len_true_minus)

        @DynamicMethod()
        def _len_true_plus(self):
            self._len_true.set(self._len_true.get() + 1)

        @DynamicMethod()
        def _len_true_minus(self):
            self._len_true.set(self._len_true.get() - 1)

        @DynamicMethod()
        def _update_value(self):
            self.set(self._len_true.get() == self.__len__)
            Log.p(self.get())

        # @DynamicMethod()
        # def print(self):
        #     print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")

    class VariableManager(DynamicModule):
        def setupVariables(self):
            self.a = DyBool(True)
            self.b = DyBool(False)
            self.c = DyBool(False)
            self.list = DyBoolList(self)

        def setupTriggers(self):
            self.list.add(self.a)
            self.list.add(self.b)
            self.list.add(self.c)

            self.addTrigger(self.POST_INIT, True, self.printList)
            self.addTrigger(self.list, True, self.printVictory)

        @DynamicMethod()
        def printVictory(self):
            Log.p("Victory!", Log.color.PURPLE)

        @DynamicMethod()
        def printList(self):
            # self.a.set(True)
            self.b.set(True)
            self.c.set(True)
            list = self.list.__list__
            for item in list:
                print(item.get())

            # Log.i(len(self.list))

    vm = VariableManager()
