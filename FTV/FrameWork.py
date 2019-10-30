from FTV.Managers.FeatureManager import FeatureManager as FM
from FTV.Managers.TriggerManager import TriggerManager as TM
from FTV.Managers.VariableManager import VariableManager as VM
from FTV.Managers.LogManager import LogManager as LM

from abc import abstractmethod


class FrameWork:
    fm: FM = None
    tm: TM = None
    vm: VM = None
    lm: LM = None

    def __init__(self):
        self.set_managers()
        self._set_triggers()
        self.vm.start_app()

    @abstractmethod
    def set_managers(self):
        pass

    def set_feature_manager(self, fm):
        self.fm = fm()

    def set_trigger_manager(self, tm):
        self.tm = tm()

    def set_variable_manager(self, vm):
        self.vm = vm()

    def set_log_manager(self, lm):
        self.lm = lm()

    def _set_triggers(self):
        self.vm.set_triggers()
