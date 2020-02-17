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

class DyBool(DynamicVariable):
    def __init__(self, value):
        super().__init__(value)
        self.value: bool


a = DyBool(True)
