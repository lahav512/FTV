from abc import abstractmethod


class Condition(object):
    @staticmethod
    @abstractmethod
    def __condition__(old_val, new_val, *args, **kwargs):
        return True


class Trigger:
    __slots__ = ("dy_module_parent",
                 "condition",
                 "condition_args",
                 "condition_kwargs",
                 "action",
                 "action_name",
                 "action_args",
                 "action_kwargs",
                 "thread")

    def __init__(self, dy_module_parent):
        self.dy_module_parent = dy_module_parent

        self.condition: function = None
        self.condition_args = []
        self.condition_kwargs = dict()

        self.action: function = None
        self.action_name = None
        self.action_args = []
        self.action_kwargs = dict()

        self.thread: object = None

    def setCondition(self, condition, *args, **kwargs):
        self.condition = condition.__condition__
        self.condition_args = args
        self.condition_kwargs = kwargs
        return self

    def setAction(self, action, *args, **kwargs):
        if callable(action):
            modified_action = self.dy_module_parent.__get_dy_method__(action)
            self.action_name = action.__name__
        else:
            modified_action = action

        self.action = modified_action.__action__
        self.action_args = args
        self.action_kwargs = kwargs
        return self

    def setThread(self, thread):
        self.thread = thread
        return self

    def runCondition(self, old_val, new_val):
        return self.__condition__(old_val, new_val, *self.condition_args, **self.condition_kwargs)

    def runAction(self):
        return self.__action__(*self.action_args, **self.action_kwargs)

    def __condition__(self, old_val, new_val, *args, **kwargs):
        return self.condition(old_val, new_val, *args, **kwargs)

    def __action__(self, *args, **kwargs):
        return self.action(*args, **kwargs)
