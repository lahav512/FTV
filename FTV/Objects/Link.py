
class Link:
    def __init__(self, feature, trigger, method):
        self.feature = feature
        self.trigger = trigger()
        self.method = method
