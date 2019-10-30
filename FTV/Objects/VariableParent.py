from FTV.Managers.LogManager import LogManager as LM
from FTV.Managers.TriggerManager import TriggerManager as TM
from FTV.Triggers.Trigger import SetterTrigger
from abc import abstractmethod


class VariableParent:
    _forbidden = ("_hold", "_current_key", "_current_value")

    def __init__(self):
        self._hold = False
        self._current_key = None
        self._current_value = None

    def __setattr__(self, key, value):
        if key in self._forbidden:
            super().__setattr__(key, value)
            return
        if self._hold:
            self._current_key = key
            self._current_value = value
            super().__setattr__(key, value)
            return
        if key in dir(self):
            old_var = getattr(self, key)
            old_var_id = id(old_var)
            super().__setattr__(key, value)
            new_var = getattr(self, key)
            new_var_id = id(new_var)
            if old_var_id in TM.setter_links:
                TM.rename_key(old_var_id, new_var_id)
                link = TM.setter_links[new_var_id]
                link.trigger.set_args(old_var, new_var)
                if link.trigger():
                    # print("Change: " + str(key) + " = " + str(value))
                    link.method()

        super().__setattr__(key, value)

    # def __getattribute__(self, item):
    #     var_id = id(super().__getattribute__(item))
    #     if var_id in TM.setter_links:
    #         link = TM.getter_links[var_id]
    #         if link.trigger():
    #             # print("Change: " + str(key) + " = " + str(value))
    #             link.method()

    # @abstractmethod
    def set_triggers(self):
        pass

    def add_trigger(self, variable, trigger: SetterTrigger, method):
        TM.add_trigger(self, variable, trigger, method)

    def print(self, message):
        LM.print(message)

    def hold(self):
        self._hold = True

    def release(self):
        self._hold = False
        self.__setattr__(self._current_key, self._current_value)


