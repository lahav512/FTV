from FTV.Managers.AbstractManager import AbstractManager


class FeatureManager(AbstractManager):
    __short_name__ = "FM"
    # features = []

    def __init__(self, _is_parent_app=None):
        super().__init__(_is_parent_app=_is_parent_app)
        self.init()

    def init(self):
        pass

    def _setupBuiltinVariables(self):
        super(FeatureManager, self)._setupBuiltinVariables()
        self.features = []

    def add(self, *features):
        from FTV.FrameWork.Features import Feature

        for feature in features:
            temp_feature: Feature = feature()
            if temp_feature.settings.enabled:
                self.features.append(temp_feature)

    def setupSettings(self):
        pass
