from abc import abstractmethod

from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Features import DynamicModule


class FeatureManager(DynamicModule):
    features = []

    def __init__(self):
        super().__init__()

    def addFeatures(self, *features):
        from FTV.FrameWork.Features import NIFeature

        for feature in features:
            temp_feature: NIFeature = feature()
            if temp_feature.settings.enabled:
                self.features.append(temp_feature)

