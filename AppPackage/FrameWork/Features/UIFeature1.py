# from AppPackage.FrameWork.App import App
from FTV.FrameWork.Features import UIFeature
from FTV.Managers.VariableManager import VariableManager
from FTV.Managers.UIManager import UIManager


class VM(VariableManager):
    pass

class UIM(UIManager):
    pass

class UIFeature1(UIFeature):
    vm = VM()
    uim = UIM()

    def setupSettings(self):
        pass
