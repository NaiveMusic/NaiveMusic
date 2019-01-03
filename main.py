import sys
from view.mainView import MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
app.setStyleSheet("""
            QMainWindow {
                background-color: rgb(64, 64, 64);
            }""")

window = MainWindow()

window.show()
sys.exit(app.exec_())
