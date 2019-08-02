from App.Variables.PrintersManager import PrintersManager
from App.Variables.PrintsManager import PrintsManager


class VariablesManager:

    printers_manager = PrintersManager()
    prints_manager = PrintsManager()

    def __init__(self):
        pass

    @classmethod
    def add(cls, key, value):
        cls.__setattr__(key, value)
