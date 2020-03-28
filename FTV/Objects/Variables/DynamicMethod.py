import wrapt

from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DynamicObjectInterface


class DynamicMethod(DynamicObjectInterface):
    # __slots__ = ()

    # def __init__(self):
    #     super(DynamicMethod, self).__init__()

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        self.__log_p__("->"" {}".format(wrapped.__name__))
        self.__log_step__(1)
        # instance._ACTIVE_METHOD = wrapped.__name__
        ans = wrapped(*args, **kwargs)
        # instance._ACTIVE_METHOD = ""
        self.__log_step__(-1)
        self.__log_p__("<-"" {}".format(wrapped.__name__))
        self._distributeTriggers(instance.__dynamic_methods__[wrapped.__name__])
        self._runActiveTriggers(instance.__dynamic_methods__[wrapped.__name__])
        return ans

    @staticmethod
    def __log_p__(message):
        Log.p(message, Log.color.ORANGE)

    @staticmethod
    def __log_step__(step):
        Log.step(step)


class BuiltinDynamicMethod(DynamicMethod):

    @staticmethod
    def __log_p__(message):
        if Log.BUILTIN_ENABLED:
            DynamicMethod.__log_p__(message)

    @staticmethod
    def __log_step__(step):
        if Log.BUILTIN_ENABLED:
            DynamicMethod.__log_step__(step)
