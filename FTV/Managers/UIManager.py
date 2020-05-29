from FTV.Managers.AbstractManager import AbstractManager


class UIManager(AbstractManager):
    __short_name__ = "UIM"

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        pass
