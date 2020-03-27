from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DynamicObject, DynamicMethod


class DyBool(DynamicObject):
    def __init__(self, value):
        super().__init__(value)
        self.__value__: bool


class DySwitch(DynamicObject):
    def __init__(self):
        super().__init__(False)
        self.__value__: bool

    def set(self, value):
        if value:
            super(DySwitch, self).set(True)

        super(DySwitch, self)._set(False)

    def activate(self):
        self.set(True)


class DyInt(DynamicObject):
    def __init__(self, value=None):
        super().__init__(value)
        self.__value__: int
