import string
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox, QLineEdit, QLabel, QTextEdit, \
    QTabWidget
import random

from EncodeDecode import EncodeDecode
from Generator import Generator


class Fenster(QTabWidget):
    def __init__(self):
        super().__init__()
        #self.init_window()

    #def init_window(self):

        width = 500
        height = 500

        self.setFixedSize(width, height)
        self.setWindowTitle("Passwortgenerator")
        self.setWindowIcon(QtGui.QIcon("generator.jpeg"))

        self.tab1 = Generator()
        self.tab2 = EncodeDecode()

        self.addTab(self.tab1, "Generator")
        self.addTab(self.tab2, "Kodieren/Dekodieren")

        self.show()
