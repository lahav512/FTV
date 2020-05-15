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
        self.seconds_mode = 60
        self.minutes_mode = 60
        self.hours_mode = 24

        self.hours = DyInt(0)
        self.minutes = DyInt(0)
        self.seconds = DyInt(0)

    def setupTriggers(self):
        self.addTrigger(self.seconds)\
            .setCondition(DyInt.IsEqualTo, self.seconds_mode)\
            .setAction(self.setSeconds, 0)

        self.addTrigger(self.seconds) \
            .setCondition(DyInt.IsEqualTo, 0) \
            .setAction(self.addMinutes, 1)

        self.addTrigger(self.minutes)\
            .setCondition(DyInt.IsEqualTo, self.minutes_mode)\
            .setAction(self.setMinutes, 0)

        self.addTrigger(self.minutes) \
            .setCondition(DyInt.IsEqualTo, 0) \
            .setAction(self.addHours, 1)

        self.addTrigger(self.hours)\
            .setCondition(DyInt.IsEqualTo, self.hours_mode)\
            .setAction(self.setHours, 0)

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

    @DyMethod()
    def addHours(self, hours: int):
        self.hours += hours


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

    def getTimeStamp(self):
        return f"{self.vm.hours}:{self.vm.minutes}:{self.vm.seconds}"

    @DyMethod()
    def tick(self):
        self.vm.seconds += 1
        Log.p(self.getTimeStamp())
        time.sleep(1)


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
