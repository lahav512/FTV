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

    def __delattr__(self, *args, **kwargs):
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs):
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs):
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs):
        """
        This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self):
        """ Initialize self.  See help(type(self)) for accurate signature. """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__

    def __new__(cls, *more):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs):
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs):
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs):
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs):
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs):
        """ Return str(self). """
        pass

    @classmethod  # known case

    def __subclasshook__(cls, subclass):
        """
        Abstract classes can override this to customize issubclass().
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass


class DyIntMagicMethods(DyObjectMagicMethods):

    def __abs__(self, *args, **kwargs):
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs):
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs):
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs):
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs):
        """ Ceiling of an Integral returns itself. """
        pass

    def __divmod__(self, *args, **kwargs):
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs):
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs):
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs):
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs):
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs):
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs):
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, x, base=10):
        """
        int([x]) -> integer
        int(x, base=10) -> integer

        Convert a number or string to an integer, or return 0 if no arguments
        are given.  If x is a number, return x.__int__().  For floating point
        numbers, this truncates towards zero.

        If x is not a number or if base is given, then x must be a string,
        bytes, or bytearray instance representing an integer literal in the
        given base.  The literal can be preceded by '+' or '-' and be surrounded
        by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
        Base 0 means to interpret the base from the string as an integer literal.
        >>> int('0b100', base=0)
        4
        # (copied from class doc)
        """
        pass

    def __int__(self, *args, **kwargs):
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs):
        """ ~self """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs):
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs):
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs):
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs):
        """ -self """
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs):
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs):
        """ +self """
        pass

    def __pow__(self, *args, **kwargs):
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs):
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs):
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs):
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs):
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs):
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs):
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs):
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs):
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs):
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs):
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs):
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs):
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs):
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs):
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs):
        """ Return value^self. """
        pass

    def __sizeof__(self, *args, **kwargs):
        """ Returns size in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs):
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs):
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs):
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs):
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs):
        """ Return self^value. """
        pass


class DyBoolMagicMethods(DyIntMagicMethods):

    def __and__(self, *args, **kwargs):
        """ Return self&value. """
        pass

    def __init__(self, x):
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs):
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs):
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs):
        """ Return value|self. """
        pass

    def __rxor__(self, *args, **kwargs):
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs):
        """ Return str(self). """
        pass

    def __xor__(self, *args, **kwargs):
        """ Return self^value. """
        pass


class DyDictMagicMethods(DyObjectMagicMethods):

    def __contains__(self, *args, **kwargs):
        """ True if the dictionary has the specified key, else False. """
        pass

    def __delitem__(self, *args, **kwargs):
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, y):
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __init__(self, seq=None, **kwargs):
        """
        dict() -> new empty dictionary
        dict(mapping) -> new dictionary initialized from a mapping object's
            (key, value) pairs
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  dict(one=1, two=2)
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs):
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs):
        """ Set self[key] to value. """
        pass

    def __sizeof__(self):
        """ D.__sizeof__() -> size of D in memory, in bytes """
        pass


