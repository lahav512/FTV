from AppPackage.Experiments.GeneralObjects.App import App
from AppPackage.Experiments.GeneralObjects.Dialog import Dialog, Dialog2
from AppPackage.Experiments.GeneralObjects.FeatureDemo import FeatureDemo




class AppDemo(App):
    def start(self):
        Dialog.show()
        # Dialog2.show()

    def init_containers(self):
        Dialog()
        # Dialog2()

    def init_features(self):
        FeatureDemo()


if __name__ == '__main__':
    AppDemo()
