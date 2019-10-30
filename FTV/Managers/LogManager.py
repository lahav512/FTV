class LogManager:
    _debugging_mode = False

    def __init__(self):
        self.set_options()

    def set_options(self):
        pass

    @classmethod
    def set_debugging_mode(cls, mode):
        cls._debugging_mode = mode

    @classmethod
    def print(cls, message):
        if cls._debugging_mode:
            print(message)

