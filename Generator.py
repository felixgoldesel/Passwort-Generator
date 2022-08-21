import string
import random

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QCheckBox, QLabel


class Generator(QWidget):
    def __init__(self):
        super().__init__()

        button_random = QPushButton("Zufälliges Passwort", self)
        button_random.setGeometry(70, 130, 120, 25)
        button_random.clicked.connect(self.random_pw)

        self.textbox_random = QTextEdit(self)
        self.textbox_random.setGeometry(300, 130, 150, 25)

        button_word = QPushButton("Wortbasiert", self)
        button_word.setGeometry(70, 205, 120, 25)
        button_word.clicked.connect(self.word_pw)

        self.textbox_word = QTextEdit(self)
        self.textbox_word.setGeometry(300, 205, 150, 25)

        self.checkbox_custom_word = QCheckBox(self)
        self.checkbox_custom_word.setGeometry(230, 205, 120, 25)
        self.checkbox_custom_word.stateChanged.connect(self.custom)

        label_checkbox_word = QLabel("Custom", self)
        label_checkbox_word.move(220, 235)

        button_safe = QPushButton("Sicheres Passwort", self)
        button_safe.setGeometry(70, 280, 120, 25)
        button_safe.clicked.connect(self.safe_pw)

        self.textbox_safe = QTextEdit(self)
        self.textbox_safe.setGeometry(300, 280, 150, 25)

        self.checkbox_custom = QCheckBox(self)
        self.checkbox_custom.setGeometry(230, 280, 120, 25)
        self.checkbox_custom.stateChanged.connect(self.custom)

        label_checkbox = QLabel("Custom", self)
        label_checkbox.move(220, 310)

        self.checkbox_upper_lower = QCheckBox(self)
        self.checkbox_upper_lower.setGeometry(80, 340, 100, 25)
        self.checkbox_upper_lower.hide()
        self.checkbox_upper_lower.setChecked(True)

        self.label_upper_lower = QLabel("Groß- und Kleinschreibung", self)
        self.label_upper_lower.move(110, 345)
        self.label_upper_lower.hide()

        self.checkbox_numbers = QCheckBox(self)
        self.checkbox_numbers.setGeometry(80, 380, 100, 25)
        self.checkbox_numbers.hide()
        self.checkbox_numbers.setChecked(True)

        self.label_numbers = QLabel("Ziffern", self)
        self.label_numbers.move(110, 385)
        self.label_numbers.hide()

        self.checkbox_sign = QCheckBox(self)
        self.checkbox_sign.setGeometry(80, 420, 100, 25)
        self.checkbox_sign.hide()
        self.checkbox_sign.setChecked(True)

        self.label_sign = QLabel("Zeichen", self)
        self.label_sign.move(110, 425)
        self.label_sign.hide()

    def custom(self, state):
        if QtCore.Qt.Checked == state:
            if self.checkbox_custom_word.isChecked():
                self.checkbox_custom.setCheckable(False)
            if self.checkbox_custom.isChecked():
                self.checkbox_custom_word.setCheckable(False)
            self.checkbox_upper_lower.show()
            self.label_upper_lower.show()
            self.checkbox_numbers.show()
            self.label_numbers.show()
            self.checkbox_sign.show()
            self.label_sign.show()
        else:
            if self.checkbox_custom_word.isChecked() is False:
                self.checkbox_custom.setCheckable(True)
            if self.checkbox_custom.isChecked() is False:
                self.checkbox_custom_word.setCheckable(True)
            self.checkbox_upper_lower.hide()
            self.label_upper_lower.hide()
            self.checkbox_numbers.hide()
            self.label_numbers.hide()
            self.checkbox_sign.hide()
            self.label_sign.hide()

    def random_pw(self):
        pw_length = random.randint(5, 10)
        pw = ''
        for x in range(pw_length):
            pw += random.choice(string.ascii_letters)

        self.textbox_random.setPlainText(pw)

    def word_pw(self):
        #file_path = './sample.txt'

        with open('./sample.txt') as file:
            random_num = random.randint(1, 15)
            content = file.readlines()
            print(content[random_num])

    def safe_pw(self):
        pw_length = random.randint(8, 12)
        pw = ''
        allowed = ''
        if self.checkbox_upper_lower.isChecked():
            allowed += string.ascii_letters
        if self.checkbox_numbers.isChecked():
            allowed += string.digits
        if self.checkbox_sign.isChecked():
            allowed += string.punctuation

        if not self.checkbox_upper_lower.isChecked() and not self.checkbox_numbers.isChecked() and not self.checkbox_sign.isChecked():
            pw = "Praesidium_sit_amet!"
            self.textbox_safe.setPlainText(pw)
            return

        for x in range(pw_length):
            pw += random.choice(allowed)

        self.textbox_safe.setPlainText(pw)
