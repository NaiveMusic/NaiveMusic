import sys
from PyQt5 import QtCore, QtWidgets
from model.const import *
from controller.mainController import MainController


class TrackView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
