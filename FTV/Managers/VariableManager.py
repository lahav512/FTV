from FTV.Objects.VariableParent import VariableParent as VP
from abc import abstractmethod


class _Variables(VP):
    def __setattr__(self, key, value):
        super(_Variables, self).__setattr__(key, value)
        print(key, value)


class VariableManager:

    _vars = VP()

    def __init__(self):
        super(VariableManager, self).__init__()
        self._init_private_variables()
        self.create_variables()

    def __setattr__(self, key, value):
        setattr(self._vars, key, value)

    def _init_private_variables(self):
        self.APP_START = False

    def create_variables(self):
        pass

    @abstractmethod
    def set_triggers(self):
        pass

    def start_app(self):
        self.APP_START = True

    def stop_app(self):
        self.APP_START = False
