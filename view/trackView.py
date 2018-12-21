import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *
from controller.mainController import MainController

class InstrumentView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.instrumentID = None
        hbox = QHBoxLayout()
        hbox.addWidget(self.instrumentLabel)
        hbox.addWidget(self.cancelButton)
        hbox.addStretch(1)
        self.setLayout(hbox)

    def initUI(self):
        self.instrumentLabel = QLabel('Default', self)
        self.instrumentLabel.setMinimumSize(50, 50)
        self.cancelButton = QPushButton('', self)
        self.cancelButton.setMinimumSize(10, 10)
        self.cancelButton.setIcon(QIcon('view/Icons/ui/cancel.svg'))
        self.cancelButton.clicked.connect(self.deleteInstrument)


    def deleteInstrument(self):
        self.deleteLater()

class TrackView(QWidget):
    def __init__(self, trackController, trackID, sheet):
        super().__init__()
        self.sheet = sheet
        self.trackID = trackID
        self.trackController = trackController
        self.value = 0
        self.isMute = True
        self.instrument = None
        self.initUI()
    
    # 初始化单轨的交互界面
    def initUI(self):
        self.setMinimumSize(70, 70)

        self.initInstrumentUI()
        self.initVolumeUI()
        self.initTrackUI()

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.volume)
        hbox.addWidget(self.vAdjuster)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.instrumentButton)
        vbox.addLayout(hbox)
        vbox2 = QVBoxLayout()
        vbox2.setContentsMargins(0, 0, 0, 0)
        vbox2.addWidget(self.track)
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

    # 初始化音轨区域
    def initTrackUI(self):
        self.track = QPushButton('track', self)
        self.track.setMinimumSize(1160, 120)
        # self.track.clicked.connect(self.playTrack)


    # 轨道乐器图标
    def initInstrumentUI(self):
        self.instrumentButton = QPushButton('', self)
        self.instrumentButton.setMinimumSize(80, 80)
        self.instrumentButton.setCheckable(True)  
        self.instrumentButton.setIcon(QIcon('view/Icons/instrument/default.svg'))

    def bindInstrument(self, icon, instID):
        self.instrumentButton.setIcon(icon)
        self.trackController.curFile.getTrack(self.trackID).setInst(instID)
        

    # 音量图标界面初始化函数
    def initVolumeUI(self):
        # 音量按钮，点击效果静音，随着音量的变化，图标进行变化
        self.volume = QPushButton('', self)
        self.volume.setMinimumSize(30, 30)
        self.volume.setIcon(QIcon('view/Icons/volume/midVolume.svg'))
        self.currentVIcon = QIcon('view/Icons/volume/midVolume.svg')
        self.volume.clicked.connect(self.muteTrack)

        # 音量滑动条
        self.vAdjuster = QSlider(Qt.Horizontal, self)
        self.vAdjuster.setMinimumSize(50, 30)
        self.vAdjuster.setMaximum(100)
        self.vAdjuster.setValue(50)
        self.vAdjuster.valueChanged[int].connect(self.changeValue)


    # 音量滑动条连接函数         
    def changeValue(self, value):

        self.value = value
        self.trackController.curFile.getTrack(self.trackID).setVel(self.value)
        if value == 0:
            self.volume.setIcon(QIcon('view/Icons/volume/zeroVolume.svg'))
            self.currentVIcon = QIcon('view/Icons/volume/zeroVolume.svg')
        elif value > 0 and value <= 30:
            self.volume.setIcon(QIcon('view/Icons/volume/minVolume.svg'))
            self.currentVIcon = QIcon('view/Icons/volume/minVolume.svg')
        elif value > 30 and value <= 80:
            self.volume.setIcon(QIcon('view/Icons/volume/midVolume.svg'))
            self.currentVIcon = QIcon('view/Icons/volume/midVolume.svg')
        else:
            self.volume.setIcon(QIcon('view/Icons/volume/maxVolume.svg'))
            self.currentVIcon = QIcon('view/Icons/volume/maxVolume.svg')

    # 音轨静音效果
    def muteTrack(self):
        # 
        if self.isMute: 
            self.volume.setIcon(QIcon('view/Icons/volume/mute.svg'))
            self.value = 0
            self.isMute = False
        else:
            self.volume.setIcon(self.currentVIcon)
            self.value = self.vAdjuster.value()
            self.isMute = True

        self.trackController.curFile.getTrack(self.trackID).setVel(self.value)


    def selectTrack(self):
        self.trackController.setCurTrack(self.trackID)
        self.sheet.setPlainText(self.trackController.curTrack.demoNotes)

    def deleteTrack(self):
        # 删除音轨暂时不需要实现
        pass

'''

class TrackView_Demo(QtWidgets.QWidget):
    def __init__(self, mc, trackID):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.mc = mc
        self.trackID = trackID

        # 单轨播放
        self.trackPlay = QtWidgets.QPushButton()
        self.trackPlay.setText('Play')
        self.trackPlay.clicked.connect(self.playTrack)
        self.layout.addWidget(self.trackPlay)

        # 显示框
        self.trackShow = QtWidgets.QTextBrowser()
        self.layout.addWidget(self.trackShow)

        # 切换到当前track
        self.trackSwitch = QtWidgets.QPushButton()
        self.trackSwitch.setText('Switch to {}'.format(self.trackID))
        self.trackSwitch.setObjectName('switch ' + str(self.trackID))
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
        self.trackDel.setObjectName('del ' + str(self.trackID))
        # self.trackDel.clicked.connect(self.delTrack)
        self.layout.addWidget(self.trackDel)

    # 单轨播放
    def playTrack(self):
        self.mc.playTrack(self.trackID)

    def changeInst(self):
        self.mc.curFile.getTrack(self.trackID).setInst(self.trackInst.currentIndex())

    def changeVel(self):
        self.mc.curFile.getTrack(self.trackID).setVel(self.trackVel.value())

    def delTrack(self):
        self.hide()
        self.deleteLater()
'''
