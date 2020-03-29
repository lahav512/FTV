from FTV.Objects.Variables.AbstractDynamicObject import DynamicObjectInterface


class DynamicMethodObject(DynamicObjectInterface):
    def __init__(self, action):
        super(DynamicMethodObject, self).__init__()
        self.action = action

    def __action__(self, *args, **kwargs):
        return self.action(*args, **kwargs)

