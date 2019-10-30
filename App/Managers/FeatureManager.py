from FTV.Managers.FeatureManager import FeatureManager

from App.Features.AddPrintToEnvironment import AddPrintToEnvironment


class FM(FeatureManager):
    def set_features(self):
        self.add_features(
            AddPrintToEnvironment
        )
