

class Module(object):
    em = None
    vm = None
    lm = None

    def __init__(self):
        self.settings = Module.__Settings()

    def setupTriggers(self):
        pass

    def addTrigger(self):
        pass

    def loadFeatures(self):
        pass

    def loadFeature(self):
        pass

    def setupParents(self):
        pass

    def addParent(self):
        pass

    def setupSettings(self):
        pass

    class __Settings:
        def __init__(self):
            self.enabled = True

        def setEnabled(self):
            self.enabled = True

        def setDisabled(self):
            self.enabled = False
