import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .trackView import TrackView, InstrumentView
from .sheetView import SheetView_Demo
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
            trackID = self.mc.curFile.addTrack(inst=0, vel=100)
            self.tracklist.append(TrackView(self.mc, trackID, self.sheet))

    def playTrack(self):
        self.mc.curFile.setBPM(100)
        if self.isPlay:
            self.playButton.setIcon(QIcon('view/Icons/ui/pause.svg'))
            self.isPlay = False
        else: 
            self.playButton.setIcon(QIcon('view/Icons/ui/play.svg'))
            self.isPlay = True

        self.mc.playTrack(self.mc.curTrackID)

    def playAll(self):
        self.mc.playAll()

    def addTrack(self):

        pass

    def updateTrack(self):
        text = self.sheet.toPlainText()
        self.mc.curTrack.demoNotes = text
'''
class MainWindow_Demo(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('Demo2')
        self.resize(800, 600)
        self.mc = MainController()

        # 居中显示
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(100, 100, 600, 400))
        self.grid = QtWidgets.QGridLayout(self.widget)
        self.widget.setLayout(self.grid)

        # Sheet
        self.sheet = SheetView_Demo()
        self.sheet.textChanged.connect(self.updateTrack)
        self.grid.addWidget(self.sheet, 0, 0, 1, 6)

        # 全局播放
        self.play = QtWidgets.QPushButton()
        self.play.setText('Play All')
        self.play.clicked.connect(self.playAllButton)
        self.grid.addWidget(self.play, 1, 0)

        # bpm label
        self.label = QtWidgets.QLabel('BPM')
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label, 1, 1)

        # bpm
        self.bpm = QtWidgets.QSpinBox()
        self.bpm.setMaximum(200)
        self.bpm.setValue(120)
        self.bpm.valueChanged.connect(self.setBPM)
        self.grid.addWidget(self.bpm, 1, 2)

        # vel label
        self.label2 = QtWidgets.QLabel('Vel')
        self.label2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label2, 1, 3)

        # 显示音量
        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.display('100')
        self.grid.addWidget(self.lcd, 1, 4)

        # '添加音轨'按钮
        self.trackAdd = QtWidgets.QPushButton()
        self.trackAdd.setText('Add Track')
        self.trackAdd.clicked.connect(self.addTrack)
        self.grid.addWidget(self.trackAdd, 1, 5)

        # 添加音轨view
        self.trackViews = {}
        self.switchButtons = QtWidgets.QButtonGroup()
        self.switchButtons.buttonClicked.connect(self.switchTrack)

        self.deleteButtons = QtWidgets.QButtonGroup()
        self.deleteButtons.buttonClicked.connect(self.delTrack)
        self.addTrack()

    # 添加track
    def addTrack(self):
        trackID = self.mc.curFile.addTrack(inst=0, vel=100)
        print('track {} added'.format(trackID))

        curTrackNum = self.mc.curFile.getLen()
        trackView = TrackView_Demo(self.mc, trackID)

        self.trackViews[trackID] = trackView
        self.switchButtons.addButton(trackView.trackSwitch)
        self.deleteButtons.addButton(trackView.trackDel)

        trackView.trackVel.valueChanged.connect(self.lcd.display)

        self.mc.setCurTrack(trackID)

        self.grid.addWidget(trackView, curTrackNum + 2, 0, 1, 6)
        self.switchTrack(trackView.trackSwitch)

    # 设置bpm
    def setBPM(self):
        self.mc.curFile.setBPM(self.bpm.value())

    # 全局播放
    def playAllButton(self):
        self.mc.playAll()

    # 切换track
    def switchTrack(self, button):
        trackID = button.objectName()
        trackID = int(trackID.split()[1])
        self.mc.setCurTrack(trackID)
        self.sheet.setPlainText(self.mc.curTrack.demoNotes)

    # 删除track
    def delTrack(self, button):
        trackID = button.objectName()
        trackID = int(trackID.split()[1])
        print('track {} deleted'.format(trackID))

        for view in self.trackViews.values():
            self.grid.removeWidget(view)
        trackView = self.trackViews.pop(trackID)
        for i, view in enumerate(self.trackViews.values()):  # may not stable
            self.grid.addWidget(view, i + 2, 0, 1, 6)

        self.switchButtons.removeButton(trackView.trackSwitch)
        self.deleteButtons.removeButton(trackView.trackDel)
        trackView.delTrack()
        self.mc.curFile.delTrack(trackID)

    # 更新track的text
    def updateTrack(self):
        text = self.sheet.toPlainText()
        self.mc.curTrack.demoNotes = text
        self.trackViews[self.mc.curTrackID].trackShow.setText(text)
'''

