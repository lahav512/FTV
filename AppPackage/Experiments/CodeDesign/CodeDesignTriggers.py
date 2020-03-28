from FTV.Objects.Variables.DynamicMethods import *
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import *


class Module(DyModule):

    def setupVariables(self):
        self.dy_object_or_method = DyBool(False)
        self.b = DyBool(False)
        self.onSwitch = DySwitch()

    def setupTriggers(self):
        self.addTrigger(self.dy_object_or_method, condition=DyObject.isChanged(*args, **kwargs))\
            .setAction(action=self.dy_object_or_method, *args, **kwargs)\
            .setThread(thread=self.threads.main)

    @DyMethod()
    def printFinish(self):
        Log.p("finish")


class DyObjectDemo:
    def __condition__(self, *args, **kwargs):
        return True

    def __action__(self, *args, **kwargs):
        pass

class DyMethodObjectDemo(object):
    def __condition__(self, *args, **kwargs):
        return True

    def __action__(self, *args, **kwargs):
        self.__call__(*args, **kwargs)

