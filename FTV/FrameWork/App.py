import abc

from FTV.FrameWork.Feature import Feature


class App(Feature):
    @abc.abstractmethod
    def loadFeatures(self):
        pass

    @abc.abstractmethod
    def setupSettings(self):
        pass

