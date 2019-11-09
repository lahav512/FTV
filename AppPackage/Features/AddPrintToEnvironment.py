from FTV.Objects.Feature import *

from FTV.Triggers import Any, Bool, Int

from AppPackage.Managers.LogManager import *
from AppPackage.Managers.VariableManager import VM
from AppPackage.Objects.Print import Print

vm: VM


class SetUp(Feature):
    def set_options(self):
        self.set_enabled()

    def create_variables(self):
        pass


class AddPrintToEnvironment(SetUp):
    def set_triggers(self):
        self.add_trigger(vm.APP_START, Bool.ChangedToTrue(), self.load_gcode_file)
        self.add_trigger(vm.next_id, Any.Changed(), self.clean_file)
        self.add_trigger(vm.current_round, Int.ChangedLessThan(vm.max_rounds), self.load_gcode_file)
        pass

    @logmethod
    def load_gcode_file(self):
        vm.prints_manager.add(Print(vm.gcode_file_fullname, vm.next_id))
        vm.last_id = vm.next_id
        vm.next_id += 1

    @logmethod
    def clean_file(self):
        vm.prints_manager.get(vm.last_id).gcode.clean()
        vm.current_round += 1


if __name__ == '__main__':
    AddPrintToEnvironment()
