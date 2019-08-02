from FTV.Managers.VariablesManager import VariablesManager

from App.Variables.PrintersManager import PrintersManager
from App.Variables.PrintsManager import PrintsManager


class VM(VariablesManager):
    printers_manager = PrintersManager()
    prints_manager = PrintsManager()
