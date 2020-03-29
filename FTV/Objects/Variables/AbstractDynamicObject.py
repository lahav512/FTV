import inspect
import time
from abc import abstractmethod, ABC
from functools import wraps, partial
from queue import Queue

import wrapt as wrapt

from AppPackage.Experiments.Log import Log
from FTV.Objects.SystemObjects.Trigger import Trigger
from AppPackage.Experiments import Efficiency


class DynamicObjectInterface(object):
    # __slots__ = ("__triggers__", "__active_triggers__")

    def __init__(self):
        self.__triggers__ = []
        self.__active_triggers__ = Queue()

    @staticmethod
    def _distributeTriggers(dy_object):
        for trigger in dy_object.__triggers__:
            if trigger.thread is None:
                dy_object.__active_triggers__.put_nowait(trigger)
            else:
                # TODO lahav Add trigger to its designated thread
                pass

    @staticmethod
    def _runActiveTriggers(dy_object):
        while not dy_object.__active_triggers__.empty():
            trigger = dy_object.__active_triggers__.get_nowait()
            if trigger.runCondition():
                trigger.runAction()

    def _prepareAndRunTriggers(self, dy_object):
        self._distributeTriggers(dy_object)
        self._runActiveTriggers(dy_object)

    def __condition__(self, *args, **kwargs):
        return True

    @abstractmethod
    def __action__(self, *args, **kwargs) -> object:
        pass


class DyObjectMagicMethods(object):

    # # # Operator Magic Methods

    def __lt__(self, other):
        return object.__lt__(self.get(), DyObject.__get_other__(other))

    def __le__(self, other):
        return object.__le__(self.get(), DyObject.__get_other__(other))

    def __eq__(self, other):
        return object.__eq__(self.get(), DyObject.__get_other__(other))

    def __ne__(self, other):
        return object.__ne__(self.get(), DyObject.__get_other__(other))

    def __gt__(self, other):
        return object.__gt__(self.get(), DyObject.__get_other__(other))

    def __ge__(self, other):
        return object.__ge__(self.get(), DyObject.__get_other__(other))

    # # # String Magic Methods

    def __str__(self):
        return object.__str__(self.get())

    def __format__(self, formatstr):
        return object.__format__(self.get(), formatstr)

    def __hash__(self):
        return object.__hash__(self.get())


