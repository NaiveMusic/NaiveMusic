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
        self.track.clicked.connect(self.selectTrack)


    # 轨道乐器图标
    def initInstrumentUI(self):
        self.instrumentButton = QPushButton('', self)
        self.instrumentButton.setMinimumSize(80, 80)
        self.instrumentButton.setCheckable(True)  
        self.instrumentButton.setIcon(QIcon('view/Icons/instrument/default.svg'))

    def bindInstrument(self, icon, instID):
        '''
            Set the instrument of track

            Args: 
                icon, QICON type, icon of the instrument
                instID, int type, id of the instrument

        '''

        self.instrumentButton.setIcon(icon)
        self.trackController.curFile.getTrack(self.trackID).setInst(instID)
        


    def initVolumeUI(self):
        '''
            Volume UI initialization, including a volume icon and a slider

        '''
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


  
    def changeValue(self, value):
        '''
            Update the volume of track

            Args: value, float type, gained from slider, no need to set manually

        '''       
        # change track volume, updated by trackController 
        self.value = value
        self.trackController.setTrackVel(self.trackID, self.value)

        # UI interaction effect, allow volume icon change dynamically
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


    def muteTrack(self):
        '''
            Mute track, different from directly set the volume of track to zero

            that previous volume of the track can be restored
        
        '''
        if self.isMute: # is to mute
            self.volume.setIcon(QIcon('view/Icons/volume/mute.svg'))
            self.value = 0
            self.isMute = False

        else: # restore previous track volume
            self.volume.setIcon(self.currentVIcon)
            self.value = self.vAdjuster.value()
            self.isMute = True

        self.trackController.setTrackVel(self.trackID, self.value) # update volume


    def selectTrack(self):
        '''
            In mainview, set the current track editable

        '''
        self.trackController.setCurTrack(self.trackID)
        self.sheet.setPlainText(self.trackController.curTrack.demoNotes)

    def deleteTrack(self):
        ''''
            Delete a track

        '''
        pass

