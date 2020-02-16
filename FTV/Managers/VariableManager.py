import abc

from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Features import DynamicModule


class VariableManager(DynamicModule):
    def __init__(self):
        self.__setupVariables()
        self.setupVariables()
        self.init()
        self.__setupTriggers()
        super().__init__()
        Log.i("initVM: " + str(self.__class__.__name__))

    def __setupVariables(self):
        self.POST_SETUP = False
        self.PRE_LOAD_FEATURES = False
        self.POST_LOAD_FEATURES = False
        self.START = False
        self.EXIT = False

    def setupVariables(self):
        pass

    def init(self):
        pass

    def __setupTriggers(self):
        self.addTrigger(self.POST_SETUP, True, self.PRE_LOAD_FEATURES)
        self.addTrigger(self.POST_LOAD_FEATURES, True, self.START)
