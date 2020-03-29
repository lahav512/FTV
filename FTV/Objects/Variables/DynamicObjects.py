import math

from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import (DyObject, DyIntMagicMethods,
                                                         DyBoolMagicMethods)


class DyBool(DyBoolMagicMethods, DyObject):
    def __init__(self, value, builtin=False):
        super().__init__(value, builtin)
        self.__value__: bool

    def __condition__(self, *args, **kwargs):
        return self.__value__


class DySwitch(DyObject):
    def __init__(self, builtin=False):
        super().__init__(False, builtin)
        self.__value__: bool

    def set(self, value):
        if value:
            super(DySwitch, self).set(True)

        super(DySwitch, self)._set(False)

    def activate(self):
        self.set(True)

    def __action__(self, *args, **kwargs):
        self.activate()


class DyInt(DyIntMagicMethods, DyObject):
    def __init__(self, value: int=None, builtin=False):
        super().__init__(value, builtin)
        self.__value__: int = value


if __name__ == '__main__':
    a = DyInt(8)
    b = DyInt(5)
    # b -= a
    # a -= 1
    # a.set(15)
    # print(a)
    # a += b
    print(a > b)
    # print(b)

    # magic_methods = list(filter(lambda method: method.startswith("__") and method.endswith("__"), dir(int)))
    # dy_int_magic_methods = list(filter(lambda method: method not in dir(DyInt), magic_methods))
    #
    # print("\n".join(dy_int_magic_methods))
