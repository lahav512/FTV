from FTV.Objects.Variables.AbstractDynamicObject import DynamicObject


class Trigger:
    def __init__(self, dy_module_parent, dy_variable: DynamicObject, condition, action, thread=None):
        self.dy_module_parent = dy_module_parent
        self.dy_variable = dy_variable
        self.condition = condition
        self.action = action
        self.thread = thread
