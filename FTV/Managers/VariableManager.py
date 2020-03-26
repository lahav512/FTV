from abc import abstractmethod

from AppPackage.Experiments.Log import Log
from FTV.Managers.AbstractManager import AbstractManager


class VariableManager(AbstractManager):
    def __init__(self):
        super().__init__()
        Log.p("initVM: " + str(self.__class__.__name__))
        self.init()

    def init(self):
        pass
