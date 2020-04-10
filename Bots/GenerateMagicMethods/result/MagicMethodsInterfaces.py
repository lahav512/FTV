from AppPackage.Experiments.Log import Log
from AppPackage.Experiments.PickleTests.DataObject import TempQueue
from FTV.Objects.Variables.AbstractConditions import DyObjectConditions


class DynamicObjectInterface(object):
    # __slots__ = ("__triggers__", "__active_triggers__")

    def __init__(self):
        self.__triggers__ = []
        self.__active_triggers__ = TempQueue()

    @staticmethod
    def _distributeTriggers(dy_object):
        for trigger in dy_object.__triggers__:
            if trigger.thread is None:
                dy_object.__active_triggers__.put_nowait(trigger)
            else:
                # TODO lahav Add trigger to its designated thread
                pass

    @staticmethod
    def _runActiveTriggers(dy_object, old_val=None, new_val=None):
        while not dy_object.__active_triggers__.empty():
            trigger = dy_object.__active_triggers__.get_nowait()
            if trigger.runCondition(old_val, new_val):
                trigger.runAction()

    def _prepareAndRunTriggers(self, dy_object, old_val=None, new_val=None):
        self._distributeTriggers(dy_object)
        self._runActiveTriggers(dy_object, old_val, new_val)

    # @abstractmethod
    def __action__(self, *args, **kwargs) -> object:
        pass


class DyObjectMagicMethods:

    def __delattr__(self, *args, **kwargs) -> None:  # real signature unknown
        return object.__delattr__(self.get(), *args, **kwargs)

    def __dir__(self, *args, **kwargs):  # real signature unknown
        return object.__dir__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs) -> bool:  # real signature unknown
        return object.__eq__(self.get(), args[0] + 0, **kwargs)

    def __format__(self, *args, **kwargs) -> str:  # real signature unknown
        return object.__format__(self.get(), *args, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return object.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __ge__(self, *args, **kwargs):  # real signature unknown
        return object.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs):  # real signature unknown
        return object.__gt__(self.get(), args[0] + 0, **kwargs)

    def __hash__(self, *args, **kwargs) -> int:  # real signature unknown
        return object.__hash__(self.get(), *args, **kwargs)

    # def __init_subclass__(self, *args, **kwargs) -> None:  # real signature unknown
    #     return object.__init_subclass__(self, *args, **kwargs) # TODO Not Implemented

    # def __init__(self) -> None:  # known special case of object.__init__
    #     return object.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __le__(self, *args, **kwargs):  # real signature unknown
        return object.__le__(self.get(), args[0] + 0, **kwargs)

    def __lt__(self, *args, **kwargs):  # real signature unknown
        return object.__lt__(self.get(), args[0] + 0, **kwargs)

    # @staticmethod # known case of __new__
    # def __new__(cls, *more):  # known special case of object.__new__
    #     return object.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs) -> bool:  # real signature unknown
        return object.__ne__(self.get(), args[0] + 0, **kwargs)

    def __reduce_ex__(self, *args, **kwargs) -> tuple:  # real signature unknown
        return object.__reduce_ex__(self.get(), *args, **kwargs)

    def __reduce__(self, *args, **kwargs) -> tuple:  # real signature unknown
        return object.__reduce__(self.get(), *args, **kwargs)

    # def __repr__(self, *args, **kwargs) -> str:  # real signature unknown
    #     return object.__repr__(self, *args, **kwargs) # TODO Not Implemented

    # def __setattr__(self, *args, **kwargs) -> None:  # real signature unknown
    #     return object.__setattr__(self, *args, **kwargs) # TODO Not Implemented

    def __sizeof__(self, *args, **kwargs) -> int:  # real signature unknown
        return object.__sizeof__(self.get(), *args, **kwargs)

    def __str__(self, *args, **kwargs) -> str:  # real signature unknown
        return object.__str__(self.get(), *args, **kwargs)

    @classmethod # known case
    def __subclasshook__(cls, subclass):  # known special case of object.__subclasshook__
        pass  # Lahav


