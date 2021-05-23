import time

from Experiments.Log import Log
from FTV.FrameWork.Apps import UIApp
from FTV.Managers.ExecutionManager import ExecutionManager
from FTV.Objects.SystemObjects.Executions import DyThread, DyThreadList
from FTV.Objects.Variables.DynamicMethods import DyMethod


class EM(ExecutionManager):
    def setupThreads(self):
        self.MainUI = DyThread()
        self.MainApplication = DyThread()
        self.Tests = DyThreadList()


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
        self.addTrigger(self.vm.START).setAction(self.startAppOperations).setThread(self.em.MainApplication)
        self.addTrigger(self.vm.START).setAction(self.startAppOperations).setThread(self.em.MainUI)
        # self.addTrigger(self.vm.START).setAction(self.startTest, "test 1").setThread(self.em.Tests)
        # self.addTrigger(self.vm.START).setAction(self.startTest, "test 2").setThread(self.em.Tests)
        # self.addTrigger(self.vm.START).setAction(self.startTest, "test 3").setThread(self.em.Tests)

        # self.addTrigger(self.vm.EXIT).setAction(self.printRuntime)

    @DyMethod()
    def printRuntime(self):
        Log.p(App.runtime)

    @DyMethod()
    def startAppOperations(self):
        Log.p("Application is running!")
        # time.sleep(1)

    @DyMethod()
    def startTest(self, test):
        Log.p(f"Running \"{test}\"")
        time.sleep(int(test[-1]))


if __name__ == '__main__':
    app = App()
