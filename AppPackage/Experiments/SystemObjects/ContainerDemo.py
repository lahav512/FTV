from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QWidget, QStackedLayout, QLayout,
                             QStackedWidget)

from AppPackage.Experiments.GeneralObjects.Container import Container, MyCell

FONT = "Arial"
FONT_SIZE = 14

class ContainerDemo(Container):
    @classmethod
    def setupUI(cls):

        label = QLabel(id)
        label.setFont(QFont(FONT, FONT_SIZE))
        label.setAlignment(QtCore.Qt.AlignCenter)

        cls.layout = QHBoxLayout()
        cls.layout.addWidget(label)

    @classmethod
    def setItem(cls, question, yes, no):
        pass

if __name__ == '__main__':
    ContainerDemo.showDemo()