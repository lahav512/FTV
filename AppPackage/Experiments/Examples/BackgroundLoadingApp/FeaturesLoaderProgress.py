from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Features import NIFeature
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicObjects import DyFloat


class VM(VariableManager):

    def setupVariables(self):
        self.progress = DyFloat(0)

    def setupTriggers(self):
        pass

class FeaturesLoaderProgress(NIFeature):
    def setupSettings(self):
        self.settings.setEnabled()

    def setupManagers(self):
        self.setVariableManager(VM)

    def setupFeatures(self):
        pass

    def setupTriggers(self):
        self.addTrigger(self.vm.progress).setAction(self.printProgress)

    @DyMethod()
    def updateProgress(self):
        self.progress += 100/3

    @DyMethod()
    def printProgress(self):
        Log.p(f"{self.progress}%")