class DyIntMagicMethods(DyObjectMagicMethods):

    def bit_length(self) -> int:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def conjugate(self, *args, **kwargs):  # real signature unknown
        return int.conjugate(self.get(), *args, **kwargs)

    @classmethod # known case
    def from_bytes(cls, *args, **kwargs):  # real signature unknown
        pass  # Lahav

    def to_bytes(self, *args, **kwargs) -> bytes:  # real signature unknown
        return int.to_bytes(self.get(), *args, **kwargs)

    def __abs__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__abs__(self.get(), *args, **kwargs)

    def __add__(self, *args, **kwargs) -> int:  # real signature unknown
        self.set(int.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __and__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__and__(self.get(), *args, **kwargs)

    def __bool__(self, *args, **kwargs) -> bool:  # real signature unknown
        return int.__bool__(self.get(), *args, **kwargs)

    def __ceil__(self, *args, **kwargs):  # real signature unknown
        return int.__ceil__(self.get(), *args, **kwargs)

    def __divmod__(self, *args, **kwargs):  # real signature unknown
        self.set(int.__divmod__(self.get(), args[0] + 0, **kwargs))
        return self

    def __eq__(self, *args, **kwargs) -> bool:  # real signature unknown
        return int.__eq__(self.get(), args[0] + 0, **kwargs)

    def __float__(self, *args, **kwargs) -> float:  # real signature unknown
        return int.__float__(self.get(), *args, **kwargs)

    def __floordiv__(self, *args, **kwargs) -> int:  # real signature unknown
        self.set(int.__floordiv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __floor__(self, *args, **kwargs):  # real signature unknown
        return int.__floor__(self.get(), *args, **kwargs)

    def __format__(self, *args, **kwargs):  # real signature unknown
        return int.__format__(self.get(), *args, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return int.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        return int.__getnewargs__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs) -> bool:  # real signature unknown
        return int.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return int.__gt__(self.get(), args[0] + 0, **kwargs)

    def __hash__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__hash__(self.get(), *args, **kwargs)

    def __index__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__index__(self.get(), *args, **kwargs)

    # def __init__(self, x, base=10) -> None:  # known special case of int.__init__
    #     return int.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __int__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__int__(self.get(), *args, **kwargs)

    def __invert__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__invert__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs) -> bool:  # real signature unknown
        return int.__le__(self.get(), args[0] + 0, **kwargs)

    def __lshift__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__lshift__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return int.__lt__(self.get(), args[0] + 0, **kwargs)

    def __mod__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__mod__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs) -> int:  # real signature unknown
        self.set(int.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __neg__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__neg__(self.get(), *args, **kwargs)

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return int.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs) -> bool:  # real signature unknown
        return int.__ne__(self.get(), args[0] + 0, **kwargs)

    def __or__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__or__(self.get(), *args, **kwargs)

    def __pos__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__pos__(self.get(), *args, **kwargs)

    def __pow__(self, *args, **kwargs):  # real signature unknown
        self.set(int.__pow__(self.get(), args[0] + 0, **kwargs))
        return self

    def __radd__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__radd__(self.get(), *args, **kwargs)

    def __rand__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rand__(self.get(), *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):  # real signature unknown
        return int.__rdivmod__(self.get(), *args, **kwargs)

    # def __repr__(self, *args, **kwargs):  # real signature unknown
    #     return int.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __rfloordiv__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rfloordiv__(self.get(), *args, **kwargs)

    def __rlshift__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rlshift__(self.get(), *args, **kwargs)

    def __rmod__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rmod__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rmul__(self.get(), *args, **kwargs)

    def __ror__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__ror__(self.get(), *args, **kwargs)

    def __round__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__round__(self.get(), *args, **kwargs)

    def __rpow__(self, *args, **kwargs):  # real signature unknown
        return int.__rpow__(self.get(), *args, **kwargs)

    def __rrshift__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rrshift__(self.get(), *args, **kwargs)

    def __rshift__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rshift__(self.get(), *args, **kwargs)

    def __rsub__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rsub__(self.get(), *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs) -> float:  # real signature unknown
        return int.__rtruediv__(self.get(), *args, **kwargs)

    def __rxor__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__rxor__(self.get(), *args, **kwargs)

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        return int.__sizeof__(self.get(), *args, **kwargs)

    def __str__(self, *args, **kwargs) -> str:  # real signature unknown
        return int.__str__(self.get(), *args, **kwargs)

    def __sub__(self, *args, **kwargs) -> int:  # real signature unknown
        self.set(int.__sub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __truediv__(self, *args, **kwargs) -> float:  # real signature unknown
        self.set(int.__truediv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __trunc__(self, *args, **kwargs):  # real signature unknown
        return int.__trunc__(self.get(), *args, **kwargs)

    def __xor__(self, *args, **kwargs) -> int:  # real signature unknown
        return int.__xor__(self.get(), *args, **kwargs)


class DyBoolMagicMethods(DyIntMagicMethods):

    def __and__(self, *args, **kwargs) -> bool:  # real signature unknown
        return bool.__and__(self.get(), *args, **kwargs)

    # def __init__(self, x) -> None:  # real signature unknown; restored from __doc__
    #     return bool.__init__(self, *args, **kwargs) # TODO Not Implemented

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return bool.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __or__(self, *args, **kwargs) -> bool:  # real signature unknown
        return bool.__or__(self.get(), *args, **kwargs)

    def __rand__(self, *args, **kwargs) -> bool:  # real signature unknown
        return bool.__rand__(self.get(), *args, **kwargs)

    # def __repr__(self, *args, **kwargs):  # real signature unknown
    #     return bool.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __ror__(self, *args, **kwargs) -> bool:  # real signature unknown
        return bool.__ror__(self.get(), *args, **kwargs)

    def __rxor__(self, *args, **kwargs) -> bool:  # real signature unknown
        return bool.__rxor__(self.get(), *args, **kwargs)

    def __str__(self, *args, **kwargs):  # real signature unknown
        return bool.__str__(self.get(), *args, **kwargs)

    def __xor__(self, *args, **kwargs) -> bool:  # real signature unknown
        return bool.__xor__(self.get(), *args, **kwargs)


class DyDictMagicMethods(DyObjectMagicMethods):

    def clear(self) -> None:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def copy(self):  # real signature unknown; restored from __doc__
        pass  # Lahav

    @staticmethod # known case
    def fromkeys(*args, **kwargs):  # real signature unknown
        pass  # Lahav

    def get(self, *args, **kwargs):  # real signature unknown
        return dict.get(self.get(), *args, **kwargs)

    def items(self):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def keys(self):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def pop(self, k, d=None):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def popitem(self):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def setdefault(self, *args, **kwargs):  # real signature unknown
        return dict.setdefault(self.get(), *args, **kwargs)

    def update(self, E=None, **F) -> None:  # known special case of dict.update
        pass  # Lahav

    def values(self):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def __contains__(self, *args, **kwargs):  # real signature unknown
        return dict.__contains__(self.get(), *args, **kwargs)

    def __delitem__(self, *args, **kwargs):  # real signature unknown
        return dict.__delitem__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):  # real signature unknown
        return dict.__eq__(self.get(), args[0] + 0, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return dict.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __getitem__(self, y):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def __ge__(self, *args, **kwargs):  # real signature unknown
        return dict.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs):  # real signature unknown
        return dict.__gt__(self.get(), args[0] + 0, **kwargs)

    # def __init__(self, seq=None, **kwargs) -> None:  # known special case of dict.__init__
    #     return dict.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __iter__(self, *args, **kwargs):  # real signature unknown
        return dict.__iter__(self.get(), *args, **kwargs)

    def __len__(self, *args, **kwargs):  # real signature unknown
        return dict.__len__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs):  # real signature unknown
        return dict.__le__(self.get(), args[0] + 0, **kwargs)

    def __lt__(self, *args, **kwargs):  # real signature unknown
        return dict.__lt__(self.get(), args[0] + 0, **kwargs)

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return dict.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs):  # real signature unknown
        return dict.__ne__(self.get(), args[0] + 0, **kwargs)

    # def __repr__(self, *args, **kwargs):  # real signature unknown
    #     return dict.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __setitem__(self, *args, **kwargs):  # real signature unknown
        return dict.__setitem__(self.get(), *args, **kwargs)

    def __sizeof__(self):  # real signature unknown; restored from __doc__
        pass  # Lahav


