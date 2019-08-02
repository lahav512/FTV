from App.Objects.Print import Print


class PrintsManager:
    def __init__(self):
        self.prints = {}

    def add(self, _print, id_number: int):
        self.prints[id_number] = _print

    def remove(self, id_number):
        del self.prints[id_number]

    def get(self, id_number) -> Print:
        return self.prints[id_number]

