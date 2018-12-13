import sys
from PyQt5 import QtCore, QtWidgets
from model.const import *

from controller.mainController import MainController


class SheetView():
    def __init__(self):
        pass


class SheetView_Demo(QtWidgets.QPlainTextEdit):
    def __init__(self):
        QtWidgets.QPlainTextEdit.__init__(self)
