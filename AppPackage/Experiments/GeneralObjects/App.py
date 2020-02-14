import abc
import sys

from PyQt5.QtWidgets import QApplication


global __app


class App:
    def __init__(self):
        __app = QApplication(sys.argv)

        self.initContainers()
        self.initFeatures()
        self.start()

        # sys.exit(__app.exec_())
        __app.exec_()

    @abc.abstractmethod
    def initContainers(self):
        pass

    @abc.abstractmethod
    def initFeatures(self):
        pass

    @abc.abstractmethod
    def start(self):
        pass
