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

class DyBoolConditions(DyObjectConditions):
    def __condition__(self, old_val, new_val, *args, **kwargs):
        return new_val

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

class DyIntConditions(DyNumericConditions):
    pass
