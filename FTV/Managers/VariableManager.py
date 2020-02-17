import abc

from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Features import DynamicModule
from FTV.Objects.Variables.DynamicVariable import DyBool


class VariableManager(DynamicModule):
    def __init__(self):
        super().__init__()
        Log.i("initVM: " + str(self.__class__.__name__))

    def _setupVariables(self):
        self.POST_SETUP = DyBool(False)
        self.PRE_LOAD_FEATURES = DyBool(False)
        self.POST_LOAD_FEATURES = DyBool(False)
        self.START = DyBool(False)
        self.EXIT = DyBool(False)

    def setupVariables(self):
        pass

    def init(self):
        pass

    def _setupTriggers(self):
        self.addTrigger(self.POST_SETUP, True, self.PRE_LOAD_FEATURES)
        self.addTrigger(self.POST_LOAD_FEATURES, True, self.START)
