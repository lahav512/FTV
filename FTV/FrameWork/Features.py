import abc

from AppPackage.Experiments.Log import Log
from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.LogManager import LogManager
from FTV.Managers.TriggerManager import TriggerManager
from FTV.Managers.UIManager import UIManager


# global variableManager
# global featureManager
from FTV.Objects.Variables.DynamicVariable import DynamicVariable


class DynamicModule(object):
    __set_dynamic_variables = False
    __forbidden_dynamic_variables = (
        "_DynamicModule__set_dynamic_variables",
        "_DynamicModule__dynamic_variable_ids",
        "__dict__",
        "_DynamicModule__isForbiddenDynamicVariable",
        "_DynamicModule__isDynamicParent",
        "_DynamicModule__addDynamicVariable"
    )

    type = "DynamicModule"
    is_potential_parent = False

    __tm = TriggerManager()
    em = ExecutionManager()
    lm = LogManager()

    def __init__(self):
        self._init()

        self.__set_dynamic_variables = True
        self._setupVariables()
        self.__set_dynamic_variables = False

        self.init()

        self.__set_dynamic_variables = True
        self.setupVariables()
        self.__set_dynamic_variables = False

        self._setupTriggers()
        self.setupTriggers()

        # Log.d("__dynamic_variable_ids: " + str(self.__dynamic_variable_ids))

    def __setattr__(self, key, value):
        # if "settings" in key:
        #     print()

        if self.__isForbiddenDynamicVariable(key):
            super().__setattr__(key, value)
            return

        if self.__isDynamicVariable(key):
            Log.d("{}.set({})".format(key, value))
            super().__getattribute__(key).set(value)
            return

        if self.__isDynamicParent(value):
            if self.__set_dynamic_variables:
                Log.d("{}.setup({})".format(key, value.get()))
                super().__setattr__(key, value)
                self.__addDynamicVariable(key)
                return

        super().__setattr__(key, value)

    def __getattribute__(self, key):
        item: DynamicVariable = super().__getattribute__(key)
        if callable(item):
            return item

        if self.__isForbiddenDynamicVariable(key):
            return item

        if self.__isDynamicVariable(key):
            # Log.d("{}.get()".format(key))
            return item.get()

        return item

    def _init(self):
        self.__set_dynamic_variables = False
        self.__dynamic_variable_ids = {}

    def __addDynamicVariable(self, key):
        super().__getattribute__("_DynamicModule__dynamic_variable_ids")[key] = id(super().__getattribute__(key))
        # self.__dynamic_variable_ids.append(key)

    def __isDynamicVariable(self, key):
        if key in self.__dict__:
            if key in super().__getattribute__("_DynamicModule__dynamic_variable_ids"):
                return True
        return False

    @staticmethod
    def __isDynamicParent(value):
        if "DynamicVariable" in list(map(lambda _base: _base.__name__, value.__class__.__bases__)):
            return True
        return False

    def __isForbiddenDynamicVariable(self, key):
        if key in super().__getattribute__("_DynamicModule__forbidden_dynamic_variables"):
            return True
        return False

    def _setupVariables(self):
        pass

    def _setupTriggers(self):
        pass

    def init(self):
        pass

    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass

    def addTrigger(self, *args):
        pass

class ModuleFeature(DynamicModule):
    from FTV.Managers.VariableManager import VariableManager
    from FTV.Managers.FeatureManager import FeatureManager

    type = "ModuleFeature"
    is_potential_parent = True

    vm: VariableManager = None
    fm: FeatureManager = None

    def __init__(self):
        Log.i("initFeature: " + str(self.__class__.__name__))

        if self.__class__.vm is None:
            self.__class__.vm = self.__class__.VariableManager()
        if self.__class__.fm is None:
            self.__class__.fm = self.__class__.FeatureManager()

        self._DynamicModule__dynamic_variable_ids = {}

        self.settings = self.__class__._Settings()
        self.setupSettings()
        super().__init__()
        self.setupFeatures()

    def _setupTriggers(self):
        self.addTrigger(self.vm.PRE_LOAD_FEATURES, True, self.addFeatures)
        self.addTrigger(self.addFeatures, "finish", self.vm.POST_LOAD_FEATURES)

    def setupFeatures(self):
        pass

    def addFeatures(self, *features):
        self.fm.addFeatures(*features)

    def setupSettings(self):
        pass

    class _Settings:
        ui_platform = None

        def __init__(self):
            self.enabled = True

        def setEnabled(self):
            self.enabled = True

        def setDisabled(self):
            self.enabled = False

class UIFeature(ModuleFeature):
    type = "UIFeature"

    uim = UIManager()

    def __init__(self):
        super().__init__()
        self.settings: __class__._Settings
        self.setupUITriggers()
        self.startUIServices()
        self.vm.POST_SETUP = True  # TODO lahav Remove this line!

    def setupUITriggers(self):
        pass

    def setupContainers(self):
        pass

    def startUIServices(self):
        pass

    class _Settings(ModuleFeature._Settings):
        @classmethod
        def setUIPlatform(cls, ui_platform):
            cls.ui_platform = ui_platform
