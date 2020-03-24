import inspect
import time
from abc import abstractmethod
from functools import wraps, partial
from queue import Queue

import wrapt as wrapt
from past.builtins import xrange

from AppPackage.Experiments.Log import Log
from FTV.Objects.SystemObjects.Trigger import Action, Trigger
from AppPackage.Experiments import Efficiency

class DynamicMethod:
    def __init__(self):
        super(DynamicMethod, self).__init__()

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        Log.i("-> " + wrapped.__name__)
        ans = wrapped(*args, **kwargs)
        Log.i("<- " + wrapped.__name__)
        DynamicModule._distributeTriggers(wrapped)
        DynamicModule._runActiveTriggers(wrapped)
        return ans


class DynamicObject(object):
    type = "DynamicObject"

    def __init__(self, value=None):
        super(DynamicObject, self).__init__()
        self.__value__: object = value
        self.__name__: str
        self.__triggers__ = []
        self.__active_triggers__ = Queue()

    def _set(self, value):
        self.__value__ = value

    def set(self, value):
        self._set(value)
        Log.i("Activated: " + self.__name__)
        DynamicModule._distributeTriggers(self)
        DynamicModule._runActiveTriggers(self)

    def _get(self):
        return self.__value__

    def get(self):
        return self._get()

    # def __repr__(self):
    #     return self.get()


class DynamicModuleParent(object):
    type = "DynamicModuleParent"

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

    def __setattr__(self, key, value):
        if key in dir(self) and callable(getattr(self, key)):
            raise Exception(
                "Can't add the attribute \"{}\" to the object \"{}\", since it is already exists as a method.".format(
                    key, self.__class__.__name__))

        super().__setattr__(key, value)

    def __init__(self):
        self._setupEnvironment()

    def __setupMethod(self, method_key):
        # print(method_key)
        method = getattr(self.__class__, method_key)
        setattr(method, "__triggers__", [])
        setattr(method, "__active_triggers__", Queue())

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
        self.__dynamic_methods__ = set()

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

        modified_action: function

        # TODO lahav This solution is temporary.
        if callable(action):
            modified_action = Action(getattr(self, action.__name__))
        else:
            modified_action = Action(action.activate)

        dy_variable.__triggers__.append(Trigger(self, condition, modified_action, thread))
        # TODO lahav Please choose a proper way to add triggers.

    def removeTrigger(self, *args):
        pass  # TODO lahav Must be redefined.

    # def _getDySwitchAction(self, action):
    #     return self.__temp_action.activate()


class DynamicModule(DynamicModuleParent, DynamicObject):
    type = "DynamicModule"

    @DynamicMethod()
    def _setupEnvironment(self):
        self._loadBuiltinSelf()

    @DynamicMethod()
    def _loadBuiltinSelf(self):
        self._setupBuiltinVariables()
        self._setupBuiltinMethods()
        self._setupBuiltinTriggers()

    @DynamicMethod()
    def _loadSelf(self):
        self.setupVariables()
        self._setupMethods()
        self.setupTriggers()

    def _setupBuiltinTriggers(self):
        self.addTrigger(self._loadBuiltinSelf, True, self.POST_BUILTIN_INIT)  # TODO lahav use this line: , "thread.main")
        self.addTrigger(self.POST_BUILTIN_INIT, True, self.PRE_INIT)
        self.addTrigger(self.PRE_INIT, True, self._loadSelf)
        self.addTrigger(self._setupEnvironment, True, self.POST_INIT)

    def _setupBuiltinVariables(self):

        self.POST_BUILTIN_INIT = DySwitch()
        self.PRE_INIT = DySwitch()
        self.POST_INIT = DySwitch()

    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass

    @staticmethod
    def _distributeTriggers(dy_object: DynamicObject):
        for trigger in dy_object.__triggers__:
            if trigger.thread is None:
                dy_object.__active_triggers__.put_nowait(trigger)
            else:
                # TODO lahav Add trigger to its designated thread
                pass

    @staticmethod
    def _runActiveTriggers(dy_object: DynamicObject):
        while not dy_object.__active_triggers__.empty():
            dy_object.__active_triggers__.get_nowait().action()

    def __setattr__(self, key, value):
        # try:
        #     getattr(self, key)
        #     is_new_var = False
        # except:
        #     is_new_var = True

        is_new_var = key not in locals()
        # is_new_var = True

        super(DynamicModule, self).__setattr__(key, value)
        object = getattr(self, key)
        try:
            if object.type == DynamicObject.type:
                if not is_new_var:
                    Log.i("Activated: " + key)
                    DynamicModule._distributeTriggers(object)
                    DynamicModule._runActiveTriggers(object)
                else:
                    object.__name__ = key
        except:
            pass


    # def __getattribute__(self, item):
    #     return super(DynamicModule, self).__getattribute__(item)


