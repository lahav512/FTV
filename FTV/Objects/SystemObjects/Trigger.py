

class Action(object):
    __slots__ = ("func", "__name__")

    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)


class Condition(object):
    __slots__ = ()

    def __call__(self, *args, **kwargs):
        self.run()

    def run(self):
        pass


class Trigger:
    __slots__ = ("dy_module_parent", "condition", "action", "thread")

    def __init__(self, dy_module_parent, condition, action, thread=None):
        self.dy_module_parent = dy_module_parent
        self.condition = condition
        self.action: function = action
        self.thread = thread

    def runAction(self):
        pass