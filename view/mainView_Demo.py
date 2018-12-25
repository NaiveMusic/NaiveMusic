from PyQt5 import QtGui, QtCore, QtWidgets

from .trackView_Demo import TrackView_Demo
from .sheetView_Demo import SheetView_Demo
from controller.mainController import MainController


class MainView_Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NaiveMusic_Demo')
        self.resize(800, 600)
        self.mc = MainController()
        self.mc.setCurView(self)

        # 窗口图标
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/global/src/global/logo.png"), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # 居中显示
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)
        self.grid = QtWidgets.QGridLayout(self.widget)
        self.widget.setLayout(self.grid)

        # Sheet
        self.sheet = SheetView_Demo(self.mc)
        self.grid.addWidget(self.sheet, 0, 0, 1, 7)

        # 全局播放
        self.play = QtWidgets.QPushButton()
        self.play.setText('Play All')
        self.play.clicked.connect(self.playAll)
        self.grid.addWidget(self.play, 1, 0)

        # 播放停止
        self.pause = QtWidgets.QPushButton()
        self.pause.setText('Pause')
        self.pause.clicked.connect(self.pauseAll)
        self.grid.addWidget(self.pause, 1, 1)

        # bpm label
        self.label = QtWidgets.QLabel('BPM')
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label, 1, 2)

        # bpm
        self.bpm = QtWidgets.QSpinBox()
        self.bpm.setMaximum(200)
        self.bpm.setValue(120)
        self.bpm.valueChanged.connect(self.setBPM)
        self.grid.addWidget(self.bpm, 1, 3)

        # vel label
        self.label2 = QtWidgets.QLabel('Vel')
        self.label2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label2, 1, 4)

        # 显示音量
        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.display('100')
        self.grid.addWidget(self.lcd, 1, 5)

        # '添加音轨'按钮
        self.trackAdd = QtWidgets.QPushButton()
        self.trackAdd.setText('Add Track')
        self.trackAdd.clicked.connect(self.addTrack)
        self.grid.addWidget(self.trackAdd, 1, 6)

        # 添加音轨view
        self.trackViews = {}
        self.addTrack()

    # view不要自己调用update！
    def update(self):
        # sheetview update
        # self.sheet.setPlainText(self.mc.getCurTrack().demoNotes)

        # trackView update
        for view in self.trackViews.values():
            self.grid.removeWidget(view)

        # filiter deleted tracks
        self.trackViews = {
            i: self.trackViews[i]
            for i in self.trackViews
            if isinstance(self.trackViews[i], TrackView_Demo)
            and self.trackViews[i].deleted == False
        }

        for i, view in enumerate(
                self.trackViews.values()):  # may not stable, sort needed
            self.grid.addWidget(view, i + 2, 0, 1, 7)

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
        self.mc.playAllDemo()

    def pauseAll(self):
        self.mc.pauseAllDemo()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self, 'Message', "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
