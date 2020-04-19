from queue import Queue
from threading import Thread as BaseThread


class Process(object):
    pass


class ProcessList(object):
    pass


class Thread(object):
    def __init__(self):
        self.thread = BaseThread()
        self.__active_triggers__ = Queue()

    def addTrigger(self, trigger):
        pass

    def runTrigger(self, trigger):
        pass

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
