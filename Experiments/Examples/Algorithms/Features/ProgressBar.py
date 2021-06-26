from Experiments.Examples.Algorithms.CalculationApp import CalculationApp
from Experiments.Log import Log
from FTV.FrameWork.Features import NIFeature
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.SystemObjects.TriggerObjects import Condition
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicObjects import DyFloat, DyBool


class VM(VariableManager):
    def setupVariables(self):
        self.progress = CalculationApp.vm.progress
        self.isUpdatePBFree = DyBool(True, builtin=True)

    def setupTriggers(self):
        pass

    class IsRoundCompleted(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return old_val < args[0]*(new_val // args[0])


class ProgressBar(NIFeature):
    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setVariableManager(VM)

    def setupTriggers(self):
        self.addTrigger(self.vm.progress).setAction(self.vm.isUpdatePBFree, False)
        self.addTrigger(self.vm.progress).setAction(self.updatePB)\
            .setThread(CalculationApp.em.MainUI)\
            .setCondition(self.vm.isUpdatePBFree)
            # .setCondition(VM.IsRoundCompleted, 0.01)\

        self.addTrigger(self.updatePB).setAction(self.vm.isUpdatePBFree, True)

    @DyMethod()
    def updatePB(self):
        Log.p(f"{round(self.vm.progress * 100, 1)}%")
