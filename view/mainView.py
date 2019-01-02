import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .trackView import TrackView, TrackContainer
from .InstrumentView import InstrumentView, InstrumentContainer
from .sheetView_Demo import SheetView_Demo
from .toolBar import ToolBar
from .menuView import Menu
from controller.mainController import MainController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.isPlay = True

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(0)
        self.vbox.addWidget(self.sheet)
        self.vbox.addWidget(InstrumentContainer(self.mc))
        self.vbox.addWidget(self.toolBar)
        self.vbox.addWidget(self.tc.trackScroll)
        self.vbox.addStretch(0)

        self.mainWidget = QWidget(self)
        self.mainWidget.setLayout(self.vbox)
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle('Naive Music')
        self.resize(1920, 1080)


    def initUI(self):
        self.mc = MainController()
        self.initSheetUI()
        self.initTrackUI()
        self.initToolUI()

    def initToolUI(self):
        self.menu = Menu(self.mc)
        self.toolBar = ToolBar(self.mc, self.menu, self.tc)

    def initSheetUI(self):
        self.sheet = SheetView_Demo(self.mc)

    def initTrackUI(self):
        self.tc = TrackContainer(self.mc, self.sheet)


