from Experiments.GeneralObjects.App import App
from Experiments.Objects.Containers.Dialog import Dialog, Dialog2, Dialog3, Dialog4
from Experiments.Objects.Containers.MainWindow import MainWindow
from Experiments.Objects.Features.FeatureDemo import FeatureDemo
from FTV.Objects.SystemObjects import UIPlatforms


class AppDemo(App):
    def start(self):
        # Dialog.show()
        # Dialog2.show()
        MainWindow.show()

    def initContainers(self):
        MainWindow()
        Dialog()
        Dialog2()
        Dialog3()
        Dialog4()

    def initFeatures(self):
        FeatureDemo()

    def setSettings(self):
        self.setUIPlatform(UIPlatforms.PyQt5)


if __name__ == '__main__':
    AppDemo()
