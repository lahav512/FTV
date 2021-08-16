import os

from FTV.Managers.FeatureManager import FeatureManager
from FTV.Managers.Log import Log
from FTV.FrameWork.Apps import NIApp
from FTV.FrameWork.Features import NIFeature
from FTV.Managers.VariableManager import VariableManager
from FTV.Objects.SystemObjects.TriggerObjects import Condition
from FTV.Objects.Variables.DynamicMethods import DyMethod
from FTV.Objects.Variables.DynamicObjects import DySwitch, DyStr
from youtube_dl import YoutubeDL


class VM(VariableManager):
    def setupVariables(self):
        self.onStartDownload = DySwitch()
        self.postIntro = DySwitch()
        self.preLinkSelection = DySwitch()
        self.preDownload = DySwitch()
        self.directory = DyStr()
        self.downloadLink = DyStr()

    def setupTriggers(self):
        pass

    class IsDirExist(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return os.path.exists(new_val)

    class IsLinkValid(Condition):
        @staticmethod
        def __condition__(old_val, new_val, *args, **kwargs):
            return new_val.startswith("https://")


class FM(FeatureManager):
    def setupFeatures(self):
        self.addFeature(ConsoleDownloadFiles)


class ConsoleDownloadFiles(NIFeature):
    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setVariableManager(VM)

    def setupTriggers(self):
        self.addTrigger(YoutubeDownloaderApp.vm.START).setAction(self.showIntro)
        self.addTrigger(self.showIntro).setAction(self.vm.postIntro)
        self.addTrigger(self.vm.postIntro).setAction(self.askForDirectory)
        self.addTrigger(self.vm.directory).setAction(self.vm.preLinkSelection)\
            .setCondition(VM.IsDirExist)\
            .elseAction(self.askForDirectoryAgain)
        self.addTrigger(self.vm.preLinkSelection).setAction(self.askForDownloadLink)
        self.addTrigger(self.vm.downloadLink).setAction(self.vm.preDownload)\
            .setCondition(VM.IsLinkValid)\
            .elseAction(self.askForDownloadLinkAgain)
        self.addTrigger(self.vm.preDownload).setAction(self.download)

    @DyMethod()
    def showIntro(self):
        Log.p("Welcome to the Youtube Downloader program!")

    @DyMethod()
    def askForDirectory(self):
        self.vm.directory.set(Log.get("Please enter your download directory: "))

    @DyMethod()
    def askForDirectoryAgain(self):
        self.vm.directory.set(Log.get("The entered directory is does not exist.\n"
                                      "Please try again: "))

    @DyMethod()
    def askForDownloadLink(self):
        self.vm.downloadLink.set(Log.get("Please enter your YouTube url: "))

    @DyMethod()
    def askForDownloadLinkAgain(self):
        self.vm.downloadLink.set(Log.get("The entered url is invalid.\n"
                                         "Please try again: "))

    @DyMethod()
    def download(self):
        Log.p("downloading...")


class YoutubeDownloaderApp(NIApp):
    def setupSettings(self):
        pass

    def setupManagers(self):
        self.setFeatureManager(FM)


YoutubeDownloaderApp()

