import sys
from view.mainView import MainView
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainView()
window.show()
sys.exit(app.exec_())