from threading import current_thread

from FTV.Objects.Variables.AbstractConditions import DyObjectConditions


class DynamicObjectInterface(object):
    pass


class DyObjectMagicMethods(object):
    pass


class DyBoolMagicMethods(DyObjectMagicMethods):
    pass


class DyNumericMagicMethods(DyObjectMagicMethods):
    pass


class DyIntMagicMethods(DyNumericMagicMethods):
    pass


class DyFloatMagicMethods(DyNumericMagicMethods):
    pass


class DyListMagicMethods(DyObjectMagicMethods):
    pass


class DyObject(DyObjectMagicMethods, DyObjectConditions, DynamicObjectInterface):
    pass
