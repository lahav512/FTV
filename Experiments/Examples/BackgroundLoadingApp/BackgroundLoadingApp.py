from FTV.FrameWork.Apps import UIApp
from FTV.Managers.ExecutionManager import ExecutionManager
from FTV.Objects.SystemObjects.Executions import DyThread


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


if __name__ == '__main__':
    app = App()
