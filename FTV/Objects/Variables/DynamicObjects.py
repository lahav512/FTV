from FTV.Objects.Variables.AbstractConditions import (DyIntConditions, DyBoolConditions, DyFloatConditions,
                                                      DyStrConditions, DyListConditions)


class DyObject(object):
    pass


class DyInt(DyIntConditions, DyObject):
    pass


class DyBool(DyBoolConditions, DyObject):
    pass


class DySwitch(DyObject):
    pass


class DyFloat(DyFloatConditions, DyObject):
    pass


class DyList(DyListConditions, DyObject):
    pass


class DyStr(DyStrConditions, DyObject):
    pass
