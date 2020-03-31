class TempQueue(object):
    def __init__(self):
        self.__list__ = []

    def put_nowait(self, obj):
        self.__list__.insert(0, obj)

    def get_nowait(self):
        return self.__list__.pop()

    def empty(self):
        return not self.__list__
