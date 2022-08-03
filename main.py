import sys
from PyQt5 import QtWidgets
from Fenster import Fenster

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Fenster()
    sys.exit(app.exec_())







