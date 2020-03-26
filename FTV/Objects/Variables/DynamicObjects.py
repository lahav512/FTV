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
            self.switch = DySwitch()

        def setupTriggers(self):
            self.addTrigger(self.POST_INIT, True, self.switch)
            # self.addTrigger(self.switch, True, self.print)

        def add(self, dy_bool):
            self.__list__.append(dy_bool)
            self.__len__ = len(self.__list__)

        @DynamicMethod()
        def print(self):
            print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")

    class VariableManager(DynamicModule):
        def setupVariables(self):
            self.AAA = DySwitch()

            self.a = DyBool(False)
            self.b = DyBool(False)
            self.c = DyBool(False)
            self.list = DyBoolList(self)

        def setupTriggers(self):
            self.list.add(self.a)
            self.list.add(self.b)
            self.list.add(self.c)

            self.addTrigger(self.POST_INIT, True, self.printList)
            self.addTrigger(self.printList, True, self.AAA)

        @DynamicMethod()
        def printList(self):
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

            # Log.i(len(self.list))

    vm = VariableManager()
