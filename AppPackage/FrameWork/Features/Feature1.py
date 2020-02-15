from AppPackage.FrameWork.App import MyApp
from FTV.FrameWork.Feature import Feature
from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.VariableManager import VariableManager
from FTV.Managers.LogManager import LogManager
from FTV.Managers.UIManager import UIManager


class EM(ExecutionManager):
    pass

class VM(VariableManager):
    pass

class LM(LogManager):
    pass

class UIM(UIManager):
    pass

class Feature1(Feature):
    em = EM()
    vm = VM()
    lm = LM()
    uim = UIM()

    def setupTriggers(self):
        self.settings.setUIPlatform(0)

    def setupParents(self):
        self.addParent(MyApp)
