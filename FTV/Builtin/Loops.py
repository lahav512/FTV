
class For:
    _stage_level = 0

    def __init__(self, func: function):
        self.func = func

    def __call__(self, *args, **kwargs):

        For._stage_level += 1
        self.func(self, *args, **kwargs)
        For._stage_level -= 1



