from FTV.Objects.Link import Link


class TriggerManager:
    setter_links = {}
    getter_links = {}
    preventLoop = False

    def __init__(self):
        pass

    @classmethod
    def add_trigger(cls, variable_parent, variable_key, feature, trigger, method):
        if variable_parent not in cls.setter_links:
            cls.setter_links[variable_parent] = {}

        cls.setter_links[variable_parent][variable_key] = Link(feature, variable_key, trigger, method)
        # cls._get_variable_name(feature)

    @classmethod
    def rename_key(cls, old_id, new_id):
        if old_id == new_id:
            return
        link = cls.setter_links[old_id]
        del cls.setter_links[old_id]
        cls.setter_links[new_id] = link
