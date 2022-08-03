import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox, QLineEdit, QLabel


def random():
    print("hier wird random pw generiert")


def safe():
    print("hier wird sicheres pw generiert")


class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        #self.init_window()

    #def init_window(self):

        width = 500
        height = 500

        self.setFixedSize(width, height)
        self.setWindowTitle("Passwortgenerator")
        self.setWindowIcon(QtGui.QIcon("generator.jpeg"))

        button_random = QPushButton("Random Passwort", self)
        button_random.setGeometry(70, 130, 120, 25)
        button_random.clicked.connect(random)

        textbox_random = QLineEdit(self)
        textbox_random.setGeometry(300, 130, 150, 20)

        button_safe = QPushButton("Sicheres Passwort", self)
        button_safe.setGeometry(70, 280, 120, 25)
        button_safe.clicked.connect(safe)

        textbox_safe = QLineEdit(self)
        textbox_safe.setGeometry(300, 280, 150, 20)

        self.checkbox_custom = QCheckBox(self)
        self.checkbox_custom.setGeometry(230, 280, 120, 25)
        self.checkbox_custom.stateChanged.connect(self.custom)

        self.label_checkbox = QLabel("Custom", self)
        self.label_checkbox.move(220, 310)

        self.checkbox_upper_lower = QCheckBox(self)
        self.checkbox_upper_lower.setGeometry(80, 340, 100, 25)
        self.checkbox_upper_lower.hide()

        self.label_upper_lower = QLabel("Groß- und Kleinschreibung", self)
        self.label_upper_lower.move(110, 345)
        self.label_upper_lower.hide()

        self.checkbox_numbers = QCheckBox(self)
        self.checkbox_numbers.setGeometry(80, 380, 100, 25)
        self.checkbox_numbers.hide()

        self.label_numbers = QLabel("Ziffern", self)
        self.label_numbers.move(110, 385)
        self.label_numbers.hide()

        self.checkbox_sign = QCheckBox(self)
        self.checkbox_sign.setGeometry(80, 420, 100, 25)
        self.checkbox_sign.hide()

        self.label_sign = QLabel("Zeichen", self)
        self.label_sign.move(110, 425)
        self.label_sign.hide()

        self.show()

    def custom(self, state):
        if QtCore.Qt.Checked == state:
            self.checkbox_upper_lower.show()
            self.label_upper_lower.show()
            self.checkbox_numbers.show()
            self.label_numbers.show()
            self.checkbox_sign.show()
            self.label_sign.show()
        else:
            self.checkbox_upper_lower.hide()
            self.label_upper_lower.hide()
            self.checkbox_numbers.hide()
            self.label_numbers.hide()
            self.checkbox_sign.hide()
            self.label_sign.hide()
