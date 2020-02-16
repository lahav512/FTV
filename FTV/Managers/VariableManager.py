import abc

from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Features import Module


class VariableManager(Module):
    POST_SETUP = False
    PRE_LOAD_FEATURES = False
    POST_LOAD_FEATURES = False
    START = False
    EXIT = False

    def __init__(self):
        self.init()
        self.__setupTriggers()
        super().__init__()
        Log.i("initVM: " + str(self.__class__.__name__))

    @classmethod
    def init(cls):
        pass

    def __setupTriggers(self):
        self.addTrigger(self.POST_SETUP, True, self.PRE_LOAD_FEATURES)
        self.addTrigger(self.POST_LOAD_FEATURES, True, self.START)
