from FTV.Objects.Link import Link


class TriggerManager:
    setter_links = {}
    getter_links = {}
    preventLoop = False

    def __init__(self):
        pass

    def add_trigger(self, variable, trigger, method):
        TriggerManager.setter_links[id(variable)] = Link(self, trigger, method)

    @classmethod
    def rename_key(cls, old_id, new_id):
        if old_id == new_id:
            return
        link = cls.setter_links[old_id]
        del cls.setter_links[old_id]
        cls.setter_links[new_id] = link
