from FTV.Objects.Variables.AbstractDynamicObject import DyListMagicMethods, DyBoolMagicMethods, DyFloatMagicMethods
from FTV.Objects.Variables.DynamicModules import DyBuiltinModule


class DyObjectList(DyListMagicMethods, DyBuiltinModule):
    pass


class DyBoolList(DyBoolMagicMethods, DyObjectList):
    pass


class DySwitchList(DyBoolList):
    pass


class DyFloatList(DyFloatMagicMethods, DyObjectList):
    pass
