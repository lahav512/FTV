from FTV.FrameWork.Features import NIFeature
from FTV.Managers.FeatureManager import FeatureManager


class FM(FeatureManager):
    def setupFeatures(self):
        from Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.Feature1 import Feature1
        from Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.Feature2 import Feature2
        from Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.Feature3 import Feature3

        self.addFeatures(
            Feature1,
            Feature2,
            Feature3
        )

    def setupVariables(self):
        self.loading_progress.setBuiltin(False)


class FeaturesLoader(NIFeature):
    def setupSettings(self):
        self.settings.setEnabled()

    def setupManagers(self):
        self.setFeatureManager(FM)
