import inspect
from abc import abstractmethod

from FTV.Objects.SystemObjects.Trigger import Action, Trigger
from FTV.Objects.Variables.AbstractDynamicMethod import DynamicMethodObject


class DynamicModuleParent(object):
    type = "DynamicModuleParent"
    # _ACTIVE_METHOD = ""

    _BUILTIN_METHODS = {
        "_setupEnvironment",
        "_loadBuiltinSelf",
        "_loadSelf"
    }

    _IGNORE_METHODS = {
        "__setattr__",
        "__init__",
        "_setupBuiltinMethods",
        "_setupMethods",
        "_setupBuiltinTriggers",
        "setupTriggers",
        "_setupMethods",
        "addTrigger",
        "removeTrigger",
        "_DynamicModuleParent__initMethodsVariables",
        "_DynamicModuleParent__setupMethod",
        "_getDySwitchAction",  # TODO lahav Temporary!
        "_get",
        "_set",
        "get",
        "set",
        "_setupBuiltinVariables",
        "setupVariables",
    }

    # def __setattr__(self, key, value):
    #     if key in dir(self) and callable(getattr(self, key)):
    #         raise Exception(
    #             "Can't add the attribute \"{}\" to the object \"{}\", since it is already exists as a method.".format(
    #                 key, self.__class__.__name__))
    #
    #     super().__setattr__(key, value)

    def __init__(self, value=None):
        self._setupEnvironment()

    def __setupMethod(self, method_key):
        # print(method_key)
        self.__dynamic_methods__[method_key] = DynamicMethodObject()

    @abstractmethod
    def _setupEnvironment(self):
        pass

    @abstractmethod
    def _loadBuiltinSelf(self):
        pass

    @abstractmethod
    def _loadSelf(self):
        pass

    def _setupBuiltinMethods(self):
        # self.__dynamic_methods__ = set()
        self.__dynamic_methods__ = {}

        # map(lambda method_key: self.__setupMethod(method_key), getattr(self, "_DynamicModuleParent__BUILTIN_METHODS"))

        # [self.__setupMethod(method_key) for method_key in getattr(self, "_DynamicModuleParent__BUILTIN_METHODS")]

        for method_key in self._BUILTIN_METHODS:
            self.__setupMethod(method_key)

    def _setupMethods(self):
        ignore_methods = self._IGNORE_METHODS
        builtin_methods = self._BUILTIN_METHODS

        methods = inspect.getmembers(self, inspect.ismethod)
        # map(lambda func: self.__setupMethod(func[0]) if func[0] not in ignore_methods | builtin_methods else None, methods)

        filtered_methods = list(filter(lambda obj: obj[0] not in ignore_methods | builtin_methods, methods))

        for func in filtered_methods:
            self.__setupMethod(func[0])

    @abstractmethod
    def _setupBuiltinTriggers(self):
        pass

    @abstractmethod
    def setupTriggers(self):
        pass

    def addTrigger(self, dy_variable, condition, action, thread=None):

        # TODO lahav This solution is temporary.
        if callable(action):
            modified_action = Action(self, action, action.__name__)
        else:
            modified_action = Action(self, action.activate, action.__name__, action)

        if callable(dy_variable):
            modified_variable = self.__dynamic_methods__[dy_variable.__name__]
        else:
            modified_variable = dy_variable

        modified_variable.__triggers__.append(Trigger(self, condition, modified_action, thread))
        # TODO lahav Please choose a proper way to add triggers.

    def removeTrigger(self, *args):
        pass  # TODO lahav Must be redefined.

    # def _getDySwitchAction(self, action):
    #     return self.__temp_action.activate()
