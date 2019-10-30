from FTV.Managers.TriggerManager import TriggerManager as TM
from FTV.Triggers.Trigger import GetterTrigger


class Feature:
    def __init__(self):
        self._init_variables()
        self.set_options()
        self.set_triggers()
        self.create_variables()

    def _init_variables(self):
        self.enabled: bool

    def set_options(self):
        pass

    def set_triggers(self):
        pass

    def create_variables(self):
        pass

    def set_enabled(self):
        self.enabled = True

    def set_disabled(self):
        self.enabled = False

    def add_trigger(self, variable, trigger: GetterTrigger, method):
        TM.add_trigger(self, variable, trigger, method)
