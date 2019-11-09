from FTV.Managers.LogManager import LogManager as LM
from FTV.Managers.TriggerManager import TriggerManager as TM
from FTV.Triggers.Trigger import SetterTrigger
from abc import abstractmethod
import functools


class VariableParent:
    _forbidden = ("_hold", "_current_key", "_current_value")

    def __init__(self):
        self._hold = False
        self._current_key = None
        self._current_value = None

    # def __set__(self, instance, owner):
    #     return functools.partial(self.function, instance)

    def __setattr__(self, key, value):
        if key in self._forbidden:
            super().__setattr__(key, value)
            return
        if self._hold:
            self._current_key = key
            self._current_value = value
            super().__setattr__(key, value)
            return

        if self in TM.setter_links:
            if key in TM.setter_links[self]:
                old_var = getattr(self, key)
                super().__setattr__(key, value)
                link = TM.setter_links[self][key]
                link.trigger.set_args(old_var, value)
                if link.trigger():
                    # print("Change: " + str(key) + " = " + str(value))
                    link.method()

            else:
                super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    # def __getattribute__(self, item):
    #     var_id = id(super().__getattribute__(item))
    #     if var_id in TM.setter_links:
    #         link = TM.getter_links[var_id]
    #         if link.trigger():
    #             # print("Change: " + str(key) + " = " + str(value))
    #             link.method()

    # @abstractmethod
    # def set_triggers(self):
    #     pass

    # def add_trigger(self, variable, trigger: SetterTrigger, method):
    #     TM.add_trigger(self, variable, trigger, method)

    def print(self, message):
        LM.print(message)

    def hold(self):
        self._hold = True

    def release(self):
        self._hold = False
        self.__setattr__(self._current_key, self._current_value)


