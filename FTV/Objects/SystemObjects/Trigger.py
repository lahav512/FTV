class Condition(object):
    def __condition__(self, *args, **kwargs):
        return True


class Trigger:
    __slots__ = ("dy_module_parent",
                 "condition",
                 "condition_args",
                 "condition_kwargs",
                 "action",
                 "action_args",
                 "action_kwargs",
                 "thread")

    def __init__(self, dy_module_parent):
        self.dy_module_parent = dy_module_parent

        self.condition = None
        self.condition_args = []
        self.condition_kwargs = dict()

        self.action: function = None
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
        else:
            modified_action = action

        self.action = modified_action.__action__
        self.action_args = args
        self.action_kwargs = kwargs
        return self

    def setThread(self, thread):
        self.thread = thread
        return self

    def runCondition(self):
        return self.__condition__(self.condition_args, self.condition_kwargs)

    def runAction(self):
        return self.__action__(self.action_args, self.action_kwargs)

    def __condition__(self, *args, **kwargs):
        return self.condition(args, kwargs)

    def __action__(self, *args, **kwargs):
        return self.action()
