from AppPackage.Objects.Printer import Printer


class PrintersManager:
    def __init__(self):
        self.printers = {}

    def add(self, printer, id_number: int):
        self.printers[id_number] = printer

    def remove(self, id_number):
        del self.printers[id_number]

    def get(self, id_number) -> Printer:
        return self.printers[id_number]
