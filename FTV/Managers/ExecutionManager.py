import abc

from AppPackage.Experiments.Log import Log
from FTV.Managers.AbstractManager import AbstractManager
from FTV.Objects.SystemObjects.Executions import DyThread
from FTV.Objects.Variables.DynamicIterators import DyBoolList
from FTV.Objects.Variables.DynamicMethods import DyMethod, DyBuiltinMethod


class ExecutionManager(AbstractManager):
    def __init__(self):
        Log.p("initEM: " + str(self.__class__.__name__))
        super().__init__()
        self.init()

    def init(self):
        pass

    @DyBuiltinMethod()
    def _loadBuiltinSelf(self):
        self._setupBuiltinVariables()
        self._setupBuiltinThreads()
        self._setupBuiltinMethods()
        self._setupBuiltinTriggers()

    @DyBuiltinMethod()
    def _loadSelf(self):
        self.setupVariables()
        self.setupThreads()
        self._setupMethods()
        self.setupTriggers()

    def _setupBuiltinMethods(self):
        self._BUILTIN_METHODS |= {"_stopAllThreads"}
        super(ExecutionManager, self)._setupBuiltinMethods()

    def _setupBuiltinVariables(self):
        super(ExecutionManager, self)._setupBuiltinVariables()

    def _setupBuiltinTriggers(self):
        super(ExecutionManager, self)._setupBuiltinTriggers()
        self.addTrigger(self.areQueuesEmpty).setCondition(DyBoolList.IsChangedTo, True).setAction(self._stopAllThreads)

    def _setupBuiltinThreads(self):
        self.areQueuesEmpty = DyBoolList(builtin=True)

        self.threads = {}
        self.addThread("Main")

    def setupVariables(self):
        pass

    def setupThreads(self):
        pass

    def addThread(self, name, daemon=False):
        if name not in self.threads:
            self.threads[name] = DyThread(name=name, daemon=daemon)
            self.areQueuesEmpty.add(self.threads[name].isQueueEmpty)

    def getThread(self, name):
        return self.threads[name]

    def setupSettings(self):
        pass

    @DyBuiltinMethod()
    def _stopAllThreads(self):
        for thread in self.threads.values():
            if not thread.daemon:
                thread.stop()
