from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.Feature1 import Feature1
from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.Feature2 import Feature2
from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.Feature3 import Feature3
from FTV.FrameWork.Features import NIFeature
from FTV.Managers.FeatureManager import FeatureManager
from FTV.Managers.VariableManager import VariableManager


class FM(FeatureManager):
    def setupVariables(self):
        self.loading_progress.setBuiltin(False)

class VM(VariableManager):

    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass

class FeaturesLoader(NIFeature):
    def setupSettings(self):
        self.settings.setEnabled()

    def setupManagers(self):
        self.setVariableManager(VM)
        self.setFeatureManager(FM)

    def setupFeatures(self):
        self.addFeatures(
            Feature1,
            Feature2,
            Feature3
        )