class DyFloatMagicMethods(DyObjectMagicMethods):

    def __abs__(self, *args, **kwargs):
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs):
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs):
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs):
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs):
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs):
        """ Return self//value. """
        pass

    def __format__(self, *args, **kwargs):
        """ Formats the float according to format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __getformat__(self, *args, **kwargs):
        """
        You probably don't want to use this function.

          typestr
            Must be 'double' or 'float'.

        It exists mainly to be used in Python's test suite.

        This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
        little-endian' best describes the format of floating point numbers used by the
        C type named by typestr.
        """
        pass

    def __getnewargs__(self, *args, **kwargs):
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs):
        pass

    def __int__(self, *args, **kwargs):
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs):
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs):
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs):
        """ -self """
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs):
        """ +self """
        pass

    def __pow__(self, *args, **kwargs):
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs):
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs):
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs):
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs):
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs):
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs):
        """
        Return the Integral closest to x, rounding half toward even.

        When an argument is passed, work like built-in round(x, ndigits).
        """
        pass

    def __rpow__(self, *args, **kwargs):
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs):
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs):
        """ Return value/self. """
        pass

    def __set_format__(self, *args, **kwargs):
        """
        You probably don't want to use this function.

          typestr
            Must be 'double' or 'float'.
          fmt
            Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',
            and in addition can only be one of the latter two if it appears to
            match the underlying C reality.

        It exists mainly to be used in Python's test suite.

        Override the automatic determination of C-level floating point type.
        This affects how floats are converted to and from binary strings.
        """
        pass

    def __str__(self, *args, **kwargs):
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs):
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs):
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs):
        """ Return the Integral closest to x between 0 and x. """
        pass


class DyListMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs):
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs):
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, y):
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs):
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs):
        """ Implement self*=value. """
        pass

    def __init__(self, seq=()):
        """
        Built-in mutable sequence.

        If no argument is given, the constructor creates a new empty list.
        The argument must be an iterable if specified.
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs):
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs):
        """ Return self*value. """
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __reversed__(self, *args, **kwargs):
        """ Return a reverse iterator over the list. """
        pass

    def __rmul__(self, *args, **kwargs):
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs):
        """ Set self[key] to value. """
        pass

    def __sizeof__(self, *args, **kwargs):
        """ Return the size of the list in memory, in bytes. """
        pass


class DySetMagicMethods(DyObjectMagicMethods):

    def __and__(self, *args, **kwargs):
        """ Return self&value. """
        pass

    def __contains__(self, y):
        """ x.__contains__(y) <==> y in x. """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __iand__(self, *args, **kwargs):
        """ Return self&=value. """
        pass

    def __init__(self, seq=()):
        """
        set() -> new empty set object
        set(iterable) -> new set object

        Build an unordered collection of unique elements.
        # (copied from class doc)
        """
        pass

    def __ior__(self, *args, **kwargs):
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs):
        """ Return self-=value. """
        pass

    def __iter__(self, *args, **kwargs):
        """ Implement iter(self). """
        pass

    def __ixor__(self, *args, **kwargs):
        """ Return self^=value. """
        pass

    def __len__(self, *args, **kwargs):
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs):
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs):
        """ Return value&self. """
        pass

    def __reduce__(self, *args, **kwargs):
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs):
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs):
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs):
        """ Return value^self. """
        pass

    def __sizeof__(self):
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __sub__(self, *args, **kwargs):
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs):
        """ Return self^value. """
        pass


class DyStrMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs):
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs):
        """ Return a formatted version of the string as described by format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs):
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs):
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):
        """ Return hash(self). """
        pass

    def __init__(self, value="", encoding=None, errors="strict"):
        """
        str(object='') -> str
        str(bytes_or_buffer[, encoding[, errors]]) -> str

        Create a new string object from the given object. If encoding or
        errors is specified, then the object must expose a data buffer
        that will be decoded using the given encoding and error handler.
        Otherwise, returns the result of object.__str__() (if defined)
        or repr(object).
        encoding defaults to sys.getdefaultencoding().
        errors defaults to 'strict'.
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs):
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs):
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs):
        """ Return self*value. """
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs):
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs):
        """ Return value*self. """
        pass

    def __sizeof__(self, *args, **kwargs):
        """ Return the size of the string in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs):
        """ Return str(self). """
        pass


class DyTupleMagicMethods(DyObjectMagicMethods):

    def __add__(self, *args, **kwargs):
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs):
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs):
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs):
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs):
        pass

    def __ge__(self, *args, **kwargs):
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):
        """ Return hash(self). """
        pass

    def __init__(self, seq=()):
        """
        Built-in immutable sequence.

        If no argument is given, the constructor returns an empty tuple.
        If iterable is specified the tuple is initialized from iterable's items.

        If the argument is a tuple, the return value is the same object.
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs):
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs):
        """ Return self*value. """
        pass

    @staticmethod  # known case of __new__

    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs):
        """ Return value*self. """
        pass


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
