# from FTV.Objects.Variables.AbstractDynamicObject import (DyObject, DyBoolMagicMethods, DyIntMagicMethods,
#                                                          DyFloatMagicMethods)
from AppPackage.Experiments.Log import Log
from Bots.GenerateMagicMethods.result.MagicMethodsInterfaces import (DyBoolMagicMethods, DyObject, DyFloatMagicMethods,
                                                                     DyIntMagicMethods, DyStrMagicMethods,
                                                                     DyListMagicMethods)
from FTV.Objects.Variables.AbstractConditions import (DyIntConditions, DyBoolConditions, DyFloatConditions,
                                                      DyStrConditions)


class DyBool(DyBoolMagicMethods, DyBoolConditions, DyObject):
    def __init__(self, value, builtin=False):
        super().__init__(value.__bool__(), builtin)
        self.__value__ = value.__bool__()

    def set(self, value):
        super(DyBool, self).set(value.__bool__())

class DySwitch(DyBoolMagicMethods, DyObject):
    def __init__(self, builtin=False):
        super().__init__(False, builtin)
        self.__value__ = False

    def set(self, value):
        super(DySwitch, self)._set_empty(value.__bool__())

    def activate(self):
        self.set(True)

    def __action__(self, *args, **kwargs):
        self.activate()

class DyInt(DyIntMagicMethods, DyIntConditions, DyObject):
    def __init__(self, value: int=None, builtin=False):
        super().__init__(value.__int__(), builtin)
        self.__value__ = value.__int__()

    def set(self, value):
        super(DyInt, self).set(value.__int__())

    # def __condition__(self, old_val, new_val, *args, **kwargs):
    #     pass

class DyFloat(DyFloatMagicMethods, DyFloatConditions, DyObject):
    def __init__(self, value: float=None, builtin=False):
        super().__init__(value.__float__(), builtin)
        self.__value__ = value.__float__()

    def set(self, value):
        super(DyFloat, self).set(value.__float__())


class DyStr(DyStrMagicMethods, DyStrConditions, DyObject):
    def __init__(self, value: str=None, builtin=False):
        super().__init__(value.__str__(), builtin)
        self.__value__ = value.__str__()

    def set(self, value):
        super(DyStr, self).set(value.__str__())

class DyComplex(DyStrMagicMethods, DyStrConditions, DyObject):
    def __init__(self, value: complex=None, builtin=False):
        super().__init__(complex(value), builtin)
        self.__value__ = complex(value)

    def set(self, value):
        super(DyComplex, self).set(complex(value))

class DyList(DyListMagicMethods, DyStrConditions, DyObject):
    def __init__(self, value: list=None, builtin=False):
        super().__init__(value + [], builtin)
        self.__value__ = value + []

    def set(self, value):
        super(DyList, self).set(value + [])


if __name__ == '__main__':
    from FTV.Objects.Variables.DynamicMethods import DyMethod
    from FTV.Objects.Variables.DynamicModules import DyModule

    class VM(DyModule):
        def setupVariables(self):
            self.a = DyFloat(5)
            self.b = DyFloat(5)
            # self.com = DyComplex(10)

            self.c = DyStr("lahav")
            self.d = DyStr("svorai")

            self.e = DyList([1, 2, 3])
            self.f = DyList([4, 5, 6])

        def setupTriggers(self):
            self.addTrigger(self.POST_INIT).setAction(self.action)

        @DyMethod()
        def action(self):
            # self.a += self.b
            # self.d += self.c

            # self.b % self.a

            # b += a

            # self.c *= self.a
            # self.c.set(self.d)

            # Log.p("a = {}".format(self.a))
            # Log.p("c = {}".format(self.c))
            # # Log.p("com = {}".format(self.com))
            # Log.p(type(self.a))
            # Log.p(type(self.c))
            # # ab = 5 if
            # Log.p(self.b and self.a)
            #
            # a = 5
            # a **= 7

            # self.a /= 3
            # import math
            # Log.p(math.trunc(self.a))
            #
            # Log.p(self.a)
            # Log.p(type(self.a))
            # Log.p(self.b)
            # Log.p(type(self.b))

            # self.c += self.d
            #
            # Log.p(self.d.get() in "lahavs")
            #
            # Log.p(self.c)
            # Log.p(type(self.c))
            # Log.p(self.d)
            # Log.p(type(self.d))

            self.e += self.f

            Log.p(self.c in [4])

            Log.p(self.e)
            Log.p(type(self.e))
            Log.p(self.f)
            Log.p(type(self.f))

    VM()

    # class A:
    #     R = 100
    #     C = 0
    #
    #     def __init__(self):
    #         self.a = 5
    #         # self.a = DyInt(5)
    #         self.loop()
    #
    #     def loop(self):
    #         if self.C < self.R:
    #             self.C += 1
    #             # if isinstance(a, DyInt):
    #             self.a
    #             return self.loop()
    #             # if isinstance(a, int):
    #             #     return self.loop(a)
    #
    # Efficiency.check(A, 10000, "A")

    # magic_methods = list(filter(lambda method: method.startswith("__") and method.endswith("__"), dir(int)))
    # dy_int_magic_methods = list(filter(lambda method: method not in dir(DyInt), magic_methods))
    #
    # print("\n".join(dy_int_magic_methods))
