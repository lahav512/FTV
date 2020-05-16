from threading import Thread as BaseThread

from AppPackage.Experiments.PickleTests.DataObject import Queue


class Process(object):
    pass


class ProcessList(object):
    pass


class Thread(object):
    def __init__(self):
        self.thread = BaseThread()
        self.__active_triggers__ = Queue()

    def addTrigger(self, trigger):
        self.__active_triggers__.put_nowait(trigger)

    @staticmethod
    def runTrigger(trigger):
        trigger.runAction()

    def start(self):
        pass

    def stop(self):
        pass

    def sleep(self):
        pass

    def isAlive(self):
        pass


class ThreadList(object):
    pass
