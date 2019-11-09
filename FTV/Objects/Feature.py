from FTV.Managers.VariableManager import VariableManager as VM
from FTV.Triggers.Trigger import GetterTrigger
import inspect

vm: VM = VM._vars


class Feature(object):
    def __init__(self):
        self._init_private_variables()
        self._init_variables()
        self.set_options()
        self.create_variables()

    def _init_private_variables(self):
        self._variables = []
        self._triggers_args = []

    def _init_variables(self):
        self._enabled = True

    def set_options(self):
        pass

    def set_triggers(self):
        pass

    def create_variables(self):
        pass

    def set_enabled(self):
        self._enabled = True

    def set_disabled(self):
        self._enabled = False

    def add_trigger(self, variable, trigger: GetterTrigger, method):
        self._triggers_args.append((self, trigger, method))

    def _get_variables(self):
        # Get method string
        method_str = inspect.getsource(self.set_triggers)
        trigger_lines = method_str.splitlines()[1:]

        for line in trigger_lines:
            if ".add_trigger(" not in line:
                continue

            variable_fullname = line.split(".add_trigger(")[1].split(",")[0].strip()

            if variable_fullname.startswith("self."):
                variable_name = variable_fullname.split(".", 2)[-1]
            else:
                variable_name = variable_fullname.split(".", 1)[-1]

            variable_name = variable_name.split(".", 1)[-1]

            self._variables.append(variable_name)
