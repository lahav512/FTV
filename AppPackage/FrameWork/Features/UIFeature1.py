from FTV.FrameWork.Features import UIFeature
from FTV.Managers.VariableManager import VariableManager
from FTV.Managers.UIManager import UIManager


class VM(VariableManager):
    pass

class UIM(UIManager):
    pass

class UIFeature1(UIFeature):

    @classmethod
    def _setupBuiltinManagers(cls):
        cls.vm = VM()
        cls.uim = UIM()

    def setupSettings(self):
        pass

    def setupTriggers(self):
        pass
        # self.addTrigger(self.fm.features, "Triger.List.len.Changed", "self.showPercentage")

