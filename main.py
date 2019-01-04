import sys
from view.mainView import MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
app.setStyleSheet("""
            QMainWindow {
                background-color: rgb(64, 64, 64);
                border-style: outset;
                border-width: 5px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
            }""")

window = MainWindow()
window.show()
sys.exit(app.exec_())
