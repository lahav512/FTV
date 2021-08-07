from FTV.Objects.SystemObjects.TriggerObjects import Condition


class DyObjectConditions:
    pass


class DyNumericConditions(DyObjectConditions):
    pass


class DyIteratorConditions(DyObjectConditions):
    pass


class DyIntConditions(DyNumericConditions):
    pass


class DyBoolConditions(DyObjectConditions):
    pass


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
