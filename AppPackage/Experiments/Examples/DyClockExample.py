import  time

from FTV.FrameWork.Apps import NIApp
from FTV.FrameWork.Features import NIFeature
from FTV.Managers.EexecutionManager import ExecutionManager
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicModules import DyModule
from FTV.Objects.Variables.DynamicObjects import DyInt


class VM(VariableManager):

    def setupVariables(self):
        self.mode = 10
        self.hours = DyInt(0)
        self.minutes = DyInt(0)
        self.seconds = DyInt(0)

    def setupTriggers(self):
        self.addTrigger(self.seconds)\
            .setCondition(DyInt.IsEqualTo, self.mode)\
            .setAction(self.setSeconds, 0)

        self.addTrigger(self.seconds) \
            .setCondition(DyInt.IsEqualTo, 0) \
            .setAction(self.addMinutes, 1)

    @DyMethod()
    def setHours(self, hours: int):
        self.hours.set(hours)

    @DyMethod()
    def setMinutes(self, minutes: int):
        self.minutes.set(minutes)

    @DyMethod()
    def setSeconds(self, seconds: int):
        self.seconds.set(seconds)

    @DyMethod()
    def addMinutes(self, minutes: int):
        self.minutes += minutes


class ClockFeature(DyModule):
    def setupSettings(self):
        pass

    @classmethod
    def setupManagers(cls):
        cls.vm = VM()

    def setupVariables(self):
        self.setupManagers()

    def setupTriggers(self):
        self.addTrigger(self.POST_INIT).setAction(self.tick)
        self.addTrigger(self.tick).setAction(self.tick)

    @DyMethod()
    def tick(self):
        self.vm.seconds += 1
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
