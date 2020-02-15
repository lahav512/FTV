from AppPackage.FrameWork.Features.Feature1 import Feature1
from FTV.FrameWork.App import App


class MyApp(App):

    def setupSettings(self):
        self.settings.setUIPlatform(0)

    def loadFeatures(self):
        self.loadFeature(Feature1)


if __name__ == '__main__':
    MyApp()