if __name__ == '__main__':
    from FTV.Objects.Variables.DynamicObject import DySwitch

    class DyModule(DynamicModule):

        @staticmethod
        def print(message):
            Log.i(message)

        @DynamicMethod()
        def ftvWorks(self):
            self.print("FTV Works!")

        @DynamicMethod()
        def firstMethod(self):
            # self.print("firstMethod")
            self.first.activate()

        @DynamicMethod()
        def secondMethod(self):
            # self.print("secondMethod")
            self.second.activate()

        @DynamicMethod()
        def thirdMethod(self):
            # self.print("thirdMethod")
            self.third.activate()

        def setupVariables(self):
            self.first = DySwitch()
            self.second = DySwitch()
            self.third = DySwitch()

        def setupTriggers(self):
            self.addTrigger(self.POST_INIT, True, self.firstMethod)
            self.addTrigger(self.firstMethod, True, self.secondMethod)
            # self.addTrigger(self.second, True, self.thirdMethod)
            # self.addTrigger(self.third, True, self.ftvWorks)

    class SimpleDyModule(DynamicModule):
        def __init__(self):
            super(SimpleDyModule, self).__init__()
            self.first = DySwitch()
            self.second = DySwitch()
            self.third = DySwitch()

            self.firstMethod()
            if self.first.get():
                self.secondMethod()
                if self.second.get():
                    self.thirdMethod()
                    if self.third.get():
                        self.ftvWorks()

        # def _setupBuiltinMethods(self):
        #     super(SimpleDyModule, self)._setupBuiltinMethods()
        #     self.__dynamic_methods__.add("firstMethod")
        #     self.__dynamic_methods__.add("secondMethod")
        #     self.__dynamic_methods__.add("thirdMethod")
        #     self.__dynamic_methods__.add("ftvWorks")

        @staticmethod
        def print(message):
            Log.i(message)

        # @DynamicMethod()
        def ftvWorks(self):
            self.print("FTV Works!")

        # @DynamicMethod()
        def firstMethod(self):
            # self.print("firstMethod")
            self.first.activate()

        # @DynamicMethod()
        def secondMethod(self):
            # self.print("secondMethod")
            self.second.activate()

        # @DynamicMethod()
        def thirdMethod(self):
            # self.print("thirdMethod")
            self.third.activate()

    class SimpleModule(object):
        def __init__(self):
            super(SimpleModule, self).__init__()
            self.first = False
            self.second = False
            self.third = False

            self.firstMethod()
            if self.first:
                self.secondMethod()
                if self.second:
                    self.thirdMethod()
                    if self.third:
                        self.ftvWorks()

        @staticmethod
        def print(message):
            Log.i(message)

        def ftvWorks(self):
            self.print("FTV Works!")

        def firstMethod(self):
            # self.print("firstMethod")
            self.first = True

        def secondMethod(self):
            # self.print("secondMethod")
            self.second = True

        def thirdMethod(self):
            # self.print("thirdMethod")
            self.third = True

    DyModule()

    # list_a = []
    # list_b = []
    # list_c = []
    #
    # decay_factor = []
    #
    # cycles = 1
    #
    # for i in range(cycles):
    #     list_a.append(Efficiency.check(DyModule, 1200, "DyModule"))
    #     list_b.append(Efficiency.check(SimpleDyModule, 1200, "SimpleDyModule"))
    #     # list_c.append(Efficiency.check(SimpleModule, 1200, "SimpleModule"))
    #
    #     # if list_c[-1] != 0:
    #     #     decay_factor.append(list_a[-1]/list_c[-1])
    #
    # A = sum(list_a)/len(list_a)
    # B = sum(list_b)/len(list_b)
    # # C = sum(list_c)/len(list_c)
    #
    # # decayFactor = None
    # #
    # # if len(decay_factor) != 0:
    # #     decayFactor = sum(decay_factor)/len(decay_factor)
    #
    # Efficiency.printResult(A, "DyModule")
    # Efficiency.printResult(B, "SimpleDyModule")
    # # Efficiency.printResult(C, "SimpleModule")
    #
    # # print("Decay Factor: " + str(decayFactor))
    # # print("Decay Cycles: " + str(len(decay_factor)))
