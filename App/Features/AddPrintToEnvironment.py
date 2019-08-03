from FTV.Objects.Feature import Feature

from App.Managers.VM import VM
from App.Objects.Print import Print

from App.Managers.TM import TM


class AddPrintToEnvironment(Feature):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.set_enabled()

        # Define Triggers
        # TM.DictFirstItemAdded(VM.prints_manager.prints)

    @staticmethod
    def load_gcode_file(gcode_file_fullname: str):
        VM.prints_manager.add(Print(gcode_file_fullname, VM.prints_manager.next_id))

    @staticmethod
    def clean_file(id_number: int):
        VM.prints_manager.get(id_number).gcode.clean()


if __name__ == '__main__':
    AddPrintToEnvironment()
