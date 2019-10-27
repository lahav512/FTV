from FTV.Managers.FeaturesManager import FeaturesManager


class FrameWork:
    def __init__(self):
        self.variables_manager = None
        self.triggers_manager = None
        self.features_manager = FeaturesManager()

    # def __setattr__(self, key, value):
    #     self._set_attr(key, value)
    #
    # @classmethod
    # def _set_attr(cls, key, value):
    #     setattr(cls, key, value)

    def set_variables_manager(self, variables_manager):
        self.variables_manager = variables_manager

    def set_features_manager(self, features_manager):
        self.features_manager = features_manager

    def set_triggers_manager(self, triggers_manager):
        self.triggers_manager = triggers_manager


class MainApp:
    def __init__(self):
        self.frame_work = FrameWork()
