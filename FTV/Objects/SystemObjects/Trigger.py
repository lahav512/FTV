

class Trigger:
    def __init__(self, dy_module_parent, condition, action, thread=None):
        self.dy_module_parent = dy_module_parent
        self.condition = condition
        self.action = action
        self.thread = thread

