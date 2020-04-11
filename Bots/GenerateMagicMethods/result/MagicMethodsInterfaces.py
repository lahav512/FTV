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

    def __eq__(self, *args, **kwargs):
        return object.__eq__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return object.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return object.__gt__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return object.__le__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return object.__lt__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return object.__ne__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return object.__repr__(self.get(), *args, **kwargs)


class DyIntMagicMethods(DyObjectMagicMethods):

    def __abs__(self, *args, **kwargs):
        return int.__abs__(self.get(), *args, **kwargs)

    def __add__(self, *args, **kwargs):
        return int.__add__(self.get(), *args, **kwargs)

    def __and__(self, *args, **kwargs):
        return int.__and__(self.get(), *args, **kwargs)

    def __ceil__(self, *args, **kwargs):
        return int.__ceil__(self.get(), *args, **kwargs)

    def __divmod__(self, *args, **kwargs):
        return int.__divmod__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return int.__eq__(self.get(), *args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        return int.__floordiv__(self.get(), *args, **kwargs)

    def __floor__(self, *args, **kwargs):
        return int.__floor__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return int.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return int.__gt__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return int.__le__(self.get(), *args, **kwargs)

    def __lshift__(self, *args, **kwargs):
        return int.__lshift__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return int.__lt__(self.get(), *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        return int.__mod__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return int.__mul__(self.get(), *args, **kwargs)

    def __neg__(self, *args, **kwargs):
        return int.__neg__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return int.__ne__(self.get(), *args, **kwargs)

    def __or__(self, *args, **kwargs):
        return int.__or__(self.get(), *args, **kwargs)

    def __pos__(self, *args, **kwargs):
        return int.__pos__(self.get(), *args, **kwargs)

    def __pow__(self, *args, **kwargs):
        return int.__pow__(self.get(), *args, **kwargs)

    def __radd__(self, *args, **kwargs):
        return int.__radd__(self.get(), *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        return int.__rand__(self.get(), *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):
        return int.__rdivmod__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return int.__repr__(self.get(), *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        return int.__rfloordiv__(self.get(), *args, **kwargs)

    def __rlshift__(self, *args, **kwargs):
        return int.__rlshift__(self.get(), *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        return int.__rmod__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return int.__rmul__(self.get(), *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        return int.__ror__(self.get(), *args, **kwargs)

    def __round__(self, *args, **kwargs):
        return int.__round__(self.get(), *args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        return int.__rpow__(self.get(), *args, **kwargs)

    def __rrshift__(self, *args, **kwargs):
        return int.__rrshift__(self.get(), *args, **kwargs)

    def __rshift__(self, *args, **kwargs):
        return int.__rshift__(self.get(), *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        return int.__rsub__(self.get(), *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        return int.__rtruediv__(self.get(), *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        return int.__rxor__(self.get(), *args, **kwargs)

    def __sub__(self, *args, **kwargs):
        return int.__sub__(self.get(), *args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        return int.__truediv__(self.get(), *args, **kwargs)

    def __trunc__(self, *args, **kwargs):
        return int.__trunc__(self.get(), *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        return int.__xor__(self.get(), *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        self.set(int.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __iand__(self, *args, **kwargs):
        self.set(int.__and__(self.get(), args[0] + 0, **kwargs))
        return self

    def __imul__(self, *args, **kwargs):
        self.set(int.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ior__(self, *args, **kwargs):
        self.set(int.__or__(self.get(), args[0] + 0, **kwargs))
        return self

    def __isub__(self, *args, **kwargs):
        self.set(int.__sub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ixor__(self, *args, **kwargs):
        self.set(int.__xor__(self.get(), args[0] + 0, **kwargs))
        return self


class DyBoolMagicMethods(DyIntMagicMethods):

    def __and__(self, *args, **kwargs):
        return bool.__and__(self.get(), *args, **kwargs)

    def __or__(self, *args, **kwargs):
        return bool.__or__(self.get(), *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        return bool.__rand__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return bool.__repr__(self.get(), *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        return bool.__ror__(self.get(), *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        return bool.__rxor__(self.get(), *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        return bool.__xor__(self.get(), *args, **kwargs)

    def __iand__(self, *args, **kwargs):
        self.set(bool.__and__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ior__(self, *args, **kwargs):
        self.set(bool.__or__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ixor__(self, *args, **kwargs):
        self.set(bool.__xor__(self.get(), args[0] + 0, **kwargs))
        return self


class DyDictMagicMethods(DyObjectMagicMethods):

    def __eq__(self, *args, **kwargs):
        return dict.__eq__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return dict.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return dict.__gt__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return dict.__le__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return dict.__lt__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return dict.__ne__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return dict.__repr__(self.get(), *args, **kwargs)


class DyFloatMagicMethods(DyObjectMagicMethods):

    def __abs__(self, *args, **kwargs):
        return float.__abs__(self.get(), *args, **kwargs)

    def __add__(self, *args, **kwargs):
        return float.__add__(self.get(), *args, **kwargs)

    def __divmod__(self, *args, **kwargs):
        return float.__divmod__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return float.__eq__(self.get(), *args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        return float.__floordiv__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return float.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return float.__gt__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return float.__le__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return float.__lt__(self.get(), *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        return float.__mod__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return float.__mul__(self.get(), *args, **kwargs)

    def __neg__(self, *args, **kwargs):
        return float.__neg__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return float.__ne__(self.get(), *args, **kwargs)

    def __pos__(self, *args, **kwargs):
        return float.__pos__(self.get(), *args, **kwargs)

    def __pow__(self, *args, **kwargs):
        return float.__pow__(self.get(), *args, **kwargs)

    def __radd__(self, *args, **kwargs):
        return float.__radd__(self.get(), *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):
        return float.__rdivmod__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return float.__repr__(self.get(), *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        return float.__rfloordiv__(self.get(), *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        return float.__rmod__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return float.__rmul__(self.get(), *args, **kwargs)

    def __round__(self, *args, **kwargs):
        return float.__round__(self.get(), *args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        return float.__rpow__(self.get(), *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        return float.__rsub__(self.get(), *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        return float.__rtruediv__(self.get(), *args, **kwargs)

    def __sub__(self, *args, **kwargs):
        return float.__sub__(self.get(), *args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        return float.__truediv__(self.get(), *args, **kwargs)

    def __trunc__(self, *args, **kwargs):
        return float.__trunc__(self.get(), *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        self.set(float.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __imul__(self, *args, **kwargs):
        self.set(float.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __isub__(self, *args, **kwargs):
        self.set(float.__sub__(self.get(), args[0] + 0, **kwargs))
        return self


class DyListMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        return list.__add__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return list.__eq__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return list.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return list.__gt__(self.get(), *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        self.set(list.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __imul__(self, *args, **kwargs):
        self.set(list.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        return list.__le__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return list.__lt__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return list.__mul__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return list.__ne__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return list.__repr__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return list.__rmul__(self.get(), *args, **kwargs)


class DySetMagicMethods(DyObjectMagicMethods):

    def __and__(self, *args, **kwargs):
        return set.__and__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return set.__eq__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return set.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return set.__gt__(self.get(), *args, **kwargs)

    def __iand__(self, *args, **kwargs):
        self.set(set.__and__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ior__(self, *args, **kwargs):
        self.set(set.__or__(self.get(), args[0] + 0, **kwargs))
        return self

    def __isub__(self, *args, **kwargs):
        self.set(set.__sub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ixor__(self, *args, **kwargs):
        self.set(set.__xor__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        return set.__le__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return set.__lt__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return set.__ne__(self.get(), *args, **kwargs)

    def __or__(self, *args, **kwargs):
        return set.__or__(self.get(), *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        return set.__rand__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return set.__repr__(self.get(), *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        return set.__ror__(self.get(), *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        return set.__rsub__(self.get(), *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        return set.__rxor__(self.get(), *args, **kwargs)

    def __sub__(self, *args, **kwargs):
        return set.__sub__(self.get(), *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        return set.__xor__(self.get(), *args, **kwargs)


class DyStrMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        return str.__add__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return str.__eq__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return str.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return str.__gt__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return str.__le__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return str.__lt__(self.get(), *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        return str.__mod__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return str.__mul__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return str.__ne__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return str.__repr__(self.get(), *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        return str.__rmod__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return str.__rmul__(self.get(), *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        self.set(str.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __imul__(self, *args, **kwargs):
        self.set(str.__mul__(self.get(), args[0] + 0, **kwargs))
        return self


class DyTupleMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        return tuple.__add__(self.get(), *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return tuple.__eq__(self.get(), *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return tuple.__ge__(self.get(), *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return tuple.__gt__(self.get(), *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return tuple.__le__(self.get(), *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return tuple.__lt__(self.get(), *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return tuple.__mul__(self.get(), *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return tuple.__ne__(self.get(), *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return tuple.__repr__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return tuple.__rmul__(self.get(), *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        self.set(tuple.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __imul__(self, *args, **kwargs):
        self.set(tuple.__mul__(self.get(), args[0] + 0, **kwargs))
        return self


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
