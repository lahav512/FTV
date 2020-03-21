from AppPackage.Experiments.Log import Log


class DynamicVariable(object):
    def __init__(self, value=None):
        self.__value__: object = value

        self.__key__: str = None
        self.__links__ = []

    def set(self, value):
        self.__value__ = value

    def get(self):
        return self.__value__

    def __repr__(self):
        return str(self.get())

class DyBool(DynamicVariable):
    def __init__(self, value):
        super().__init__(value)
        self.value: bool

class DySwitch(DynamicVariable):
    def __init__(self):
        super().__init__(False)
        self.value: bool

    def set(self, value):
        if value:
            super(DySwitch, self).set(True)

        super(DySwitch, self).set(False)


if __name__ == '__main__':
    a = DySwitch()
    a.set(True)
