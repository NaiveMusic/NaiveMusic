import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .trackView import TrackView, InstrumentView
from .sheetView_Demo import SheetView_Demo
from controller.mainController import MainController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.isPlay = True

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.sheet)
        self.vbox.addWidget(InstrumentView())
        hbox = QHBoxLayout()
        hbox.addWidget(self.playButton)
        hbox.addWidget(self.playAllButton)
        self.vbox.addLayout(hbox)
        self.vbox.addWidget(self.tracklist[0])
        for track in self.tracklist:
            self.vbox.addWidget(track)
        self.trackRegion = QWidget(self)
        self.trackRegion.setGeometry(QRect(100, 100, 1280, 720))
        self.trackRegion.setLayout(self.vbox)
        self.setWindowTitle('Naive Music')
        self.resize(1920, 1080)


    def initUI(self):
        self.initToolUI()
        self.initSheetUI()
        self.initTrackUI()

    def initToolUI(self):
        self.playButton = QPushButton('', self)
        self.playButton.setMinimumSize(80, 80)
        self.playButton.setIcon(QIcon('view/Icons/ui/play.svg'))
        self.playButton.clicked.connect(self.playTrack)

        self.playAllButton = QPushButton('', self)
        self.playAllButton.setMinimumSize(80, 80)
        self.playAllButton.setIcon(QIcon('view/Icons/ui/playAll.svg'))
        self.playAllButton.clicked.connect(self.playAll)

    def initSheetUI(self):
        self.sheet = SheetView_Demo()
        self.sheet.textChanged.connect(self.updateTrack)

    def initTrackUI(self):
        self.mc = MainController()
        self.tracklist = []
        for i in range(2):
            trackID = self.mc.addTrack(inst=0, vel=100)
            self.tracklist.append(TrackView(self.mc, trackID, self.sheet))

    def playTrack(self):
        self.mc.setBPM(100)
        if self.isPlay:
            self.playButton.setIcon(QIcon('view/Icons/ui/pause.svg'))
            self.isPlay = False
        else: 
            self.playButton.setIcon(QIcon('view/Icons/ui/play.svg'))
            self.isPlay = True

        self.mc.playTrack(self.mc._curTrackID)

    def playAll(self):
        self.mc.playAll()

    def addTrack(self):

        pass

    def updateTrack(self):
        text = self.sheet.toPlainText()
        self.mc._curTrack.demoNotes = text

