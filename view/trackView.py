import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *
from controller.mainController import MainController


class TrackView(QWidget):
    def __init__(self, trackController, trackID, sheet, instc):
        super().__init__()
        self.sheet = sheet
        self.trackID = trackID
        self.trackController = trackController
        self.instc = instc
        self.value = 0
        self.isMute = True
        self.instrument = None
        self.initUI()
    
    def initUI(self):
        '''
            Initialize a single track, composed of:
                an instruemnt icon;
                a volume icon;
                a volume ajuster;
                a track button;

        '''
        self.setMinimumSize(1920, 105)

        self.initInstrumentUI()
        self.initVolumeUI()
        self.initTrackUI()

 
    def initTrackUI(self):
        '''
            Initialize track button, select a track via click

        '''
        self.track = QPushButton('track {0}'.format(self.trackID), self)
        self.track.setGeometry(QRect(90, 5, 1800, 100))
        self.track.clicked.connect(self.selectTrack)


    def initInstrumentUI(self):
        '''
            Initialize instrument icon, bind an instrument via click

        '''
        self.instrumentButton = QPushButton('', self)
        self.instrumentButton.setGeometry(QRect(0, 5, 75, 75))
        self.instrumentButton.setStyleSheet("""
            .QPushButton {
                    width: 20px;
                    height: 20px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(255, 255, 111);
                    image: url('view/Icons/instrument/plug.svg');
                } """)  
        self.instrumentButton.clicked.connect(self.bindInstrument)



    def bindInstrument(self):
        '''
            Bind selected instrument to track

        '''
        if not self.instc.getCurInstID(): # when no instrument selected
            warnDialog = QDialog(self)
            warnLabel = QLabel('Please select an instrument first !', warnDialog)
            warnLabel.move(100, 100)
            warnDialog.setWindowTitle("Alert")
            warnDialog.resize(500, 200)
            warnDialog.setWindowModality(Qt.ApplicationModal)
            warnDialog.exec_()

        else:
            self.trackController.setTrackInst(self.trackID, self.instc.getCurInstID())
            self.instrumentButton.setStyleSheet(self.instc.getCurInstStyle())

        


    def initVolumeUI(self):
        '''
            Volume UI initialization, including a volume icon and a slider

        '''
        self.volume = QPushButton('', self)
        self.volume.setGeometry(QRect(0, 85, 20, 20))
        self.volume.setIcon(QIcon('view/Icons/volume/midVolume.svg'))
        self.currentVIcon = QIcon('view/Icons/volume/midVolume.svg')
        self.volume.clicked.connect(self.muteTrack)

        self.vAdjuster = QSlider(Qt.Horizontal, self)
        self.vAdjuster.setGeometry(QRect(25, 85, 50, 20))
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
        self.updateSheet()
        print('Track {0} selected !'.format(self.trackID))

    def updateSheet(self):
        # TODO
        pass

    def updateTrack(self):
        if self.mc.getTrack(self.trackID) is not None:
            # TODO update itself
            pass

    def deleteTrack(self):
        ''''
            Delete a track

        '''
        self.deleteLater()
        




class TrackContainer(QWidget):
    def __init__(self, mc, sheet, instc):
        super().__init__()
        self.mc = mc
        self.sheet = sheet
        self.instc = instc
        self.tracklist = {}
        self.init()
        self.initUI()

    def init(self):
        self.mc.register(self)
        for i in range(4):
            trackID = self.mc.addTrack(inst=0, vel=80)
            self.tracklist[trackID] = TrackView(self.mc, trackID, self.sheet, self.instc)


    def initUI(self):
        trackRegion = QWidget()
        self.trackLayout = QVBoxLayout()
        for trackID, track in self.tracklist.items():
            self.trackLayout.addWidget(track)
        self.trackLayout.addStretch(0)
        trackRegion.setLayout(self.trackLayout)
        self.trackScroll = QScrollArea()
        self.trackScroll.setWidget(trackRegion)
        self.trackScroll.setFixedHeight(300)

    def update(self):
        #### Update from base controller todo
        trackRegion = QWidget()
        trackRegion.setLayout(self.trackLayout)
        self.trackScroll.setWidget(trackRegion)

    def delTrack(self):
        trackID = self.mc.getCurTrackID()
        self.mc.delTrack(trackID)
        self.tracklist[trackID].deleteTrack()
        self.trackLayout.removeWidget(self.tracklist[trackID])
        del self.tracklist[trackID]

        self.update()

        print("Track {0} is deleted !".format(trackID))

    def addTrack(self):
        trackID = self.mc.addTrack(inst=0, vel=80)
        self.tracklist[trackID] = TrackView(self.mc, trackID, self.sheet, self.instc)
        self.trackLayout.insertWidget(self.trackLayout.count()-1, self.tracklist[trackID])
        self.update()

