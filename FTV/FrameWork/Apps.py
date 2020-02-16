import abc

from FTV.FrameWork.Features import ModuleFeature, UIFeature


class ModuleApp(ModuleFeature):
    @abc.abstractmethod
    def setupFeatures(self):
        pass

    @abc.abstractmethod
    def setupSettings(self):
        pass

class UIApp(UIFeature):
    @abc.abstractmethod
    def setupFeatures(self):
        pass

    @abc.abstractmethod
    def setupSettings(self):
        pass

