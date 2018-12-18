import sys
from view.mainView_Demo import MainView_Demo
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainView_Demo()
window.show()
sys.exit(app.exec_())