
class DyBool(object):
    def __init__(self, value):
        self.value = value

    def __set__(self, instance, value):
        self.value = value


a = DyBool(False)
a = True
print(type(a))
