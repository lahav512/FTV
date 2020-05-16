import abc
from threading import Thread

from AppPackage.Experiments.Log import Log
from FTV.Managers.AbstractManager import AbstractManager


class ExecutionManager(AbstractManager):
    def __init__(self):
        Log.p("initEM: " + str(self.__class__.__name__))
        super().__init__()
        self.threads = {}
        self.init()

    def init(self):
        pass

    def setupThreads(self):
        pass

    def addThread(self, name):
        self.threads[name] = Thread()

    def setupSettings(self):
        pass
