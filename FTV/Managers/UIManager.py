from abc import abstractmethod

from AppPackage.Experiments.Log import Log


class UIManager:
    def __init__(self):
        Log.i("initUIM: " + str(self.__class__.__name__))
        self.init()

    def init(self):
        pass

    @abstractmethod
    def setupUIVariables(self):
        pass

    def setupUITriggers(self):
        pass
