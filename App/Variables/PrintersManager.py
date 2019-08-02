from App.Objects.Printer import Printer


class PrintersManager:
    def __init__(self):
        self.printers = []

    def add(self):
        self.printers.append(Printer())

    def remove(self, index):
        del self.printers[index]
