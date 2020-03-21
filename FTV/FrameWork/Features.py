import abc

from AppPackage.Experiments.Log import Log
from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.LogManager import LogManager
from FTV.Managers.TriggerManager import TriggerManager, addTriggerWrapper
from FTV.Managers.UIManager import UIManager


# global variableManager
# global featureManager
from FTV.Objects.Variables.DynamicVariable import DynamicVariable


class DynamicModule(object):
    def __init__(self):
        self.setupManagers()

    def _setupEnvironment(self):
        self._loadBuiltinSelf()
        self.POST_BUILTIN_LOAD = True

    def _loadBuiltinSelf(self):
        self._setupBuiltinVariables()
        self._setupBuiltinTriggers()

    def _loadSelf(self):
        pass

    def _loadUISelf(self):
        pass

    def _loadChildren(self):
        pass

    @classmethod
    def setupManagers(cls):
        pass

    def _setupBuiltinVariables(self):
        self.POST_BUILTIN_LOAD = False
        self.PRE_LOAD = False

        self.IS_SELF_LOADED = False

        self.POST_LOAD = False
        self.START = False
        self.EXIT = False

    def _setupBuiltinTriggers(self):
        self.addTrigger()

    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass

    def addTrigger(self, *args):
        pass
    
class NIFeature(DynamicModule):
    from FTV.Managers.VariableManager import VariableManager
    from FTV.Managers.FeatureManager import FeatureManager

    type = "NIFeature"

    vm: VariableManager = None
    fm: FeatureManager = None
    
    def __init__(self):
        super(NIFeature, self).__init__()
        self.setupSettings()

        # if self.settings.enabled:
        #    self._setupEnvironment() TODO lahav Don't forget to add the enabled flag
        self._setupEnvironment()

    def _setupBuiltinVariables(self):
        super(NIFeature, self)._setupBuiltinVariables()
        self.PRE_LOAD_FEATURES = False

        self.IS_CHILDREN_LOADED = False

        self.POST_LOAD_FEATURES = False

    @abc.abstractmethod
    def setupSettings(self):
        pass

    def addFeature(self):
        pass

class UIFeature(NIFeature):

    type = "UIFeature"

    uim = UIManager()

    def _setupBuiltinVariables(self):
        super(UIFeature, self)._setupBuiltinVariables()
        self.PRE_UI_LOAD = False

        self.IS_SELF_UI_LOADED = False

        self.POST_UI_LOAD = False

    def addUITrigger(self):
        pass
