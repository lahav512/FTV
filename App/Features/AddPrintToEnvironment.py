from FTV.Objects.Feature import Feature

from FTV.Triggers import Any, Bool

from App.Managers.LogManager import LM
from App.Managers.VariableManager import VM
from App.Objects.Print import Print


class AddPrintToEnvironment(Feature):
    def set_options(self):
        pass

    def set_triggers(self):
        self.add_trigger(VM.APP_START, Bool.ChangedToTrue, self.load_gcode_file)
        self.add_trigger(VM.next_id, Any.Changed, self.clean_file)

    def create_variables(self):
        pass

    @staticmethod
    def load_gcode_file():
        LM.print("start - load_gcode_file")
        VM.prints_manager.append(Print(VM.gcode_file_fullname, VM.next_id))
        VM.next_id = VM.next_id + 1
        LM.print("end - load_gcode_file")

    @staticmethod
    def clean_file():
        VM.prints_manager.get(VM.next_id).gcode.clean()


if __name__ == '__main__':
    AddPrintToEnvironment()
