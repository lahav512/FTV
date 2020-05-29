from FTV.Managers.AbstractManager import AbstractManager
from FTV.Objects.SystemObjects.Executions import DyThread
from FTV.Objects.Variables.DynamicIterators import DyBoolList
from FTV.Objects.Variables.DynamicMethods import DyBuiltinMethod


class ExecutionManager(AbstractManager):
    __short_name__ = "EM"

    def __init__(self, _is_parent_app=False):
        super().__init__(_is_parent_app=_is_parent_app)
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

    def _setupBuiltinTriggers(self):
        super(ExecutionManager, self)._setupBuiltinTriggers()
        self.addTrigger(self.areQueuesEmpty)\
            .setCondition(DyBoolList.IsChangedTo, True)\
            .setAction(self._stopAllThreads)\
            # .setThread(self.getThread("Main"))

    def _setupBuiltinThreads(self):
        self.areQueuesEmpty = DyBoolList(builtin=True)

        self.threads = {}

        if self._is_parent_app:
            self.addThread("Main")

    def setupVariables(self):
        pass

    def setupThreads(self):
        pass

    def addThread(self, name, daemon=False):
        # if self._is_parent_app:
        if name not in self.threads:
            self.threads[name] = DyThread(name=name, daemon=daemon)
            self.areQueuesEmpty.add(self.threads[name].isQueueEmpty)
            # self.threads[name].start()

    def getThread(self, name):
        return self.threads[name]

    def setupSettings(self):
        pass

    @DyBuiltinMethod()
    def _stopAllThreads(self):
        for thread in self.threads.values():
            if not thread.daemon:
                thread.stop()
