import time

from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Features import NIFeature
from FTV.Objects.Variables.DynamicMethods import DyMethod


class AbstractFeature(NIFeature):
    def setupSettings(self):
        pass

    def setupManagers(self):
        pass

    def setupTriggers(self):
        self.addTrigger(self.vm.POST_LOAD_FEATURES).setAction(self.printLoaded)

    def setupFeatures(self):
        time.sleep(1)

    @DyMethod()
    def printLoaded(self):
        Log.p(f"\"{self.__name__}\" has been loaded.")
