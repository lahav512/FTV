from FTV.FrameWork.Module import Module


class Feature(Module):
    uim = None

    def __init__(self):
        super().__init__()
        self.settings: __class__._Settings
        self.setupUITriggers()
        self.setupContainers()

    # def __createSettings(self):
    #     self.settings = Module._Settings()

    def setupUITriggers(self):
        pass

    def setupContainers(self):
        pass

    class _Settings(Module._Settings):
        def setUIPlatform(self, ui_platform):
            pass
