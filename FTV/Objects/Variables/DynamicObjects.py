# from FTV.Objects.Variables.AbstractDynamicObject import (DyObject, DyBoolMagicMethods, DyIntMagicMethods,
#                                                          DyFloatMagicMethods)
from AppPackage.Experiments.Log import Log
from Bots.GenerateMagicMethods.result.MagicMethodsInterfaces import (DyBoolMagicMethods, DyObject, DyFloatMagicMethods,
                                                                     DyIntMagicMethods, DyStrMagicMethods)
from FTV.Objects.Variables.AbstractConditions import (DyIntConditions, DyBoolConditions, DyFloatConditions,
                                                      DyStrConditions)


class DyBool(DyBoolMagicMethods, DyBoolConditions, DyObject):
    def __init__(self, value, builtin=False):
        super().__init__(bool(value), builtin)
        self.__value__ = bool(value)

    def set(self, value):
        super(DyBool, self).set(bool(value))

class DySwitch(DyBoolMagicMethods, DyObject):
    def __init__(self, builtin=False):
        super().__init__(False, builtin)
        self.__value__ = False

    def set(self, value):
        super(DySwitch, self)._set_empty(value)

    def activate(self):
        self.set(True)

    def __action__(self, *args, **kwargs):
        self.activate()

class DyInt(DyIntMagicMethods, DyIntConditions, DyObject):
    def __init__(self, value: int=None, builtin=False):
        super().__init__(int(value), builtin)
        self.__value__ = int(value)

    def set(self, value):
        super(DyInt, self).set(int(value))

    # def __condition__(self, old_val, new_val, *args, **kwargs):
    #     pass

class DyFloat(DyFloatMagicMethods, DyFloatConditions, DyObject):
    def __init__(self, value: float=None, builtin=False):
        super().__init__(float(value), builtin)
        self.__value__ = float(value)

    def set(self, value):
        super(DyFloat, self).set(float(value))


class DyStr(DyStrMagicMethods, DyStrConditions, DyObject):
    def __init__(self, value: str=None, builtin=False):
        super().__init__(str(value), builtin)
        self.__value__ = str(value)

    def set(self, value):
        super(DyStr, self).set(str(value))

class DyComplex(DyStrMagicMethods, DyStrConditions, DyObject):
    def __init__(self, value: complex=None, builtin=False):
        super().__init__(complex(value), builtin)
        self.__value__ = complex(value)

    def set(self, value):
        super(DyComplex, self).set(complex(value))

if __name__ == '__main__':
    from FTV.Objects.Variables.DynamicMethods import DyMethod
    from FTV.Objects.Variables.DynamicModules import DyModule

    class VM(DyModule):
        def setupVariables(self):
            self.a = DyInt(8)
            self.b = DyInt(10)
            # self.com = DyComplex(10)

            self.c = DyStr("lahav")
            self.d = DyStr("svorai")

        def setupTriggers(self):
            self.addTrigger(self.POST_INIT).setAction(self.action)

        @DyMethod()
        def action(self):
            self.a += self.b
            self.c += self.d
            # b += a

            # self.c *= self.a
            self.c.set(self.d)

            Log.p("a = {}".format(self.a))
            Log.p("c = {}".format(self.c))
            # Log.p("com = {}".format(self.com))
            Log.p(type(self.a))
            Log.p(type(self.c))

    VM()

    # magic_methods = list(filter(lambda method: method.startswith("__") and method.endswith("__"), dir(int)))
    # dy_int_magic_methods = list(filter(lambda method: method not in dir(DyInt), magic_methods))
    #
    # print("\n".join(dy_int_magic_methods))
