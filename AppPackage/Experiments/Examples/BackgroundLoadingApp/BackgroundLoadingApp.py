from AppPackage.Experiments.Examples.BackgroundLoadingApp.FeaturesLoader import FeaturesLoader
from AppPackage.Experiments.Examples.BackgroundLoadingApp.FeaturesLoaderProgress import FeaturesLoaderProgress
from FTV.FrameWork.Apps import NIApp
from FTV.Managers.ExecutionManager import ExecutionManager
from FTV.Objects.SystemObjects.Executions import DyThread


class EM(ExecutionManager):
    def _setupBuiltinThreads(self):
        super(EM, self)._setupBuiltinThreads()
        self.LoadFeatures = DyThread()

class App(NIApp):
    def setupFeatures(self):
        self.addFeature(FeaturesLoader)
        self.addFeature(FeaturesLoaderProgress)

    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setExecutionManager(EM)


if __name__ == '__main__':
    app = App()
