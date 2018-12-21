import sys
from PyQt5 import QtCore, QtWidgets

from .trackView import TrackView
from .sheetView import SheetView
from controller.mainController import MainController


class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()