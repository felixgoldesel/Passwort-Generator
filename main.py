import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QCheckBox


def window():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()

    #windows.resize(500, 500)
    #windows.move(200, 200)
    windows.setGeometry(200, 200, 500, 500)

    windows.setWindowTitle('Passwortgenerator')
    windows.setWindowIcon(QtGui.QIcon('generator.jpeg'))

    layout = QHBoxLayout()
    button = QPushButton("Klick mich!")
    layout.addWidget(button)
    windows.setLayout(layout)

    checkbox1 = QCheckBox("Check 1")
    checkbox1.setChecked(False)
    checkbox1.stateChanged.connect()
    layout.addWidget(checkbox1)



    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()








