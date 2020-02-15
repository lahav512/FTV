

class Module(object):
    em = None
    vm = None
    lm = None

    def __init__(self):
        self.loadFeatures()
        # self.setupManagers()
        self.__setups()

    # def setupManagers(self):
    #     pass

    def __setups(self):
        self.settings = self.__class__._Settings()
        self.setupSettings()
        self.setupTriggers()
        self.setupParents()

    def setupTriggers(self):
        pass

    def addTrigger(self):
        pass

    def loadFeatures(self):
        pass

    def loadFeature(self, feature):
        feature()

    def setupParents(self):
        pass

    def addParent(self, parent):
        pass

    def setupSettings(self):
        pass

    class _Settings:
        def __init__(self):
            self.enabled = True

        def setEnabled(self):
            self.enabled = True

        def setDisabled(self):
            self.enabled = False
