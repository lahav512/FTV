from Experiments.Log import Log
from FTV.FrameWork.Apps import UIApp
from FTV.Managers.ExecutionManager import ExecutionManager
from FTV.Objects.SystemObjects.Executions import DyThread
from FTV.Objects.Variables.DynamicMethods import DyMethod


class EM(ExecutionManager):
    def setupThreads(self):
        self.MainUI = DyThread()


class App(UIApp):
    def setupFeatures(self):
        from Experiments.Examples.BackgroundLoadingApp.Features.FeaturesLoader import FeaturesLoader
        from Experiments.Examples.BackgroundLoadingApp.Features.FeaturesLoaderProgress import \
            FeaturesLoaderProgress

        self.addFeature(FeaturesLoaderProgress)
        self.addFeature(FeaturesLoader)

    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setExecutionManager(EM)

    def setupTriggers(self):
        self.addTrigger(self.vm.START).setAction(self.startAppOperations)
        self.addTrigger(self.vm.EXIT).setAction(self.printRuntime)

    @DyMethod()
    def printRuntime(self):
        Log.p(App.runtime)

    @DyMethod()
    def startAppOperations(self):
        Log.p("Application is running!")


if __name__ == '__main__':
    app = App()
