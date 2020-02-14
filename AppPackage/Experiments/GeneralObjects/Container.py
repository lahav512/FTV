import abc
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLayout

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
    __window = None
    __app = None
    __container = None
    print(__name__)

    def __init__(self):
        self.__setup_variables()
        self.setup_ui()
        self.__window.setLayout(self.layout)
        self.add_cells()

    @classmethod
    def __setup_variables(cls):
        cls.__window = QWidget()

    @abc.abstractmethod
    def setup_ui(self):
        pass

    @abc.abstractmethod
    def set_item(self, *args):
        pass

    @classmethod
    @abc.abstractmethod
    def add_cells(cls):
        pass

    @classmethod
    def show(cls):
        cls.__window.show()

    @classmethod
    def show_demo(cls):
        cls.__app = QApplication(sys.argv)
        cls.__container = cls()
        cls.__container.show()
        sys.exit(cls.__app.exec_())