class DyBoolMagicMethods(DyObjectMagicMethods):

    # # # Operator Magic Methods

    def __lt__(self, other):
        return bool.__lt__(self.get(), other + 0)

    def __le__(self, other):
        return bool.__le__(self.get(), other + 0)

    def __eq__(self, other):
        return bool.__eq__(self.get(), other + 0)

    def __ne__(self, other):
        return bool.__ne__(self.get(), other + 0)

    def __gt__(self, other):
        return bool.__gt__(self.get(), other + 0)

    def __ge__(self, other):
        return bool.__ge__(self.get(), other + 0)

    # # # Operator Magic Methods

    def __add__(self, other):
        return bool.__add__(self.get(), other + 0)

    def __sub__(self, other):
        return bool.__sub__(self.get(), other + 0)

    def __mul__(self, other):
        return bool.__mul__(self.get(), other + 0)

    def __floordiv__(self, other):
        return bool.__floordiv__(self.get(), other + 0)

    def __truediv__(self, other):
        return bool.__truediv__(self.get(), other + 0)

    def __mod__(self, other):
        return bool.__mod__(self.get(), other + 0)

    def __divmod__(self, other):
        return bool.__divmod__(self.get(), other + 0)

    def __pow__(self, other):
        return bool.__pow__(self.get(), other + 0)

    def __lshift__(self, other):
        return bool.__lshift__(self.get(), other + 0)

    def __rshift__(self, other):
        return bool.__rshift__(self.get(), other + 0)

    def __and__(self, other):
        return bool.__and__(self.get(), other + 0)

    def __or__(self, other):
        return bool.__or__(self.get(), other + 0)

    def __xor__(self, other):
        return bool.__xor__(self.get(), other + 0)

    def __bool__(self):
        return bool.__bool__(self.get())

    # def __div__(self, other):
    #     return int.__div__(self.__value__, other)

    # # # Type Conversion Magic Methods

    def __bool__(self):
        return bool.__bool__(self.get())

    def __float__(self):
        return bool.__float__(self.get())

    def __index__(self):
        return bool.__index__(self.get())

    # def __complex__(self):
    #     return int.__complex__(self.__value__)

    # def __oct__(self):
    #     return int.__oct__(self.__value__)

    # def __hex__(self):
    #     return int.__hex__(self.__value__)

    # # # Augmented Assignment

    def __iadd__(self, other):
        self.set(self.__add__(other))
        return self

    def __radd__(self, other):
        return bool.__radd__(self.get(), other)

    def __isub__(self, other):
        self.set(self.__sub__(other))
        return self

    def __rsub__(self, other):
        return bool.__rsub__(self.get(), other)

    def __imul__(self, other):
        self.set(self.__mul__(other))
        return self

    def __rmul__(self, other):
        return bool.__rmul__(self.get(), other)

    def __ifloordiv__(self, other):
        self.set(self.__floordiv__(other))
        return self

    def __rfloordiv__(self, other):
        return bool.__rfloordiv__(self.get(), other)

    def __itruediv__(self, other):
        self.set(self.__truediv__(other))
        return self

    def __rtruediv__(self, other):
        return bool.__rtruediv__(self.get(), other)

    def __imod__(self, other):
        self.set(self.__mod__(other))
        return self

    def __rmod__(self, other):
        return bool.__rmod__(self.get(), other)

    def __ipow__(self, other):
        self.set(self.__pow__(other))
        return self

    def __rpow__(self, other):
        return bool.__rpow__(self.get(), other)

    def __ilshift__(self, other):
        self.set(self.__lshift__(other))
        return self

    def __rlshift__(self, other):
        return bool.__rlshift__(self.get(), other)

    def __irshift__(self, other):
        self.set(self.__rshift__(other))
        return self

    def __rrshift__(self, other):
        return bool.__rrshift__(self.get(), other)

    def __iand__(self, other):
        self.set(self.__and__(other))
        return self

    def __rand__(self, other):
        return bool.__rand__(self.get(), other)

    def __ior__(self, other):
        self.set(self.__or__(other))
        return self

    def __ror__(self, other):
        return bool.__ror__(self.get(), other)

    def __ixor__(self, other):
        self.set(self.__xor__(other))
        return self

    def __rxor__(self, other):
        return bool.__rxor__(self.get(), other)

    # def __idiv__(self, other):
    #     return int.__rdiv__(self.__value__, other)

    # # # Unary operators and functions

    def __pos__(self):
        return bool.__pos__(self.get())

    def __neg__(self):
        return bool.__neg__(self.get())

    def __abs__(self):
        return bool.__abs__(self.get())

    def __invert__(self):
        return bool.__invert__(self.get())

    def __round__(self):
        return bool.__round__(self.get())

    def __trunc__(self):
        return self.get() # True for int only!!!

    # def __floor__(self):
    #     return int.__floor__(self.__value__)

    # def __ceil__(self):
    #     return int.__ceil__(self.__value__)