class DyFloatMagicMethods(DyObjectMagicMethods):

    def as_integer_ratio(self):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def conjugate(self, *args, **kwargs):  # real signature unknown
        return float.conjugate(self.get(), *args, **kwargs)

    @staticmethod # known case
    def fromhex(*args, **kwargs) -> float:  # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass  # Lahav

    def hex(self) -> str:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def is_integer(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.is_integer(self.get(), *args, **kwargs)

    def __abs__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__abs__(self.get(), *args, **kwargs)

    def __add__(self, *args, **kwargs) -> float:  # real signature unknown
        self.set(float.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __bool__(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.__bool__(self.get(), *args, **kwargs)

    def __divmod__(self, *args, **kwargs):  # real signature unknown
        self.set(float.__divmod__(self.get(), args[0] + 0, **kwargs))
        return self

    def __eq__(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.__eq__(self.get(), args[0] + 0, **kwargs)

    def __float__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__float__(self.get(), *args, **kwargs)

    def __floordiv__(self, *args, **kwargs) -> float:  # real signature unknown
        self.set(float.__floordiv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __format__(self, *args, **kwargs):  # real signature unknown
        return float.__format__(self.get(), *args, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return float.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __getformat__(self, *args, **kwargs):  # real signature unknown
        return float.__getformat__(self.get(), *args, **kwargs)

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        return float.__getnewargs__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.__gt__(self.get(), args[0] + 0, **kwargs)

    def __hash__(self, *args, **kwargs) -> int:  # real signature unknown
        return float.__hash__(self.get(), *args, **kwargs)

    # def __init__(self, *args, **kwargs) -> None:  # real signature unknown
    #     return float.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __int__(self, *args, **kwargs) -> int:  # real signature unknown
        return float.__int__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.__le__(self.get(), args[0] + 0, **kwargs)

    def __lt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.__lt__(self.get(), args[0] + 0, **kwargs)

    def __mod__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__mod__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs) -> float:  # real signature unknown
        self.set(float.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __neg__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__neg__(self.get(), *args, **kwargs)

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return float.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs) -> bool:  # real signature unknown
        return float.__ne__(self.get(), args[0] + 0, **kwargs)

    def __pos__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__pos__(self.get(), *args, **kwargs)

    def __pow__(self, *args, **kwargs) -> float:  # real signature unknown
        self.set(float.__pow__(self.get(), args[0] + 0, **kwargs))
        return self

    def __radd__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__radd__(self.get(), *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):  # real signature unknown
        return float.__rdivmod__(self.get(), *args, **kwargs)

    # def __repr__(self, *args, **kwargs):  # real signature unknown
    #     return float.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __rfloordiv__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__rfloordiv__(self.get(), *args, **kwargs)

    def __rmod__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__rmod__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__rmul__(self.get(), *args, **kwargs)

    def __round__(self, *args, **kwargs) -> int:  # real signature unknown
        return float.__round__(self.get(), *args, **kwargs)

    def __rpow__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__rpow__(self.get(), *args, **kwargs)

    def __rsub__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__rsub__(self.get(), *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs) -> float:  # real signature unknown
        return float.__rtruediv__(self.get(), *args, **kwargs)

    def __set_format__(self, *args, **kwargs):  # real signature unknown
        return float.__set_format__(self.get(), *args, **kwargs)

    def __str__(self, *args, **kwargs) -> str:  # real signature unknown
        return float.__str__(self.get(), *args, **kwargs)

    def __sub__(self, *args, **kwargs) -> float:  # real signature unknown
        self.set(float.__sub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __truediv__(self, *args, **kwargs) -> float:  # real signature unknown
        self.set(float.__truediv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __trunc__(self, *args, **kwargs):  # real signature unknown
        return float.__trunc__(self.get(), *args, **kwargs)


class DyListMagicMethods(DyObjectMagicMethods):

    def append(self, *args, **kwargs) -> None:  # real signature unknown
        return list.append(self.get(), *args, **kwargs)

    def clear(self, *args, **kwargs) -> None:  # real signature unknown
        return list.clear(self.get(), *args, **kwargs)

    def copy(self, *args, **kwargs):  # real signature unknown
        return list.copy(self.get(), *args, **kwargs)

    def count(self, *args, **kwargs) -> int:  # real signature unknown
        return list.count(self.get(), *args, **kwargs)

    def extend(self, *args, **kwargs) -> None:  # real signature unknown
        return list.extend(self.get(), *args, **kwargs)

    def index(self, *args, **kwargs) -> int:  # real signature unknown
        return list.index(self.get(), *args, **kwargs)

    def insert(self, *args, **kwargs) -> None:  # real signature unknown
        return list.insert(self.get(), *args, **kwargs)

    def pop(self, *args, **kwargs):  # real signature unknown
        return list.pop(self.get(), *args, **kwargs)

    def remove(self, *args, **kwargs) -> None:  # real signature unknown
        return list.remove(self.get(), *args, **kwargs)

    def reverse(self, *args, **kwargs) -> None:  # real signature unknown
        return list.reverse(self.get(), *args, **kwargs)

    def sort(self, *args, **kwargs) -> None:  # real signature unknown
        return list.sort(self.get(), *args, **kwargs)

    def __add__(self, *args, **kwargs):  # real signature unknown
        self.set(list.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __contains__(self, *args, **kwargs) -> bool:  # real signature unknown
        return list.__contains__(self.get(), *args, **kwargs)

    def __delitem__(self, *args, **kwargs) -> None:  # real signature unknown
        return list.__delitem__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):  # real signature unknown
        return list.__eq__(self.get(), args[0] + 0, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return list.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __getitem__(self, y):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def __ge__(self, *args, **kwargs) -> bool:  # real signature unknown
        return list.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return list.__gt__(self.get(), args[0] + 0, **kwargs)

    def __iadd__(self, *args, **kwargs):  # real signature unknown
        return list.__iadd__(self.get(), *args, **kwargs)

    def __imul__(self, *args, **kwargs):  # real signature unknown
        return list.__imul__(self.get(), *args, **kwargs)

    # def __init__(self, seq=()) -> None:  # known special case of list.__init__
    #     return list.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __iter__(self, *args, **kwargs):  # real signature unknown
        return list.__iter__(self.get(), *args, **kwargs)

    def __len__(self, *args, **kwargs) -> int:  # real signature unknown
        return list.__len__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs) -> bool:  # real signature unknown
        return list.__le__(self.get(), args[0] + 0, **kwargs)

    def __lt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return list.__lt__(self.get(), args[0] + 0, **kwargs)

    def __mul__(self, *args, **kwargs):  # real signature unknown
        self.set(list.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return list.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs):  # real signature unknown
        return list.__ne__(self.get(), args[0] + 0, **kwargs)

    # def __repr__(self, *args, **kwargs):  # real signature unknown
    #     return list.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __reversed__(self, *args, **kwargs):  # real signature unknown
        return list.__reversed__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):  # real signature unknown
        return list.__rmul__(self.get(), *args, **kwargs)

    def __setitem__(self, *args, **kwargs) -> None:  # real signature unknown
        return list.__setitem__(self.get(), *args, **kwargs)

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        return list.__sizeof__(self.get(), *args, **kwargs)


class DySetMagicMethods(DyObjectMagicMethods):

    def add(self, *args, **kwargs) -> None:  # real signature unknown
        return set.add(self.get(), *args, **kwargs)

    def clear(self, *args, **kwargs) -> None:  # real signature unknown
        return set.clear(self.get(), *args, **kwargs)

    def copy(self, *args, **kwargs):  # real signature unknown
        return set.copy(self.get(), *args, **kwargs)

    def difference(self, *args, **kwargs):  # real signature unknown
        return set.difference(self.get(), *args, **kwargs)

    def difference_update(self, *args, **kwargs) -> None:  # real signature unknown
        return set.difference_update(self.get(), *args, **kwargs)

    def discard(self, *args, **kwargs) -> None:  # real signature unknown
        return set.discard(self.get(), *args, **kwargs)

    def intersection(self, *args, **kwargs):  # real signature unknown
        return set.intersection(self.get(), *args, **kwargs)

    def intersection_update(self, *args, **kwargs) -> None:  # real signature unknown
        return set.intersection_update(self.get(), *args, **kwargs)

    def isdisjoint(self, *args, **kwargs) -> bool:  # real signature unknown
        return set.isdisjoint(self.get(), *args, **kwargs)

    def issubset(self, *args, **kwargs) -> bool:  # real signature unknown
        return set.issubset(self.get(), *args, **kwargs)

    def issuperset(self, *args, **kwargs) -> bool:  # real signature unknown
        return set.issuperset(self.get(), *args, **kwargs)

    def pop(self, *args, **kwargs):  # real signature unknown
        return set.pop(self.get(), *args, **kwargs)

    def remove(self, *args, **kwargs) -> None:  # real signature unknown
        return set.remove(self.get(), *args, **kwargs)

    def symmetric_difference(self, *args, **kwargs):  # real signature unknown
        return set.symmetric_difference(self.get(), *args, **kwargs)

    def symmetric_difference_update(self, *args, **kwargs) -> None:  # real signature unknown
        return set.symmetric_difference_update(self.get(), *args, **kwargs)

    def union(self, *args, **kwargs):  # real signature unknown
        return set.union(self.get(), *args, **kwargs)

    def update(self, *args, **kwargs) -> None:  # real signature unknown
        return set.update(self.get(), *args, **kwargs)

    def __and__(self, *args, **kwargs):  # real signature unknown
        return set.__and__(self.get(), *args, **kwargs)

    def __contains__(self, y) -> bool:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def __eq__(self, *args, **kwargs):  # real signature unknown
        return set.__eq__(self.get(), args[0] + 0, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return set.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __ge__(self, *args, **kwargs) -> bool:  # real signature unknown
        return set.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return set.__gt__(self.get(), args[0] + 0, **kwargs)

    def __iand__(self, *args, **kwargs):  # real signature unknown
        return set.__iand__(self.get(), *args, **kwargs)

    # def __init__(self, seq=()) -> None:  # known special case of set.__init__
    #     return set.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __ior__(self, *args, **kwargs):  # real signature unknown
        return set.__ior__(self.get(), *args, **kwargs)

    def __isub__(self, *args, **kwargs):  # real signature unknown
        return set.__isub__(self.get(), *args, **kwargs)

    def __iter__(self, *args, **kwargs):  # real signature unknown
        return set.__iter__(self.get(), *args, **kwargs)

    def __ixor__(self, *args, **kwargs):  # real signature unknown
        return set.__ixor__(self.get(), *args, **kwargs)

    def __len__(self, *args, **kwargs) -> int:  # real signature unknown
        return set.__len__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs) -> bool:  # real signature unknown
        return set.__le__(self.get(), args[0] + 0, **kwargs)

    def __lt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return set.__lt__(self.get(), args[0] + 0, **kwargs)

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return set.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs):  # real signature unknown
        return set.__ne__(self.get(), args[0] + 0, **kwargs)

    def __or__(self, *args, **kwargs):  # real signature unknown
        return set.__or__(self.get(), *args, **kwargs)

    def __rand__(self, *args, **kwargs):  # real signature unknown
        return set.__rand__(self.get(), *args, **kwargs)

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        return set.__reduce__(self.get(), *args, **kwargs)

    # def __repr__(self, *args, **kwargs):  # real signature unknown
    #     return set.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __ror__(self, *args, **kwargs):  # real signature unknown
        return set.__ror__(self.get(), *args, **kwargs)

    def __rsub__(self, *args, **kwargs):  # real signature unknown
        return set.__rsub__(self.get(), *args, **kwargs)

    def __rxor__(self, *args, **kwargs):  # real signature unknown
        return set.__rxor__(self.get(), *args, **kwargs)

    def __sizeof__(self):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def __sub__(self, *args, **kwargs):  # real signature unknown
        self.set(set.__sub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __xor__(self, *args, **kwargs):  # real signature unknown
        return set.__xor__(self.get(), *args, **kwargs)


class DyStrMagicMethods(DyObjectMagicMethods):

    def capitalize(self, *args, **kwargs) -> str:  # real signature unknown
        return str.capitalize(self.get(), *args, **kwargs)

    def casefold(self, *args, **kwargs) -> str:  # real signature unknown
        return str.casefold(self.get(), *args, **kwargs)

    def center(self, *args, **kwargs) -> str:  # real signature unknown
        return str.center(self.get(), *args, **kwargs)

    def count(self, sub, start=None, end=None) -> int:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def encode(self, *args, **kwargs) -> bytes:  # real signature unknown
        return str.encode(self.get(), *args, **kwargs)

    def endswith(self, suffix, start=None, end=None):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def expandtabs(self, *args, **kwargs) -> str:  # real signature unknown
        return str.expandtabs(self.get(), *args, **kwargs)

    def find(self, sub, start=None, end=None) -> int:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def format(self, *args, **kwargs) -> str:  # known special case of str.format
        return str.format(self.get(), *args, **kwargs)

    def format_map(self, mapping) -> str:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def index(self, sub, start=None, end=None) -> int:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def isalnum(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isalnum(self.get(), *args, **kwargs)

    def isalpha(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isalpha(self.get(), *args, **kwargs)

    def isascii(self, *args, **kwargs):  # real signature unknown
        return str.isascii(self.get(), *args, **kwargs)

    def isdecimal(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isdecimal(self.get(), *args, **kwargs)

    def isdigit(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isdigit(self.get(), *args, **kwargs)

    def isidentifier(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isidentifier(self.get(), *args, **kwargs)

    def islower(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.islower(self.get(), *args, **kwargs)

    def isnumeric(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isnumeric(self.get(), *args, **kwargs)

    def isprintable(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isprintable(self.get(), *args, **kwargs)

    def isspace(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isspace(self.get(), *args, **kwargs)

    def istitle(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.istitle(self.get(), *args, **kwargs)

    def isupper(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.isupper(self.get(), *args, **kwargs)

    def join(self, ab=None, pq=None, rs=None) -> str:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def ljust(self, *args, **kwargs) -> str:  # real signature unknown
        return str.ljust(self.get(), *args, **kwargs)

    def lower(self, *args, **kwargs) -> str:  # real signature unknown
        return str.lower(self.get(), *args, **kwargs)

    def lstrip(self, *args, **kwargs) -> str:  # real signature unknown
        return str.lstrip(self.get(), *args, **kwargs)

    def maketrans(self, *args, **kwargs):  # real signature unknown
        return str.maketrans(self.get(), *args, **kwargs)

    def partition(self, *args, **kwargs):  # real signature unknown
        return str.partition(self.get(), *args, **kwargs)

    def replace(self, *args, **kwargs) -> str:  # real signature unknown
        return str.replace(self.get(), *args, **kwargs)

    def rfind(self, sub, start=None, end=None) -> int:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def rindex(self, sub, start=None, end=None) -> int:  # real signature unknown; restored from __doc__
        pass  # Lahav

    def rjust(self, *args, **kwargs) -> str:  # real signature unknown
        return str.rjust(self.get(), *args, **kwargs)

    def rpartition(self, *args, **kwargs):  # real signature unknown
        return str.rpartition(self.get(), *args, **kwargs)

    def rsplit(self, *args, **kwargs):  # real signature unknown
        return str.rsplit(self.get(), *args, **kwargs)

    def rstrip(self, *args, **kwargs) -> str:  # real signature unknown
        return str.rstrip(self.get(), *args, **kwargs)

    def split(self, *args, **kwargs):  # real signature unknown
        return str.split(self.get(), *args, **kwargs)

    def splitlines(self, *args, **kwargs):  # real signature unknown
        return str.splitlines(self.get(), *args, **kwargs)

    def startswith(self, prefix, start=None, end=None):  # real signature unknown; restored from __doc__
        pass  # Lahav

    def strip(self, *args, **kwargs) -> str:  # real signature unknown
        return str.strip(self.get(), *args, **kwargs)

    def swapcase(self, *args, **kwargs) -> str:  # real signature unknown
        return str.swapcase(self.get(), *args, **kwargs)

    def title(self, *args, **kwargs) -> str:  # real signature unknown
        return str.title(self.get(), *args, **kwargs)

    def translate(self, *args, **kwargs) -> str:  # real signature unknown
        return str.translate(self.get(), *args, **kwargs)

    def upper(self, *args, **kwargs) -> str:  # real signature unknown
        return str.upper(self.get(), *args, **kwargs)

    def zfill(self, *args, **kwargs) -> str:  # real signature unknown
        return str.zfill(self.get(), *args, **kwargs)

    def __add__(self, *args, **kwargs) -> str:  # real signature unknown
        self.set(str.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __contains__(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.__contains__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.__eq__(self.get(), args[0] + 0, **kwargs)

    def __format__(self, *args, **kwargs):  # real signature unknown
        return str.__format__(self.get(), *args, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return str.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __getitem__(self, *args, **kwargs) -> str:  # real signature unknown
        return str.__getitem__(self.get(), *args, **kwargs)

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        return str.__getnewargs__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.__gt__(self.get(), args[0] + 0, **kwargs)

    def __hash__(self, *args, **kwargs) -> int:  # real signature unknown
        return str.__hash__(self.get(), *args, **kwargs)

    # def __init__(self, value='', encoding=None, errors='strict') -> None:  # known special case of str.__init__
    #     return str.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __iter__(self, *args, **kwargs):  # real signature unknown
        return str.__iter__(self.get(), *args, **kwargs)

    def __len__(self, *args, **kwargs) -> int:  # real signature unknown
        return str.__len__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.__le__(self.get(), args[0] + 0, **kwargs)

    def __lt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.__lt__(self.get(), args[0] + 0, **kwargs)

    def __mod__(self, *args, **kwargs) -> str:  # real signature unknown
        return str.__mod__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs) -> str:  # real signature unknown
        self.set(str.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return str.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs) -> bool:  # real signature unknown
        return str.__ne__(self.get(), args[0] + 0, **kwargs)

    # def __repr__(self, *args, **kwargs) -> str:  # real signature unknown
    #     return str.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __rmod__(self, *args, **kwargs):  # real signature unknown
        return str.__rmod__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs) -> str:  # real signature unknown
        return str.__rmul__(self.get(), *args, **kwargs)

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        return str.__sizeof__(self.get(), *args, **kwargs)

    def __str__(self, *args, **kwargs) -> str:  # real signature unknown
        return str.__str__(self.get(), *args, **kwargs)


class DyTupleMagicMethods(DyObjectMagicMethods):

    def count(self, *args, **kwargs) -> int:  # real signature unknown
        return tuple.count(self.get(), *args, **kwargs)

    def index(self, *args, **kwargs) -> int:  # real signature unknown
        return tuple.index(self.get(), *args, **kwargs)

    def __add__(self, *args, **kwargs):  # real signature unknown
        self.set(tuple.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __contains__(self, *args, **kwargs) -> bool:  # real signature unknown
        return tuple.__contains__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):  # real signature unknown
        return tuple.__eq__(self.get(), args[0] + 0, **kwargs)

    # def __getattribute__(self, *args, **kwargs):  # real signature unknown
    #     return tuple.__getattribute__(self, *args, **kwargs) # TODO Not Implemented

    def __getitem__(self, *args, **kwargs):  # real signature unknown
        return tuple.__getitem__(self.get(), *args, **kwargs)

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        return tuple.__getnewargs__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs) -> bool:  # real signature unknown
        return tuple.__ge__(self.get(), args[0] + 0, **kwargs)

    def __gt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return tuple.__gt__(self.get(), args[0] + 0, **kwargs)

    def __hash__(self, *args, **kwargs):  # real signature unknown
        return tuple.__hash__(self.get(), *args, **kwargs)

    # def __init__(self, seq=()):  # known special case of tuple.__init__
    #     return tuple.__init__(self, *args, **kwargs) # TODO Not Implemented

    def __iter__(self, *args, **kwargs):  # real signature unknown
        return tuple.__iter__(self.get(), *args, **kwargs)

    def __len__(self, *args, **kwargs) -> int:  # real signature unknown
        return tuple.__len__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs) -> bool:  # real signature unknown
        return tuple.__le__(self.get(), args[0] + 0, **kwargs)

    def __lt__(self, *args, **kwargs) -> bool:  # real signature unknown
        return tuple.__lt__(self.get(), args[0] + 0, **kwargs)

    def __mul__(self, *args, **kwargs):  # real signature unknown
        self.set(tuple.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    # @staticmethod # known case of __new__
    # def __new__(*args, **kwargs):  # real signature unknown
    #     return tuple.__new__(self, *args, **kwargs) # TODO Not Implemented

    def __ne__(self, *args, **kwargs):  # real signature unknown
        return tuple.__ne__(self.get(), args[0] + 0, **kwargs)

    # def __repr__(self, *args, **kwargs):  # real signature unknown
    #     return tuple.__repr__(self, *args, **kwargs) # TODO Not Implemented

    def __rmul__(self, *args, **kwargs):  # real signature unknown
        return tuple.__rmul__(self.get(), *args, **kwargs)


class DyObject(DyObjectMagicMethods, DyObjectConditions, DynamicObjectInterface):

    type = "DynamicObject"

    def __init__(self, value=None, builtin=False):
        super(DyObject, self).__init__()
        self.__value__: object = value
        self.__name__: str = "__name__"
        self._is_builtin: bool = builtin

    def _set_empty(self, value):
        old_val = self._get()
        self.__log_p__("{} = {}".format(self.__name__, value))
        self._prepareAndRunTriggers(self, old_val, value)

    def _set(self, value):
        self.__value__ = value

    def set(self, value):
        old_val = self._get()
        self._set(value)
        self.__log_p__("{} = {}".format(self.__name__, value))
        self._prepareAndRunTriggers(self, old_val, value)

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
