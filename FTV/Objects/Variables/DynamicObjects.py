# from FTV.Objects.Variables.AbstractDynamicObject import (DyObject, DyBoolMagicMethods, DyIntMagicMethods,
#                                                          DyFloatMagicMethods)
from Bots.GenerateMagicMethods.result.MagicMethodsInterfaces import (DyBoolMagicMethods, DyObject, DyFloatMagicMethods,
                                                                     DyIntMagicMethods, DyStrMagicMethods)
from FTV.Objects.Variables.AbstractConditions import (DyIntConditions, DyBoolConditions, DyFloatConditions,
                                                      DyStrConditions)


class DyBool(DyBoolMagicMethods, DyBoolConditions, DyObject):
    def __init__(self, value, builtin=False):
        super().__init__(value, builtin)
        self.__value__: bool

class DySwitch(DyBoolMagicMethods, DyObject):
    def __init__(self, builtin=False):
        super().__init__(False, builtin)
        self.__value__: bool

    def set(self, value):
        super(DySwitch, self)._set_empty(value)

    def activate(self):
        self.set(True)

    def __action__(self, *args, **kwargs):
        self.activate()

class DyInt(DyIntMagicMethods, DyIntConditions, DyObject):
    def __init__(self, value: int=None, builtin=False):
        super().__init__(value, builtin)
        self.__value__: int = value

    # def __condition__(self, old_val, new_val, *args, **kwargs):
    #     pass

class DyFloat(DyFloatMagicMethods, DyFloatConditions, DyObject):
    def __init__(self, value: float=None, builtin=False):
        super().__init__(value, builtin)
        self.__value__: float = value

class DyStr(DyStrMagicMethods, DyStrConditions, DyObject):
    def __init__(self, value: str=None, builtin=False):
        super().__init__(value, builtin)
        self.__value__: str = value


if __name__ == '__main__':
    a = DyInt(8)
    b = DyInt(8)
    a += b

    print(a)


    # magic_methods = list(filter(lambda method: method.startswith("__") and method.endswith("__"), dir(int)))
    # dy_int_magic_methods = list(filter(lambda method: method not in dir(DyInt), magic_methods))
    #
    # print("\n".join(dy_int_magic_methods))
