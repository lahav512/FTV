

class TriggerManager:
    setter_links = {}
    getter_links = {}
    # preventLoop = False

    def __init__(self):
        pass

    @classmethod
    def add_trigger(cls, variable, trigger, action, thread_id=None):
        cls.setter_links[id(variable)] = cls.__Link(cls, trigger, action, thread_id)

    @classmethod
    def rename_key(cls, old_id, new_id):
        if old_id == new_id:
            return
        link = cls.setter_links[old_id]
        del cls.setter_links[old_id]
        cls.setter_links[new_id] = link

    class __Link:
        def __init__(self, feature, trigger, action, thread_id):
            self.feature = feature
            self.trigger = trigger
            self.action = action
            self.thread_id = thread_id

        def runAction(self):
            self.feature.em.getThread(self.thread_id).start(self.action)

