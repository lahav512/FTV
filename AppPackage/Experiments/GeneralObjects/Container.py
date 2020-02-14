import abc
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QFrame


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
    frames: dict = {}

    __window = None
    __app = None
    __container = None

    _is_show = False

    def __init__(self):
        self.__setupVariables()
        self.setupUI()
        self.__window.setLayout(self.layout)

    @classmethod
    def __setupVariables(cls):
        cls.__window = QWidget()

    @classmethod
    def _setID(cls, frame, frame_id=None):
        if frame_id is None:
            frame_id = len(cls.frames)

        cls.frames[frame_id] = frame

    @abc.abstractmethod
    def setupUI(self):
        pass

    @abc.abstractmethod
    def setItem(self, *args):
        pass

    @classmethod
    def show(cls):
        cls._is_show = True
        cls.__window.show()

    @classmethod
    def hide(cls):
        cls._is_show = False
        cls.__window.hide()

    @classmethod
    def showDemo(cls):
        cls.__app = QApplication(sys.argv)
        cls.__container = cls()
        cls.__container.show()
        sys.exit(cls.__app.exec_())
