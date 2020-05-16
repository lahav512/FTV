import abc

from AppPackage.Experiments.Log import Log
from FTV.Managers.AbstractManager import AbstractManager
from FTV.Objects.SystemObjects.Executions import DyThread


class ExecutionManager(AbstractManager):
    def __init__(self):
        Log.p("initEM: " + str(self.__class__.__name__))
        super().__init__()
        self.init()

    def init(self):
        pass

    def _setupBuiltinVariables(self):
        super(ExecutionManager, self)._setupBuiltinVariables()
        self._setupBuiltinThreads()

    def _setupBuiltinThreads(self):
        self.threads = {}
        self.addThread("Main")

    def setupVariables(self):
        self.setupThreads()

    def setupThreads(self):
        pass

    def addThread(self, name):
        self.threads[name] = DyThread(name=name)

    def setupSettings(self):
        pass
