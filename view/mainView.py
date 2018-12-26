import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .trackView import TrackView, InstrumentView
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
        self.vbox.addWidget(InstrumentView())
        self.vbox.addWidget(self.toolBar)
        self.vbox.addWidget(self.tracklist[0])
        for track in self.tracklist:
            self.vbox.addWidget(track)
        self.vbox.addStretch(0)
        self.trackRegion = QWidget(self)
        self.trackRegion.setGeometry(QRect(100, 100, 1280, 750))
        self.trackRegion.setLayout(self.vbox)
        self.setWindowTitle('Naive Music')
        self.resize(1920, 1080)


    def initUI(self):
        self.initSheetUI()
        self.initTrackUI()
        self.initToolUI()

    def initToolUI(self):
        self.menu = Menu(self.mc)
        self.toolBar = ToolBar(self.mc, self.menu)
        pass

    def initSheetUI(self):
        self.sheet = SheetView_Demo()
        self.sheet.textChanged.connect(self.updateTrack)

    def initTrackUI(self):
        self.mc = MainController()
        self.tracklist = []
        for i in range(2):
            trackID = self.mc.addTrack(inst=0, vel=100)
            self.tracklist.append(TrackView(self.mc, trackID, self.sheet))


    def addTrack(self):

        pass

    def updateTrack(self):
        text = self.sheet.toPlainText()
        self.mc._curTrack.demoNotes = text

