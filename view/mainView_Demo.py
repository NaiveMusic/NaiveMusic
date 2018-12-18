import sys
from PyQt5 import QtCore, QtWidgets

from .trackView_Demo import TrackView_Demo
from .sheetView_Demo import SheetView_Demo
from controller.mainController import MainController




class MainView_Demo(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('Demo2')
        self.resize(800, 600)
        self.mc = MainController()
        self.mc.setCurView(self)

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
        self.play.clicked.connect(self.playAll)
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
        self.addTrack()

    # view不要自己调用update！
    def update(self):
        # sheetview update
        self.sheet.setPlainText(self.mc.getCurTrack().demoNotes)

        # trackView update
        for view in self.trackViews.values():
            self.grid.removeWidget(view)

        # filiter deleted tracks
        self.trackViews = {
            i: self.trackViews[i]
            for i in self.trackViews
            if isinstance(self.trackViews[i], TrackView_Demo) and self.trackViews[i].deleted == False
        }

        for i, view in enumerate(self.trackViews.values()):  # may not stable, sort needed
            self.grid.addWidget(view, i + 2, 0, 1, 6)

    # 添加track
    def addTrack(self):
        trackID = self.mc.addTrack(inst=0, vel=100)
        print('track {} added'.format(trackID))
        trackView = TrackView_Demo(self.mc, trackID)
        self.trackViews[trackID] = trackView
        trackView.trackVel.valueChanged.connect(self.lcd.display)
        self.mc.setCurTrack(trackID)

    # 设置bpm
    def setBPM(self):
        self.mc.setBPM(self.bpm.value())

    # 全局播放
    def playAll(self):
        self.mc.playAll()

    # 更新track的text
    def updateTrack(self):
        text = self.sheet.toPlainText()
        self.mc.getCurTrack().demoNotes = text
        self.trackViews[self.mc.getCurTrackID()].trackShow.setText(text)