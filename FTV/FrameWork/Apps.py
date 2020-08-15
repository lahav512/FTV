from FTV.FrameWork.Features import NIFeature, UIFeature, Feature
from FTV.Objects.Variables.DynamicObjects import DySwitch


class __AbstractApp:
    type = "App"

    @classmethod
    def startApp(cls):
        cls.vm.START.activate()

    @classmethod
    def stopApp(cls):
        cls.vm.EXIT.activate()


class NIApp(__AbstractApp, NIFeature):
    def __init__(self):
        super(NIApp, self).__init__()
        super(Feature, self).__init__()

    """This method is deprecated. Please use the method "setupFeatures" in the FeatureManager instead."""
    # @abstractmethod
    def setupFeatures(self):
        pass

    """This method is deprecated. Please use the method "setupSettings" in the FeatureManager instead."""
    # @abstractmethod
    def setupSettings(self):
        pass

    def _setupBuiltinVariables(self):
        super(NIApp, self)._setupBuiltinVariables()
        self.vm.START = DySwitch()
        self.vm.EXIT = DySwitch()

    def _setupBuiltinTriggers(self):
        super(NIApp, self)._setupBuiltinTriggers()
        self.addTrigger(self.vm.POST_BUILTIN_LOAD).setAction(self._resumeSetupEnvironment)

        self.overrideTriggers(self._setupEnvironment).setAction(self.vm.POST_BUILTIN_LOAD).setThread(self.em.Main)
        self.addTrigger(self.vm.POST_LOAD_FEATURES).setAction(self.vm.START)


class UIApp(__AbstractApp, UIFeature):
    """This method is deprecated. Please use the method "setupFeatures" in the FeatureManager instead."""
    # @abstractmethod
    def setupFeatures(self):
        pass

    """This method is deprecated. Please use the method "setupSettings" in the FeatureManager instead."""
    # @abstractmethod
    def setupSettings(self):
        pass



