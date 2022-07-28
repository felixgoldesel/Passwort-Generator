import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QHBoxLayout, QPushButton


def window():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()

    windows.resize(500, 500)
    windows.move(200, 200)

    windows.setWindowTitle('Passwortgenerator')
    windows.setWindowIcon(QtGui.QIcon('weihnaxfeierliebe.png'))

    layout = QHBoxLayout()
    button = QPushButton("Klick mich!")
    layout.addWidget(button)
    windows.setLayout(layout)

    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()








