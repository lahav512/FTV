from abc import abstractmethod

from AppPackage.Experiments.Log import Log
from FTV.Managers.AbstractManager import AbstractManager


class VariableManager(AbstractManager):
    def __init__(self):
        Log.p("initVM: " + str(self.__class__.__name__))
        super().__init__()
        self.init()

    def init(self):
        pass

    @abstractmethod
    def setupVariables(self):
        pass

    @abstractmethod
    def setupTriggers(self):
        pass
