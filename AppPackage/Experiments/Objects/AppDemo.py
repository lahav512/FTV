from AppPackage.Experiments.GeneralObjects.App import App
from AppPackage.Experiments.Objects.Containers.Dialog import Dialog, Dialog2, Dialog3, Dialog4
from AppPackage.Experiments.Objects.Containers.MainWindow import MainWindow
from AppPackage.Experiments.Objects.Features.FeatureDemo import FeatureDemo




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


if __name__ == '__main__':
    AppDemo()
