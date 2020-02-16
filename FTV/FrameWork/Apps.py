from abc import ABC, abstractmethod

from FTV.FrameWork.Features import ModuleFeature, UIFeature


class __AbstractApp:
    @classmethod
    def startApp(cls):
        cls.START = True

    @classmethod
    def stopApp(cls):
        cls.EXIT = True


class ModuleApp(__AbstractApp, ModuleFeature):
    @abstractmethod
    def setupFeatures(self):
        pass

    @abstractmethod
    def setupSettings(self):
        pass

class UIApp(__AbstractApp, UIFeature):
    @abstractmethod
    def setupFeatures(self):
        pass

    @abstractmethod
    def setupSettings(self):
        pass



