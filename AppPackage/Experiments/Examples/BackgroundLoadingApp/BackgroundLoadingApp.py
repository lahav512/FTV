from FTV.FrameWork.Apps import NIApp
from FTV.Managers.ExecutionManager import ExecutionManager
from FTV.Objects.SystemObjects.Executions import DyThread


class EM(ExecutionManager):
    def _setupBuiltinThreads(self):
        super(EM, self)._setupBuiltinThreads()
        self.MainUI = DyThread()

class App(NIApp):
    def setupFeatures(self):
        from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.FeaturesLoader import FeaturesLoader
        from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.FeaturesLoaderProgress import \
            FeaturesLoaderProgress

        self.addFeature(FeaturesLoaderProgress)
        self.addFeature(FeaturesLoader)

    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setExecutionManager(EM)


if __name__ == '__main__':
    app = App()
