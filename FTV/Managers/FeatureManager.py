from abc import abstractmethod

from AppPackage.Experiments.Log import Log


class FeatureManager:
    def __init__(self):
        self.features = []

    def addFeatures(self, *features):
        from FTV.FrameWork.Features import ModuleFeature

        for feature in features:
            temp_feature: ModuleFeature = feature()
            if temp_feature.settings.enabled:
                self.features.append(temp_feature)

