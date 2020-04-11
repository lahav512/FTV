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
        self.set(object.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(object.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(object.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(object.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(object.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(object.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return object.__repr__(self.get(), *args, **kwargs)


class DyIntMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        self.set(int.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __divmod__(self, *args, **kwargs):
        self.set(int.__divmod__(self.get(), args[0] + 0, **kwargs))
        return self

    def __eq__(self, *args, **kwargs):
        self.set(int.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __floordiv__(self, *args, **kwargs):
        self.set(int.__floordiv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(int.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(int.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(int.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(int.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __mul__(self, *args, **kwargs):
        self.set(int.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(int.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __pow__(self, *args, **kwargs):
        self.set(int.__pow__(self.get(), args[0] + 0, **kwargs))
        return self

    def __radd__(self, *args, **kwargs):
        self.set(int.__radd__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rand__(self, *args, **kwargs):
        self.set(int.__rand__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return int.__repr__(self.get(), *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        self.set(int.__rfloordiv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rlshift__(self, *args, **kwargs):
        self.set(int.__rlshift__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rmod__(self, *args, **kwargs):
        self.set(int.__rmod__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rmul__(self, *args, **kwargs):
        self.set(int.__rmul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ror__(self, *args, **kwargs):
        self.set(int.__ror__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rrshift__(self, *args, **kwargs):
        self.set(int.__rrshift__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rsub__(self, *args, **kwargs):
        self.set(int.__rsub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rxor__(self, *args, **kwargs):
        self.set(int.__rxor__(self.get(), args[0] + 0, **kwargs))
        return self

    def __sub__(self, *args, **kwargs):
        self.set(int.__sub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __truediv__(self, *args, **kwargs):
        self.set(int.__truediv__(self.get(), args[0] + 0, **kwargs))
        return self


class DyBoolMagicMethods(DyIntMagicMethods):

    def __rand__(self, *args, **kwargs):
        self.set(bool.__rand__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return bool.__repr__(self.get(), *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        self.set(bool.__ror__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rxor__(self, *args, **kwargs):
        self.set(bool.__rxor__(self.get(), args[0] + 0, **kwargs))
        return self


class DyDictMagicMethods(DyObjectMagicMethods):

    def __eq__(self, *args, **kwargs):
        self.set(dict.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(dict.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(dict.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(dict.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(dict.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(dict.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return dict.__repr__(self.get(), *args, **kwargs)


class DyFloatMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        self.set(float.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __divmod__(self, *args, **kwargs):
        self.set(float.__divmod__(self.get(), args[0] + 0, **kwargs))
        return self

    def __eq__(self, *args, **kwargs):
        self.set(float.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __floordiv__(self, *args, **kwargs):
        self.set(float.__floordiv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(float.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(float.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(float.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(float.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __mul__(self, *args, **kwargs):
        self.set(float.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(float.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __pow__(self, *args, **kwargs):
        self.set(float.__pow__(self.get(), args[0] + 0, **kwargs))
        return self

    def __radd__(self, *args, **kwargs):
        self.set(float.__radd__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return float.__repr__(self.get(), *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        self.set(float.__rfloordiv__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rmod__(self, *args, **kwargs):
        self.set(float.__rmod__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rmul__(self, *args, **kwargs):
        self.set(float.__rmul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rsub__(self, *args, **kwargs):
        self.set(float.__rsub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __sub__(self, *args, **kwargs):
        self.set(float.__sub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __truediv__(self, *args, **kwargs):
        self.set(float.__truediv__(self.get(), args[0] + 0, **kwargs))
        return self


class DyListMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        self.set(list.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __eq__(self, *args, **kwargs):
        self.set(list.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(list.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(list.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(list.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(list.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __mul__(self, *args, **kwargs):
        self.set(list.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(list.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return list.__repr__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        self.set(list.__rmul__(self.get(), args[0] + 0, **kwargs))
        return self


class DySetMagicMethods(DyObjectMagicMethods):

    def __eq__(self, *args, **kwargs):
        self.set(set.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(set.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(set.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(set.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(set.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(set.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rand__(self, *args, **kwargs):
        self.set(set.__rand__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return set.__repr__(self.get(), *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        self.set(set.__ror__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rsub__(self, *args, **kwargs):
        self.set(set.__rsub__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rxor__(self, *args, **kwargs):
        self.set(set.__rxor__(self.get(), args[0] + 0, **kwargs))
        return self

    def __sub__(self, *args, **kwargs):
        self.set(set.__sub__(self.get(), args[0] + 0, **kwargs))
        return self


class DyStrMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        self.set(str.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __eq__(self, *args, **kwargs):
        self.set(str.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(str.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(str.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(str.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(str.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __mul__(self, *args, **kwargs):
        self.set(str.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(str.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return str.__repr__(self.get(), *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        self.set(str.__rmod__(self.get(), args[0] + 0, **kwargs))
        return self

    def __rmul__(self, *args, **kwargs):
        self.set(str.__rmul__(self.get(), args[0] + 0, **kwargs))
        return self


class DyTupleMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        self.set(tuple.__add__(self.get(), args[0] + 0, **kwargs))
        return self

    def __eq__(self, *args, **kwargs):
        self.set(tuple.__eq__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ge__(self, *args, **kwargs):
        self.set(tuple.__ge__(self.get(), args[0] + 0, **kwargs))
        return self

    def __gt__(self, *args, **kwargs):
        self.set(tuple.__gt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __le__(self, *args, **kwargs):
        self.set(tuple.__le__(self.get(), args[0] + 0, **kwargs))
        return self

    def __lt__(self, *args, **kwargs):
        self.set(tuple.__lt__(self.get(), args[0] + 0, **kwargs))
        return self

    def __mul__(self, *args, **kwargs):
        self.set(tuple.__mul__(self.get(), args[0] + 0, **kwargs))
        return self

    def __ne__(self, *args, **kwargs):
        self.set(tuple.__ne__(self.get(), args[0] + 0, **kwargs))
        return self

    def __repr__(self, *args, **kwargs):
        return tuple.__repr__(self.get(), *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        self.set(tuple.__rmul__(self.get(), args[0] + 0, **kwargs))
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
