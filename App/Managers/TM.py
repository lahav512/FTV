from FTV.Managers.TriggersManager import TriggersManager

from App.Triggers.DictFirstItemAdded import DictFirstItemAdded


class TM(TriggersManager):
    DictFirstItemAdded = DictFirstItemAdded

    def __init__(self):
        super().__init__()

