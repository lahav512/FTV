from abc import abstractmethod

from AppPackage.Experiments.Log import Log

class VariableManager:
    def __init__(self):
        Log.i("initVM: " + str(self.__class__.__name__))
        self.init()

    def init(self):
        pass

    @abstractmethod
    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass
