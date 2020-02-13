import abc
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLayout


class Layout(QLayout):
    @abc.abstractmethod
    def set_container(self):
        pass

class Cell:
    @abc.abstractmethod
    def set_layout(self):
        pass

    @abc.abstractmethod
    def set_container(self):
        pass

class MyCell(Cell):
    def set_container(self):
        pass

    def set_layout(self):
        pass

class Container:
    layout: QLayout = None

    def __init__(self):
        self.setup_layout()
        self.add_cells()

    @abc.abstractmethod
    def setup_layout(self):
        pass

    @classmethod
    @abc.abstractmethod
    def add_cells(cls):
        pass

    def show(self):
        pass

class MyContainer(Container):
    def setup_layout(self):

        self.bottom_lay = QHBoxLayout()

        self.main_lay = QVBoxLayout()
        self.main_lay.addLayout(self.bottom_lay)

    @classmethod
    def add_cells(cls):
        cls.a = MyCell()
        cls.b = MyCell()
        cls.c = MyCell()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        MyContainer()
        MyContainer.a.set_layout()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())