from FTV.Objects.Variables.AbstractDynamicObject import DynamicObjectInterface


class DynamicMethodObject(DynamicObjectInterface):
    def __action__(self, *args, **kwargs):
        pass
        # return self.__call__(args, kwargs)

