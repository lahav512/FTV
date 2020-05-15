from FTV.Objects.SystemObjects.TriggerObjects import Condition


class DyObjectConditions:
    def __condition__(self, old_val, new_val, *args, **kwargs):
        return True

    class IsChanged(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return old_val != new_val

    class IsChangedTo(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            if new_val == args[0]:
                return old_val != new_val
            return False


class DyNumericConditions(DyObjectConditions):

    class IsIncreased(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return old_val < new_val

    class IsDecreased(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return old_val > new_val

    class IsEqualTo(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val == args[0]

    class IsNotEqualTo(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val != args[0]

    class IsGraterEqualTo(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val >= args[0]

    class IsLessEqualTo(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val <= args[0]

    class IsGraterThan(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val > args[0]

    class IsLessThan(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val < args[0]


class DyIteratorConditions(DyObjectConditions):

    class IsIncreased(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return old_val < new_val

    class IsDecreased(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return old_val > new_val

    class IsEqualTo(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val == args[0]

    class IsNotEqualTo(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val != args[0]


class DyIntConditions(DyNumericConditions):
    pass


class DyBoolConditions(DyObjectConditions):
    def __condition__(self, old_val, new_val, *args, **kwargs):
        return new_val


class DyByteArrayConditions(DyIteratorConditions):
    pass


class DyBytesConditions(DyNumericConditions):
    pass


class DyComplexConditions(DyNumericConditions):
    pass


class DyDictConditions(DyIteratorConditions):
    pass


class DyFloatConditions(DyNumericConditions):
    pass


class DyListConditions(DyIteratorConditions):
    pass


class DySetConditions(DyIteratorConditions):
    pass


class DyStrConditions(DyObjectConditions):
    pass


class DyTupleConditions(DyIteratorConditions):
    pass
