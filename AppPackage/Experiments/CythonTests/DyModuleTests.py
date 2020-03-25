from AppPackage.Experiments import Efficiency
from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DynamicMethod
from FTV.Objects.Variables.DynamicModuleObject import DynamicModule
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


if __name__ == '__main__':
    DyModule()

    list_a = []
    list_b = []
    list_c = []

    decay_factor = []

    cycles = 1

    for i in range(cycles):
        list_a.append(Efficiency.check(DyModule, 1200, "DyModule"))
        list_b.append(Efficiency.check(SimpleDyModule, 1200, "SimpleDyModule"))
        # list_c.append(Efficiency.check(SimpleModule, 1200, "SimpleModule"))

        # if list_c[-1] != 0:
        #     decay_factor.append(list_a[-1]/list_c[-1])

    A = sum(list_a)/len(list_a)
    B = sum(list_b)/len(list_b)
    # C = sum(list_c)/len(list_c)

    # decayFactor = None
    #
    # if len(decay_factor) != 0:
    #     decayFactor = sum(decay_factor)/len(decay_factor)

    Efficiency.printResult(A, "DyModule")
    Efficiency.printResult(B, "SimpleDyModule")
    # Efficiency.printResult(C, "SimpleModule")

    # print("Decay Factor: " + str(decayFactor))
    # print("Decay Cycles: " + str(len(decay_factor)))
