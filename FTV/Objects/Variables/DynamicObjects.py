from FTV.Objects.Variables.AbstractDynamicObject import DynamicObject


class DyBool(DynamicObject):
    def __init__(self, value):
        super().__init__(value)
        self.value: bool

class DySwitch(DynamicObject):
    def __init__(self):
        super().__init__(False)
        self.value: bool

    def set(self, value):
        if value:
            super(DySwitch, self).set(True)

        super(DySwitch, self)._set(False)

    def activate(self):
        self.set(True)


if __name__ == '__main__':
    a = DySwitch()
    a.set(True)
