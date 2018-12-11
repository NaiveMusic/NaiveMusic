import sys
from view.mainView import MainWindow_Demo
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainWindow_Demo()
window.show()
sys.exit(app.exec_())