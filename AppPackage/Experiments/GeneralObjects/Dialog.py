from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLayout, QPushButton, QLabel

from AppPackage.Experiments.GeneralObjects.Container import Container, MyCell

FONT = "Arial"
FONT_SIZE = 10

class Dialog(Container):
    txt_question = None
    txt_yes = None
    txt_no = None

    question_label: QLabel = None
    btn_yes: QPushButton = None
    btn_no: QPushButton = None

    @classmethod
    def setup_ui(cls):

        cls.question_label = QLabel(cls.txt_question)
        cls.question_label.setFont(QFont(FONT, FONT_SIZE))

        cls.top_lay = QVBoxLayout()
        cls.top_lay.addWidget(cls.question_label)

        cls.btn_yes = QPushButton(cls.txt_yes)
        cls.btn_yes.setFont(QFont(FONT, FONT_SIZE))
        cls.btn_no = QPushButton(cls.txt_no)
        cls.btn_no.setFont(QFont(FONT, FONT_SIZE))

        cls.bottom_lay = QHBoxLayout()
        cls.bottom_lay.addWidget(cls.btn_yes)
        cls.bottom_lay.addWidget(cls.btn_no)

        cls.layout = QVBoxLayout()
        cls.layout.addLayout(cls.top_lay)
        cls.layout.addLayout(cls.bottom_lay)
        # return layout

    @classmethod
    def add_cells(cls):
        cls.a = MyCell()
        cls.b = MyCell()
        cls.c = MyCell()

    @classmethod
    def set_item(cls, question, yes, no):
        cls.question_label.setText(question)
        cls.btn_yes.setText(yes)
        cls.btn_no.setText(no)

class Dialog2(Dialog):
    pass

if __name__ == '__main__':
    Dialog.show_demo()