import abc
import sys

from PyQt5.QtWidgets import QApplication


global app


class App:
    def __init__(self):
        app = QApplication(sys.argv)

        self.init_containers()
        self.init_features()
        self.start()

        sys.exit(app.exec_())

    @abc.abstractmethod
    def init_containers(self):
        pass

    @abc.abstractmethod
    def init_features(self):
        pass

    @abc.abstractmethod
    def start(self):
        pass
