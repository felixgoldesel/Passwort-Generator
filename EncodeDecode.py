from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QComboBox, QPushButton


class EncodeDecode(QWidget):
    def __init__(self):
        super().__init__()

        menu = QComboBox(self)
        menu.setGeometry(50, 20, 150, 25)
        menu.addItem("MD5")
        menu.addItem("kp")

        encode = QLabel("Verschlüsseln", self)
        encode.setGeometry(50, 50, 100, 25)

        self.encode_textbox = QTextEdit(self)
        self.encode_textbox.setGeometry(50, 80, 400, 100)

        self.encode_button = QPushButton("Verschlüsseln", self)
        self.encode_button.setGeometry(350, 190, 100, 25)

        decode = QLabel("Entschlüsseln", self)
        decode.setGeometry(50, 250, 100, 25)

        self.decode_textbox = QTextEdit(self)
        self.decode_textbox.setGeometry(50, 280, 400, 100)

        self.decode_button = QPushButton("Entschlüsseln", self)
        self.decode_button.setGeometry(350, 390, 100, 25)