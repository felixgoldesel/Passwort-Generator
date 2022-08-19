import string

from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QComboBox, QPushButton


class EncodeDecode(QWidget):
    def __init__(self):
        super().__init__()

        self.menu = QComboBox(self)
        self.menu.setGeometry(50, 20, 150, 25)
        self.menu.addItem("---")
        self.menu.addItem("Run Length Encoding")
        self.menu.addItem("Lempel-Ziv-Welch")
        self.menu.addItem("kp")

        self.menu.currentIndexChanged.connect(self.coding)

        # encode = QLabel("Verschlüsseln", self)
        # encode.setGeometry(50, 50, 100, 25)

        self.encode_textbox = QTextEdit(self)
        self.encode_textbox.setGeometry(50, 80, 400, 100)
        self.encode_textbox.setPlaceholderText("Text einfügen, der verschlüsselt werden soll")

        self.encode_button = QPushButton("Verschlüsseln", self)
        self.encode_button.setGeometry(350, 190, 100, 25)
        self.encode_button.clicked.connect(self.encode_text)

        # decode = QLabel("Entschlüsseln", self)
        # decode.setGeometry(50, 250, 100, 25)

        self.warning_run_length_encoding = QLabel("Warnung! Funktioniert nur für\n Buchstabenketten richtig!", self)
        self.warning_run_length_encoding.setGeometry(210, 10, 250, 40)
        self.warning_run_length_encoding.hide()

        self.warning_lempel_ziv_welch = QLabel("Warnung! Funktioniert nur für sehr\n lange Zeichenketten richtig!", self)
        self.warning_lempel_ziv_welch.setGeometry(210, 10, 250, 40)
        self.warning_lempel_ziv_welch.hide()

        self.decode_textbox = QTextEdit(self)
        self.decode_textbox.setGeometry(50, 280, 400, 100)
        self.decode_textbox.setPlaceholderText("Text einfügen, der entschlüsselt werden soll")

        self.decode_button = QPushButton("Entschlüsseln", self)
        self.decode_button.setGeometry(350, 390, 100, 25)
        self.decode_button.clicked.connect(self.decode_text)

    def coding(self):
        if self.menu.currentText() == "Run Length Encoding":
            self.warning_run_length_encoding.show()
        else:
            self.warning_run_length_encoding.hide()

        if self.menu.currentText() == "Lempel-Ziv-Welch":
            self.warning_lempel_ziv_welch.show()
        else:
            self.warning_lempel_ziv_welch.hide()

    def encode_text(self):
        if self.menu.currentText() == "Run Length Encoding":
            self.encode_run_length()
        elif self.menu.currentText() == "Lempel-Ziv-Welch":
            self.encode_lempel_ziv_welch()

    def decode_text(self):
        if self.menu.currentText() == "Run Length Encoding":
            self.decode_run_length()
        elif self.menu.currentText() == "Lempel-Ziv-Welch":
            self.decode_lempel_ziv_welch()

    def encode_run_length(self):
        text = self.encode_textbox.toPlainText() + '|'
        counter = 1
        result = ''
        for i in range(len(text)):
            if text[i] != '|' and text[i] != text[i+1]:
                result += text[i] + str(counter)
                counter = 1
            elif text[i] != '|' and text[i] == text[i+1]:
                counter += 1
        self.decode_textbox.setPlainText(result)

    def decode_run_length(self):
        text = self.decode_textbox.toPlainText() + '|'
        x = 1
        number = ''
        result = ''
        for i in range(len(text)):
            if text[i].isdigit() is False and text[i] != '|':
                while text[i+x].isdigit():
                    number += text[i+x]
                    x += 1
                x = 1
                result += text[i] * int(number)
                number = ''
                if text[i+x].isdigit() is False:
                    print("Falsches Format")
        self.encode_textbox.setPlainText(result)

    def encode_lempel_ziv_welch(self):
        text = self.encode_textbox.toPlainText() + '|'
        pattern_list = []
        result = ''
        # for i in range(len(text)):
        #     if i+1 in range(len(text)):
        #         next_sign = text[i+1]
        #         combination = text[i] + next_sign
        #         if combination in pattern_list:
        #             result += '<' + str(pattern_list.index(combination)) + '>'
        #             # if i+2 in range(len(text)):
        #             #     pattern_list.append(combination+text[i+2])
        #         else:
        #             pattern_list.append(combination)
        #             result += text[i]
        #             #print(result)
        #     print(result)
        i = 0
        counter = 1
        while i+1 in range(len(text)):
            next_sign = text[i+1]
            combination = text[i] + next_sign
            if combination in pattern_list:
                result += '<' + str(pattern_list.index(combination)) + '>'
                #counter += 1

                #pattern_list.append(combination + text[i+counter])
                i += 2
            else:
                pattern_list.append(combination)
                result += text[i]
                i += 1
        self.decode_textbox.setPlainText(result)

    def decode_lempel_ziv_welch(self):
        text = self.decode_textbox.toPlainText()
        print(text)
