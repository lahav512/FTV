

class Feature:
    def __init__(self):
        self.enabled: bool

    def set_enabled(self):
        self.enabled = True

    def set_disabled(self):
        self.enabled = False


if __name__ == '__main__':
    Feature()
