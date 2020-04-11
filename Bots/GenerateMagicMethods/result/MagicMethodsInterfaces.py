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

    def bit_length(self):
        """
        Number of bits necessary to represent self in binary.

        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs):
        """ Returns self, the complex conjugate of any int. """
        pass

    @classmethod  # known case

    def from_bytes(cls, *args, **kwargs):
        """
        Return the integer represented by the given array of bytes.

          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs):
        """
        Return an array of bytes representing an integer.

          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

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

    def clear(self):
        """ D.clear() -> None.  Remove all items from D. """
        pass

    def copy(self):
        """ D.copy() -> a shallow copy of D """
        pass

    @staticmethod  # known case

    def fromkeys(*args, **kwargs):
        """ Create a new dictionary with keys from iterable and values set to value. """
        pass

    def get(self, *args, **kwargs):
        """ Return the value for key if key is in the dictionary, else default. """
        pass

    def items(self):
        """ D.items() -> a set-like object providing a view on D's items """
        pass

    def keys(self):
        """ D.keys() -> a set-like object providing a view on D's keys """
        pass

    def pop(self, k, d=None):
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        pass

    def popitem(self):
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.
        """
        pass

    def setdefault(self, *args, **kwargs):
        """
        Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default.
        """
        pass

    def update(self, E=None, **F):
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass

    def values(self):
        """ D.values() -> an object providing a view on D's values """
        pass

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

    def as_integer_ratio(self):
        """
        Return integer ratio.

        Return a pair of integers, whose ratio is exactly equal to the original float
        and with a positive denominator.

        Raise OverflowError on infinities and a ValueError on NaNs.

        >>> (10.0).as_integer_ratio()
        (10, 1)
        >>> (0.0).as_integer_ratio()
        (0, 1)
        >>> (-.25).as_integer_ratio()
        (-1, 4)
        """
        pass

    def conjugate(self, *args, **kwargs):
        """ Return self, the complex conjugate of any float. """
        pass

    @staticmethod  # known case

    def fromhex(*args, **kwargs):
        """
        Create a floating-point number from a hexadecimal string.

        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -5e-324
        """
        pass

    def hex(self):
        """
        Return a hexadecimal representation of a floating-point number.

        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        """
        pass

    def is_integer(self, *args, **kwargs):
        """ Return True if the float is an integer. """
        pass

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

    def append(self, *args, **kwargs):
        """ Append object to the end of the list. """
        pass

    def clear(self, *args, **kwargs):
        """ Remove all items from list. """
        pass

    def copy(self, *args, **kwargs):
        """ Return a shallow copy of the list. """
        pass

    def count(self, *args, **kwargs):
        """ Return number of occurrences of value. """
        pass

    def extend(self, *args, **kwargs):
        """ Extend list by appending elements from the iterable. """
        pass

    def index(self, *args, **kwargs):
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        pass

    def insert(self, *args, **kwargs):
        """ Insert object before index. """
        pass

    def pop(self, *args, **kwargs):
        """
        Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range.
        """
        pass

    def remove(self, *args, **kwargs):
        """
        Remove first occurrence of value.

        Raises ValueError if the value is not present.
        """
        pass

    def reverse(self, *args, **kwargs):
        """ Reverse *IN PLACE*. """
        pass

    def sort(self, *args, **kwargs):
        """ Stable sort *IN PLACE*. """
        pass

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

    def add(self, *args, **kwargs):
        """
        Add an element to a set.

        This has no effect if the element is already present.
        """
        pass

    def clear(self, *args, **kwargs):
        """ Remove all elements from this set. """
        pass

    def copy(self, *args, **kwargs):
        """ Return a shallow copy of a set. """
        pass

    def difference(self, *args, **kwargs):
        """
        Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        pass

    def difference_update(self, *args, **kwargs):
        """ Remove all elements of another set from this set. """
        pass

    def discard(self, *args, **kwargs):
        """
        Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
        pass

    def intersection(self, *args, **kwargs):
        """
        Return the intersection of two sets as a new set.

        (i.e. all elements that are in both sets.)
        """
        pass

    def intersection_update(self, *args, **kwargs):
        """ Update a set with the intersection of itself and another. """
        pass

    def isdisjoint(self, *args, **kwargs):
        """ Return True if two sets have a null intersection. """
        pass

    def issubset(self, *args, **kwargs):
        """ Report whether another set contains this set. """
        pass

    def issuperset(self, *args, **kwargs):
        """ Report whether this set contains another set. """
        pass

    def pop(self, *args, **kwargs):
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        pass

    def remove(self, *args, **kwargs):
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        pass

    def symmetric_difference(self, *args, **kwargs):
        """
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

    def symmetric_difference_update(self, *args, **kwargs):
        """ Update a set with the symmetric difference of itself and another. """
        pass

    def union(self, *args, **kwargs):
        """
        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        pass

    def update(self, *args, **kwargs):
        """ Update a set with the union of itself and others. """
        pass

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

    def capitalize(self, *args, **kwargs):
        """
        Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower
        case.
        """
        pass

    def casefold(self, *args, **kwargs):
        """ Return a version of the string suitable for caseless comparisons. """
        pass

    def center(self, *args, **kwargs):
        """
        Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None):
        """
        S.count(sub[, start[, end]]) -> int

        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, *args, **kwargs):
        """
        Encode the string using the codec registered for encoding.

          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None):
        """
        S.endswith(suffix[, start[, end]]) -> bool

        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, *args, **kwargs):
        """
        Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None):
        """
        S.find(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs):
        """
        S.format(*args, **kwargs) -> str

        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        pass

    def format_map(self, mapping):
        """
        S.format_map(mapping) -> str

        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None):
        """
        S.index(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self, *args, **kwargs):
        """
        Return True if the string is an alpha-numeric string, False otherwise.

        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        pass

    def isalpha(self, *args, **kwargs):
        """
        Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        pass

    def isascii(self, *args, **kwargs):
        """
        Return True if all characters in the string are ASCII, False otherwise.

        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        pass

    def isdecimal(self, *args, **kwargs):
        """
        Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        pass

    def isdigit(self, *args, **kwargs):
        """
        Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        pass

    def isidentifier(self, *args, **kwargs):
        """
        Return True if the string is a valid Python identifier, False otherwise.

        Use keyword.iskeyword() to test for reserved identifiers such as "def" and
        "class".
        """
        pass

    def islower(self, *args, **kwargs):
        """
        Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        pass

    def isnumeric(self, *args, **kwargs):
        """
        Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        pass

    def isprintable(self, *args, **kwargs):
        """
        Return True if the string is printable, False otherwise.

        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        pass

    def isspace(self, *args, **kwargs):
        """
        Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        pass

    def istitle(self, *args, **kwargs):
        """
        Return True if the string is a title-cased string, False otherwise.

        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        pass

    def isupper(self, *args, **kwargs):
        """
        Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        pass

    def join(self, ab=None, pq=None, rs=None):
        """
        Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs):
        """
        Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        pass

    def lower(self, *args, **kwargs):
        """ Return a copy of the string converted to lowercase. """
        pass

    def lstrip(self, *args, **kwargs):
        """
        Return a copy of the string with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def maketrans(self, *args, **kwargs):
        """
        Return a translation table usable for str.translate().

        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, *args, **kwargs):
        """
        Partition the string into three parts using the given separator.

        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        pass

    def replace(self, *args, **kwargs):
        """
        Return a copy with all occurrences of substring old replaced by new.

          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None):
        """
        S.rfind(sub[, start[, end]]) -> int

        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None):
        """
        S.rindex(sub[, start[, end]]) -> int

        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, *args, **kwargs):
        """
        Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        pass

    def rpartition(self, *args, **kwargs):
        """
        Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        pass

    def rsplit(self, *args, **kwargs):
        """
        Return a list of the words in the string, using sep as the delimiter string.

          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.

        Splits are done starting at the end of the string and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs):
        """
        Return a copy of the string with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def split(self, *args, **kwargs):
        """
        Return a list of the words in the string, using sep as the delimiter string.

          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs):
        """
        Return a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None):
        """
        S.startswith(prefix[, start[, end]]) -> bool

        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, *args, **kwargs):
        """
        Return a copy of the string with leading and trailing whitespace remove.

        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def swapcase(self, *args, **kwargs):
        """ Convert uppercase characters to lowercase and lowercase characters to uppercase. """
        pass

    def title(self, *args, **kwargs):
        """
        Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        pass

    def translate(self, *args, **kwargs):
        """
        Replace each character in the string using the given translation table.

          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        pass

    def upper(self, *args, **kwargs):
        """ Return a copy of the string converted to uppercase. """
        pass

    def zfill(self, *args, **kwargs):
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.
        """
        pass

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

    def count(self, *args, **kwargs):
        """ Return number of occurrences of value. """
        pass

    def index(self, *args, **kwargs):
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        pass

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
