
class LogManager:
    _debugging_mode = False

    def __init__(self):
        self.set_options()

    def set_options(self):
        pass

    @staticmethod
    def set_debugging_mode(mode):
        LogManager._debugging_mode = mode

    @classmethod
    def print(cls, message=None):
        if cls._debugging_mode:
            if message is None:
                message = ""
            print(message)

    def start_app(self):
        self.print()

    def end_app(self):
        self.print()


class logmethod:
    _stage_level = 0

    def __init__(self, func):
        self.func = func
        self.name = self.func.__name__
        self._update_interval()

    def __call__(self, *args, **kwargs):
        self._update_interval()
        LogManager.print(self.interval + "-> " + self.name)

        logmethod._stage_level += 1
        self.func(self, *args, **kwargs)
        logmethod._stage_level -= 1

        self._update_interval()
        LogManager.print(self.interval + "<- " + self.name)

    def _update_interval(self):
        self.interval = "  " * logmethod._stage_level
