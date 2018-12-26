import sys
from PyQt5 import QtCore, QtWidgets
from model.const import *
from controller.mainController import MainController


class TrackView_Demo(QtWidgets.QWidget):
    def __init__(self, mc, trackID):
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.mc = mc
        self.trackID = trackID
        self.deleted = False

        # 单轨播放
        self.trackPlay = QtWidgets.QPushButton()
        self.trackPlay.setText('Play')
        self.trackPlay.clicked.connect(self.playTrack)
        self.layout.addWidget(self.trackPlay)

        # 显示框
        self.trackEditDemo = QtWidgets.QTextEdit()
        self.trackEditDemo.textChanged.connect(self.updateTrack)
        self.layout.addWidget(self.trackEditDemo)

        # 切换到当前track
        self.trackSwitch = QtWidgets.QPushButton()
        self.trackSwitch.setText('Switch to {}'.format(self.trackID))
        # self.trackSwitch.setObjectName('switch ' + str(self.trackID))
        self.trackSwitch.clicked.connect(self.switchTrack)
        self.layout.addWidget(self.trackSwitch)

        # 选择乐器
        self.trackInst = QtWidgets.QComboBox()
        self.trackInst.addItems(['{} {}'.format(i, INSTRUMENT[i]) for i in INSTRUMENT])
        self.trackInst.currentIndexChanged.connect(self.changeInst)
        self.layout.addWidget(self.trackInst)

        # 调节音量
        self.trackVel = QtWidgets.QSlider(QtCore.Qt.Vertical)
        self.trackVel.setMaximum(127)
        self.trackVel.setValue(100)
        self.trackVel.valueChanged.connect(self.changeVel)
        self.layout.addWidget(self.trackVel)

        # 删除音轨
        self.trackDel = QtWidgets.QPushButton()
        self.trackDel.setText('Del Track')
        # self.trackDel.setObjectName('del ' + str(self.trackID))
        self.trackDel.clicked.connect(self.delTrack)
        self.layout.addWidget(self.trackDel)

    def switchTrack(self):
        self.mc.setCurTrack(self.trackID)

    def delTrack(self):
        self.deleted = True
        self.deleteLater()
        self.mc.delTrack(self.trackID)

    # 更新track
    def updateTrack(self):
        text = self.trackEditDemo.toPlainText()
        self.mc.getTrack(self.trackID).demoNotes = text

    # 单轨播放
    def playTrack(self):
        self.mc.playTrackDemo(self.trackID)

    def changeInst(self):
        self.mc.setTrackInst(self.trackID, self.trackInst.currentIndex())

    def changeVel(self):
        self.mc.setTrackVel(self.trackID, self.trackVel.value())
