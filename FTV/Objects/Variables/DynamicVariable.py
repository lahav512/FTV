
class Link:
    def __init__(self, feature, trigger, action, thread_id):
        self.feature = feature
        self.trigger = trigger
        self.action = action
        self.thread_id = thread_id

    def runAction(self):
        self.feature.em.getThread(self.thread_id).start(self.action)

class DynamicVariable(object):
    def __init__(self, value=None):
        self.__value: object = value
        self.links: list[Link] = []

    def set(self, value):
        self.__value = value

    def get(self):
        return self.__value

    def updated(self):
        triggered_links = []
        for link in self.links:
            if link.trigger.condition():
                triggered_links.append(link)

        map(lambda _link: _link.runAction(), triggered_links)

class DyBool(DynamicVariable):
    def __init__(self, value):
        super().__init__(value)
        self.value: bool


a = DyBool(True)
