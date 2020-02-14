from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QWidget, QStackedLayout, QLayout,
                             QStackedWidget)

from AppPackage.Experiments.GeneralObjects.Container import Container, MyCell

FONT = "Arial"
FONT_SIZE = 10

class MainWindow(Container):
    def __init__(self):
        super().__init__()
        # self.question_label = QLabel("Lahav")
        # self.left_layout.addWidget(self.question_label)

    @classmethod
    def setupUI(cls):

        cls.frame_a = QStackedWidget()
        cls.frame_b = QStackedWidget()
        cls.frame_c = QStackedWidget()
        cls.frame_d = QStackedWidget()

        cls._setID(cls.frame_a, "A")
        cls._setID(cls.frame_b, "B")
        cls._setID(cls.frame_c, "C")
        cls._setID(cls.frame_d, "D")

        cls.left_layout = QVBoxLayout()
        cls.left_layout.setContentsMargins(0,0,0,0)
        cls.left_layout.setSpacing(2)
        cls.left_layout.addWidget(cls.getCell("A"))
        cls.left_layout.addWidget(cls.getCell("B"))

        cls.left_widget = QWidget()
        cls.left_widget.setLayout(cls.left_layout)

        cls.layout = QHBoxLayout()
        cls.layout.addWidget(cls.left_widget)
        cls.layout.addWidget(cls.getCell("C"))
        cls.layout.addWidget(cls.getCell("D"))

    @classmethod
    def setItem(cls, question, yes, no):
        pass
        # cls.question_label.setText(question)
        # cls.btn_yes.setText(yes)
        # cls.btn_no.setText(no)

if __name__ == '__main__':
    MainWindow.showDemo()