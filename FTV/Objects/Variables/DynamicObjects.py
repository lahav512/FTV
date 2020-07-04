from AppPackage.Experiments.Log import Log
from Bots.GenerateMagicMethods.result.MagicMethodsInterfaces import (DyBoolMagicMethods, DyObject, DyFloatMagicMethods,
                                                                     DyIntMagicMethods, DyStrMagicMethods,
                                                                     DyListMagicMethods, DyByteArrayMagicMethods,
                                                                     DyBytesMagicMethods, DyComplexMagicMethods,
                                                                     DyDictMagicMethods, DySetMagicMethods,
                                                                     DyTupleMagicMethods)
from FTV.Objects.Variables.AbstractConditions import (DyIntConditions, DyBoolConditions, DyFloatConditions,
                                                      DyStrConditions, DyByteArrayConditions, DyBytesConditions,
                                                      DyComplexConditions, DyDictConditions, DyListConditions,
                                                      DySetConditions, DyTupleConditions)


class DyInt(DyIntMagicMethods, DyIntConditions, DyObject):
    def __init__(self, value: int=None, builtin=False):
        super().__init__(value.__int__(), builtin)
        self.__value__ = value.__int__()

    def set(self, value):
        super(DyInt, self).set(value.__int__())

    # def __condition__(self, old_val, new_val, *args, **kwargs):
    #     pass


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


class DyByteArray(DyByteArrayMagicMethods, DyByteArrayConditions, DyObject):
    def __init__(self, value: bytearray=None, builtin=False):
        super().__init__(bytearray(value), builtin)
        self.__value__ = bytearray(value)

    def set(self, value):
        super(DyByteArray, self).set(bytearray(value))


class DyBytes(DyBytesMagicMethods, DyBytesConditions, DyObject):
    def __init__(self, value: bytes=None, builtin=False):
        super().__init__(bytes(value), builtin)
        self.__value__ = bytes(value)

    def set(self, value):
        super(DyBytes, self).set(bytearray(value))


class DyComplex(DyComplexMagicMethods, DyComplexConditions, DyObject):
    def __init__(self, value: complex=None, builtin=False):
        super().__init__(complex(value), builtin)
        self.__value__ = complex(value)

    def set(self, value):
        super(DyComplex, self).set(complex(value))


class DyDict(DyDictMagicMethods, DyDictConditions, DyObject):
    def __init__(self, value: dict=None, builtin=False):
        super().__init__(dict(value), builtin)
        self.__value__ = dict(value)

    def set(self, value):
        super(DyDict, self).set(dict(value))


class DyFloat(DyFloatMagicMethods, DyFloatConditions, DyObject):
    def __init__(self, value: float=None, builtin=False):
        super().__init__(value.__float__(), builtin)
        self.__value__ = value.__float__()

    def set(self, value):
        super(DyFloat, self).set(value.__float__())


class DyList(DyListMagicMethods, DyListConditions, DyObject):
    def __init__(self, value=None, builtin=False):
        if value is None:
            value = []
        super().__init__(list(value), builtin)
        self.__value__ = list(value)

    def set(self, value):
        super(DyList, self).set(list(value))

    def append(self, item):
        self.__value__.append(item)


class DySet(DySetMagicMethods, DySetConditions, DyObject):
    def __init__(self, value: set=None, builtin=False):
        super().__init__(set(value), builtin)
        self.__value__ = set(value)

    def set(self, value):
        super(DySet, self).set(set(value))


class DyStr(DyStrMagicMethods, DyStrConditions, DyObject):
    def __init__(self, value: str=None, builtin=False):
        super().__init__(value.__str__(), builtin)
        self.__value__ = value.__str__()

    def set(self, value):
        super(DyStr, self).set(value.__str__())


class DyTuple(DyTupleMagicMethods, DyTupleConditions, DyObject):
    def __init__(self, value: tuple=None, builtin=False):
        super().__init__(tuple(value), builtin)
        self.__value__ = tuple(value)

    def set(self, value):
        super(DyTuple, self).set(tuple(value))


if __name__ == '__main__':
    from FTV.Objects.Variables.DynamicMethods import DyMethod
    from FTV.Objects.Variables.DynamicModules import DyModule

    class VM(DyModule):
        def setupVariables(self):
            self.a = DyFloat(5)
            self.b = DyFloat(5)
            # self.com = DyComplex(10)

            self.c = DyStr("lahav {}")
            self.d = DyStr("svorai")

            self.e = DyList([1, 2, 3])
            self.f = DyList([4, 5, 6])

            self.g = DyBool(True)
            self.h = DyBool(False)

        def setupTriggers(self):
            self.addTrigger(self.POST_LOAD).setAction(self.action)

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

            # Log.p("{}...".format(self.d))
            #
            # Log.p(self.c)
            # Log.p(type(self.c))
            # Log.p(self.d)
            # Log.p(type(self.d))

            # self.e += self.f
            #
            # Log.p(self.c in [4])
            #
            # Log.p(self.e)
            # Log.p(type(self.e))
            # Log.p(self.f)
            # Log.p(type(self.f))

            self.g += self.h
            Log.p(self.g and self.h)

            Log.p(self.g)
            Log.p(type(self.g))
            Log.p(self.h)
            Log.p(type(self.h))

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
