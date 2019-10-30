from FTV.Managers.VariableManager import VariableManager
from FTV.Triggers import Any


class VM(VariableManager):

    prints_manager = []
    next_id = 0
    FLAG = True

    gcode_file_fullname = "C:/Users/user/PycharmProjects/ftv/App/ExampleGcodes/AI3M_Beak_B_R_3.gcode"

    # def increase_next_id(self):
    #     self.next_id += 1
    #
    # def set_triggers(self):
    #     self.add_trigger(self.next_id, Any.Used, self.increase_next_id)
