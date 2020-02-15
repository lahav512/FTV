from AppPackage.FrameWork.Features.Feature1 import Feature1
from FTV.FrameWork.App import App
from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.LogManager import LogManager
from FTV.Managers.UIManager import UIManager
from FTV.Managers.VariableManager import VariableManager


class EM(ExecutionManager):
    pass

class VM(VariableManager):
    pass

class LM(LogManager):
    pass

class UIM(UIManager):
    pass

class MyApp(App):
    em = EM()
    vm = VM()
    lm = LM()
    uim = UIM()

    def setupSettings(self):
        self.settings.setUIPlatform(0)

    def loadFeatures(self):
        self.loadFeature(Feature1)


if __name__ == '__main__':
    MyApp()
