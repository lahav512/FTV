import wrapt

from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DynamicObjectInterface


class DyMethod(DynamicObjectInterface):
    # __slots__ = ()

    # def __init__(self):
    #     super(DyMethod, self).__init__()

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        self.__log_p__("->"" {}".format(wrapped.__name__))
        self.__log_step__(1)
        # instance._ACTIVE_METHOD = wrapped.__name__
        ans = wrapped(*args, **kwargs)
        # instance._ACTIVE_METHOD = ""
        self.__log_step__(-1)
        self.__log_p__("<-"" {}".format(wrapped.__name__))
        self._prepareAndRunTriggers(instance.__get_dy_method__(wrapped))
        return ans

    @staticmethod
    def __log_p__(message):
        Log.p(message, Log.color.ORANGE)

    @staticmethod
    def __log_step__(step):
        Log.step(step)


class DyBuiltinMethod(DyMethod):

    @staticmethod
    def __log_p__(message):
        if Log.BUILTIN_ENABLED:
            DyMethod.__log_p__(message)

    @staticmethod
    def __log_step__(step):
        if Log.BUILTIN_ENABLED:
            DyMethod.__log_step__(step)
