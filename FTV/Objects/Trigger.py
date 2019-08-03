import signal


class Trigger:
    _obj = None

    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print(key, value)
        super().__setattr__(key, value)

    @property
    def obj(self):
        return self._obj

    @obj.setter
    def obj(self, value):
        self._obj = value

    @classmethod
    def _set_attr(cls, key, value):
        setattr(cls, key, value)

    def filter(self):
        pass

