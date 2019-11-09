from FTV.Managers.FeatureManager import FeatureManager as FM
from FTV.Managers.TriggerManager import TriggerManager as TM
from FTV.Managers.VariableManager import VariableManager as VM
from FTV.Managers.LogManager import LogManager as LM

from FTV.Objects.Feature import Feature

from abc import abstractmethod


class ApplicationManager:
    fm: FM = None
    tm: TM = None
    vm: VM = None
    lm: LM = None

    def __init__(self):
        self.set_managers()
        self._set_triggers()
        self.lm.start_app()
        self.vm.start_app()
        self.lm.end_app()

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
        for feature in self.fm.features:
            feature: Feature = feature
            feature.set_triggers()
            feature._get_variables()
            for k in range(len(feature._triggers_args)):
                if ("." in feature._variables[k]):
                    variable_parent = getattr(self.vm, feature._variables[k].rsplit(".", 1)[0])
                else:
                    variable_parent = self.vm._vars

                self.tm.add_trigger(
                    variable_parent,
                    feature._variables[k].rsplit(".", 1)[-1],
                    *feature._triggers_args[k]
                )
