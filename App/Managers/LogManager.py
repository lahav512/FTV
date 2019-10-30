from FTV.Managers.LogManager import LogManager


class LM(LogManager):
    def set_options(self):
        self.set_debugging_mode(False)
