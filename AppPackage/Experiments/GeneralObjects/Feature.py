import abc


class Feature:
    ui_platform = None

    def __init__(self):
        self.setSettings()
        self.init()

    def init(self):
        pass

    def setSettings(self):
        pass

    @staticmethod
    def setUIPlatform(ui_platform):
        Feature.ui_platform = ui_platform
