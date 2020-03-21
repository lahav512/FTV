from abc import abstractmethod

from FTV.FrameWork.Features import NIFeature, UIFeature


class __AbstractApp:
    @classmethod
    def startApp(cls):
        cls.START = True

    @classmethod
    def stopApp(cls):
        cls.EXIT = True


class NIApp(__AbstractApp, NIFeature):
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



