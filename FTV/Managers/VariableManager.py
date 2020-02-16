import abc

from FTV.FrameWork.Features import Module


class VariableManager(Module):
    APP_START = False

    def startApp(self):
        self.APP_START = True

    def stopApp(self):
        self.APP_START = False
