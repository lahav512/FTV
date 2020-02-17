from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.DynamicVariable import DynamicVariable


class TriggerManager:
    setter_links = {}
    getter_links = {}
    # preventLoop = False

    def __init__(self):
        pass

    @classmethod
    def addTrigger(cls, variable, trigger, action, thread_id=None):
        cls.setter_links[id(variable)] = cls._Link(cls, trigger, action, thread_id)

    @classmethod
    def checkTriggers(cls, variable: DynamicVariable, new_value, old_value):
        triggered_links = []
        Log.d("links: {}".format(variable.__links__))
        for link in variable.__links__:
            if link.trigger.condition():
                triggered_links.append(link)

        if triggered_links:
            print()

        map(lambda _link: _link.runAction(), triggered_links)

    @classmethod
    def rename_key(cls, old_id, new_id):
        if old_id == new_id:
            return
        link = cls.setter_links[old_id]
        del cls.setter_links[old_id]
        cls.setter_links[new_id] = link

    class _Link:
        def __init__(self, feature, trigger, action, thread_id):
            self.feature = feature
            self.trigger = trigger
            self.action = action
            self.thread_id = thread_id

        def runAction(self):
            self.feature.em.getThread(self.thread_id).start(self.action)

