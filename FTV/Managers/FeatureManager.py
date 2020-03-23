from abc import abstractmethod

from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Features import Feature
from FTV.Managers.AbstractManager import AbstractManager


class FeatureManager(AbstractManager):

    features = []

    def __init__(self):
        super().__init__()

    def add(self, *features: Feature):
        from FTV.FrameWork.Features import NIFeature

        for feature in features:
            temp_feature: NIFeature = feature()
            if temp_feature.settings.enabled:
                self.features.append(temp_feature)

    def setupSettings(self):
        pass
