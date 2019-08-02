from App.Variables.Print import Print


class PrintsManager:
    def __init__(self):
        self.prints = []

    def add(self):
        self.printers.append(Print())

    def remove(self, index):
        del self.prints[index]
