from AppPackage.Objects.Print import Print


class PrintsManager:
    next_id = 0

    def __init__(self):
        self.prints = {}

    def add(self, _print):
        self.prints[self.next_id] = _print
        self.next_id += 1

    def remove(self, id_number):
        del self.prints[id_number]

    def get(self, id_number) -> Print:
        return self.prints[id_number]

