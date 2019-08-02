

class Feature:
    def __init__(self, name):
        self.enabled: bool
        self.name = name

    def set_enabled(self):
        self.enabled = True

    def set_disabled(self):
        self.enabled = False
