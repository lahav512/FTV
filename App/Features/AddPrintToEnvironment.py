from FTV.Objects.Feature import Feature

from FTV.Managers.VariablesManager import VariablesManager as VM
from App.Objects.Print import Print


class AddPrintToEnvironment(Feature):
    def __init__(self):
        super().__init__()
        self.set_enabled()

        # Define Triggers

    @staticmethod
    def load_gcode_file(gcode_file_fullname: str, id_number: int):
        VM.prints_manager.add(Print(gcode_file_fullname, id_number))

    @staticmethod
    def clean_file(id_number: int):
        VM.prints_manager.get(id_number).gcode.clean()
