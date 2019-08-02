from FTV.Managers.FeaturesManager import FeaturesManager
# from FTV.Managers.VariablesManager import VariablesManager
from App.Variables.VM import VM as VariablesManager


class FrameWork:
    def __init__(self):
        self.features_manager = FeaturesManager()
        self.variables_manager = VariablesManager()

    def __setattr__(self, key, value):
        self._set_attr(key, value)

    @classmethod
    def _set_attr(cls, key, value):
        setattr(cls, key, value)