class DyIntMagicMethods(DyObjectMagicMethods):

    # # # Operator Magic Methods

    def __lt__(self, other):
        return int.__lt__(self.get(), other + 0)

    def __le__(self, other):
        return int.__le__(self.get(), other + 0)

    def __eq__(self, other):
        return int.__eq__(self.get(), other + 0)

    def __ne__(self, other):
        return int.__ne__(self.get(), other + 0)

    def __gt__(self, other):
        return int.__gt__(self.get(), other + 0)

    def __ge__(self, other):
        return int.__ge__(self.get(), other + 0)

    # # # Operator Magic Methods

    def __add__(self, other):
        return int.__add__(self.get(), other + 0)

    def __sub__(self, other):
        return int.__sub__(self.get(), other + 0)

    def __mul__(self, other):
        return int.__mul__(self.get(), other + 0)

    def __floordiv__(self, other):
        return int.__floordiv__(self.get(), other + 0)

    def __truediv__(self, other):
        return int.__truediv__(self.get(), other + 0)

    def __mod__(self, other):
        return int.__mod__(self.get(), other + 0)

    def __divmod__(self, other):
        return int.__divmod__(self.get(), other + 0)

    def __pow__(self, other):
        return int.__pow__(self.get(), other + 0)

    def __lshift__(self, other):
        return int.__lshift__(self.get(), other + 0)

    def __rshift__(self, other):
        return int.__rshift__(self.get(), other + 0)

    def __and__(self, other):
        return int.__and__(self.get(), other + 0)

    def __or__(self, other):
        return int.__or__(self.get(), other + 0)

    def __xor__(self, other):
        return int.__xor__(self.get(), other + 0)

    def __bool__(self):
        return int.__bool__(self.get())

    # def __div__(self, other):
    #     return int.__div__(self.__value__, other)

    # # # Type Conversion Magic Methods

    def __int__(self):
        return int.__int__(self.get())

    def __float__(self):
        return int.__float__(self.get())

    def __index__(self):
        return int.__index__(self.get())

    # def __complex__(self):
    #     return int.__complex__(self.__value__)

    # def __oct__(self):
    #     return int.__oct__(self.__value__)

    # def __hex__(self):
    #     return int.__hex__(self.__value__)

    # # # Augmented Assignment

    def __iadd__(self, other):
        self.set(self.__add__(other))
        return self

    def __radd__(self, other):
        return int.__radd__(self.get(), other)

    def __isub__(self, other):
        self.set(self.__sub__(other))
        return self

    def __rsub__(self, other):
        return int.__rsub__(self.get(), other)

    def __imul__(self, other):
        self.set(self.__mul__(other))
        return self

    def __rmul__(self, other):
        return int.__rmul__(self.get(), other)

    def __ifloordiv__(self, other):
        self.set(self.__floordiv__(other))
        return self

    def __rfloordiv__(self, other):
        return int.__rfloordiv__(self.get(), other)

    def __itruediv__(self, other):
        self.set(self.__truediv__(other))
        return self

    def __rtruediv__(self, other):
        return int.__rtruediv__(self.get(), other)

    def __imod__(self, other):
        self.set(self.__mod__(other))
        return self

    def __rmod__(self, other):
        return int.__rmod__(self.get(), other)

    def __ipow__(self, other):
        self.set(self.__pow__(other))
        return self

    def __rpow__(self, other):
        return int.__rpow__(self.get(), other)

    def __ilshift__(self, other):
        self.set(self.__lshift__(other))
        return self

    def __rlshift__(self, other):
        return int.__rlshift__(self.get(), other)

    def __irshift__(self, other):
        self.set(self.__rshift__(other))
        return self

    def __rrshift__(self, other):
        return int.__rrshift__(self.get(), other)

    def __iand__(self, other):
        self.set(self.__and__(other))
        return self

    def __rand__(self, other):
        return int.__rand__(self.get(), other)

    def __ior__(self, other):
        self.set(self.__or__(other))
        return self

    def __ror__(self, other):
        return int.__ror__(self.get(), other)

    def __ixor__(self, other):
        self.set(self.__xor__(other))
        return self

    def __rxor__(self, other):
        return int.__rxor__(self.get(), other)

    # def __idiv__(self, other):
    #     return int.__rdiv__(self.__value__, other)

    # # # Unary operators and functions

    def __pos__(self):
        return int.__pos__(self.get())

    def __neg__(self):
        return int.__neg__(self.get())

    def __abs__(self):
        return int.__abs__(self.get())

    def __invert__(self):
        return int.__invert__(self.get())

    def __round__(self):
        return int.__round__(self.get())

    def __trunc__(self):
        return self.get() # True for int only!!!

    # def __floor__(self):
    #     return int.__floor__(self.__value__)

    # def __ceil__(self):
    #     return int.__ceil__(self.__value__)


class DyObject(DyObjectMagicMethods, DynamicObjectInterface):

    type = "DynamicObject"

    def __init__(self, value=None, builtin=False):
        super(DyObject, self).__init__()
        self.__value__: object = value
        self.__name__: str = "__name__"
        self._is_builtin: bool = builtin

    def _set(self, value):
        self.__value__ = value

    def set(self, value):
        self._set(value)
        # if self.__name__ == "POST_INIT":
        self.__log_p__(self.__name__)
        self._prepareAndRunTriggers(self)

    def _get(self):
        return self.__value__

    def get(self):
        return self._get()

    def setBuiltin(self, ans):
        self._is_builtin = ans

    # def __repr__(self):
    #     return self.get()

    @staticmethod
    def __get_other__(other):
        if isinstance(other, DyObject):
            return other.get()
        return other

    def __log_p__(self, message):
        if not (self._is_builtin and not Log.BUILTIN_ENABLED):
            Log.p(message, Log.color.BLUE)

    def __action__(self, *args, **kwargs):
        return self.set(args[0])
