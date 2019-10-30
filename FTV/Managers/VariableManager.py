from FTV.Objects.VariableParent import VariableParent as VP
from abc import abstractmethod


class VariableManager(VP):
    APP_START = False

    @abstractmethod
    def set_triggers(self):
        pass

    def start_app(self):
        self.APP_START = True

    def stop_app(self):
        self.APP_START = False
