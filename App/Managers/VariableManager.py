from FTV.Managers.VariableManager import VariableManager
from App.Variables.PrintsManager import PrintsManager


class VM(VariableManager):
    def create_variables(self):
        self.prints_manager = PrintsManager()
        self.last_id = None
        self.next_id = 0

        self.gcode_file_fullname = "C:/Users/user/PycharmProjects/ftv/App/ExampleGcodes/AI3M_Beak_B_R_3.gcode"

