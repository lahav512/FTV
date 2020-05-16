from threading import Thread as BaseThread, current_thread

from AppPackage.Experiments.Log import Log
from AppPackage.Experiments.PickleTests.DataObject import Queue
from FTV.Objects.Variables.DynamicModules import DyModule


class DyProcess(object):
    pass


class DyProcessList(object):
    pass


class DyThread(DyModule):
    def __init__(self, name=None, daemon=False):
        self.name = name
        self.daemon = daemon
        super(DyThread, self).__init__()

    def setupVariables(self):
        self.__active_triggers__ = Queue()
        self.thread = BaseThread(target=self.thread_loop, daemon=self.daemon)

        if self.name is not None:
            self.thread.setName(self.name)

        self.is_new = True

    def thread_loop(self):
        self.is_new = False
        while True:
            if not self.__active_triggers__.empty():
                trigger = self.__active_triggers__.get_nowait()

                if trigger is None:
                    break

                self.runActiveTrigger(trigger)
            else:
                pass
                # self.thread.setDaemon(True)

    def addActiveTrigger(self, trigger):
        self.__active_triggers__.put_nowait(trigger)

        if self.is_new:
            self.start()

    # @staticmethod
    def runActiveTrigger(self, trigger):
        # Log.p(f"threadName: {self.name}")
        Log.p(f"threadName: {current_thread().name}")
        trigger.runAction()

    def start(self):
        self.thread.start()

    def stop(self):
        self.addActiveTrigger(None)

    def sleep(self):
        pass

    def join(self):
        self.thread.join()

    def isAlive(self):
        return self.thread.isAlive


class DyThreadList(object):
    pass
