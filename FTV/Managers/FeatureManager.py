from FTV.Objects.Feature import Feature
from abc import abstractmethod


class FeatureManager:
    def __init__(self):
        self.features = []
        self.set_features()
        # self._init_features()

    @abstractmethod
    def set_features(self):
        pass

    def add_features(self, *features):
        for feature in features:
            temp_feature: Feature = feature()
            if temp_feature._enabled:
                self.features.append(feature())

    def _init_features(self):
        for feature in self.features:
            feature()
