import  time

from AppPackage.Experiments.Log import Log
from FTV.FrameWork.Apps import NIApp
from FTV.FrameWork.Features import NIFeature
from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DyInt


class VM(VariableManager):

    def setupVariables(self):
        self.tenth_seconds_mode = 10
        self.seconds_mode = 60
        self.minutes_mode = 60
        self.hours_mode = 24

        self.tenth_seconds = DyInt(0)
        self.seconds = DyInt(0)
        self.minutes = DyInt(0)
        self.hours = DyInt(0)

    def setupTriggers(self):
        self.addTrigger(self.tenth_seconds)\
            .setCondition(DyInt.IsGraterEqualTo, self.tenth_seconds_mode)\
            .setAction(self.updateUnit, self.tenth_seconds, self.seconds, self.tenth_seconds_mode)

        self.addTrigger(self.seconds)\
            .setCondition(DyInt.IsGraterEqualTo, self.seconds_mode)\
            .setAction(self.updateUnit, self.seconds, self.minutes, self.seconds_mode)

        self.addTrigger(self.minutes)\
            .setCondition(DyInt.IsGraterEqualTo, self.minutes_mode)\
            .setAction(self.updateUnit, self.minutes, self.hours, self.minutes_mode)

        self.addTrigger(self.hours)\
            .setCondition(DyInt.IsGraterEqualTo, self.hours_mode)\
            .setAction(self.modUnit, self.hours, self.hours, self.hours_mode)

    @DyMethod()
    def updateUnit(self, var_1: DyInt, var_2: DyInt, mod: int):
        self.addUnit(var_2, var_1, mod)
        self.modUnit(var_1, var_1, mod)

    # @DyMethod()
    def modUnit(self, var: DyInt, val: DyInt, mod: int):
        var.set(val.get() % mod)

    # @DyMethod()
    def addUnit(self, var: DyInt, val: DyInt, mod: int):
        var += val.get() // mod


class ClockFeature(DyModule):
    def setupSettings(self):
        pass

    @classmethod
    def setupManagers(cls):
        cls.vm = VM()

    def setupVariables(self):
        self.setupManagers()

    def setupTriggers(self):
        self.addTrigger(self.POST_INIT).setAction(self.startClock)
        # self.addTrigger(self.tick).setAction(self.tick)

    def getTimeStamp(self):
        return f"{self.vm.hours}:{self.vm.minutes}:{self.vm.seconds}:{self.vm.tenth_seconds}"

    def startClock(self):
        while True:
            self.tick()

    @DyMethod()
    def tick(self):
        self.vm.tenth_seconds += 1
        Log.p(self.getTimeStamp())
        time.sleep(0.1)


class EM(ExecutionManager):
    pass


class ClockApp(NIApp):
    def setupFeatures(self):
        self.addFeature(ClockFeature)

    def setupSettings(self):
        pass

    @classmethod
    def setupManagers(cls):
        # cls.fm = FM()
        cls.em = EM()
        cls.vm = VM()
        # cls.lm = LM()


if __name__ == '__main__':
    # app = ClockApp()
    # app.startApp()

    feature = ClockFeature()
    # feature.vm.START.activate()
