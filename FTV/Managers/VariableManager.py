import abc


class VariableManager:
    APP_START = False

    def __init__(self):
        pass

    def setTriggers(self):
        pass

    def startApp(self):
        self.APP_START = True

    def stopApp(self):
        self.APP_START = False
