import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *
from controller.mainController import MainController


class TrackView(QWidget):
    def __init__(self, mc, trackID, sheet, instc):
        super().__init__()
        self.sheet = sheet
        self.trackID = trackID
        self.mc = mc
        self.instc = instc
        self.value = self.mc.getTrackVel(trackID)
        self.isMute = True
        self.instrument = self.mc.getTrackInst(trackID)
        self.initUI()
    
    def initUI(self):
        '''
            Initialize a single track, composed of:
                an instrument icon;
                a volume icon;
                a volume ajuster;
                a track button;

        '''
        self.setObjectName('trackView')
        self.setStyleSheet("""
            .TrackView {
                background-color: transparent;
            }""")
        self.setMinimumSize(1920, 110)
        self.initInstrumentUI()
        self.initVolumeUI()
        self.initTrackUI()

 
    def initTrackUI(self):
        '''
            Initialize track button, select a track via click

        '''
        self.track = QPushButton('track {0}'.format(self.trackID), self)
        self.track.setStyleSheet("""
            .QPushButton {
                    width: 1750px;
                    height: 70px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(224, 224, 224);
                } """)  
        self.track.setGeometry(QRect(90, 5, 1780, 100))
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
                    background-color: rgb(224, 224, 224);
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
            self.mc.setTrackInst(self.trackID, self.instc.getCurInstID())
            self.instrumentButton.setStyleSheet(self.instc.getCurInstStyle())
            self.instrument = self.instc.getCurInstID()
            self.track.setStyleSheet("""
                .QPushButton {
                    width: 1750px;
                    height: 70px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: %s;
                } """%(style(INSTRUMENT[self.instrument])[1]))  

        


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
        self.vAdjuster.setStyleSheet("""
            .QSlider::groove:horizontal {
                border: 0px solid #999999;
                height: 10px;
            }

            .QSlider::handle:horizontal {
                width: 18px;
            }

            .QSlider::add-page:qlineargradient {
                background: lightgrey;
            }

            QSlider::sub-page:qlineargradient {
                background: black;
        }""")
        self.vAdjuster.setGeometry(QRect(25, 85, 50, 20))
        self.vAdjuster.setMaximum(100)
        self.vAdjuster.setValue(self.value)
        self.vAdjuster.valueChanged[int].connect(self.changeValue)


  
    def changeValue(self, value):
        '''
            Update the volume of track

            Args: value, float type, gained from slider, no need to set manually

        '''       
        # change track volume, updated by mc 
        self.value = value
        self.mc.setTrackVel(self.trackID, self.value)

        # UI interaction effect, allow volume icon change dynamically
        if self.value == 0:
            self.volume.setIcon(QIcon('view/Icons/volume/zeroVolume.svg'))
            self.currentVIcon = QIcon('view/Icons/volume/zeroVolume.svg')
        elif self.value > 0 and self.value <= 30:
            self.volume.setIcon(QIcon('view/Icons/volume/minVolume.svg'))
            self.currentVIcon = QIcon('view/Icons/volume/minVolume.svg')
        elif self.value > 30 and self.value <= 80:
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

        self.mc.setTrackVel(self.trackID, self.value) # update volume


    def selectTrack(self):
        '''
            In mainview, set the current track editable

        '''
        self.mc.setCurTrack(self.trackID)
        print('Track {0} selected !'.format(self.trackID))



    def selectDraw(self):
        if self.instrument is None:
            self.track.setStyleSheet("""
                .QPushButton {
                    width: 1750px;
                    height: 70px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                    background-color: rgb(224, 224, 224);
                } """)  
        else:
            self.track.setStyleSheet("""
                .QPushButton {
                    width: 1750px;
                    height: 70px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                    background-color: %s;
                } """%(style(INSTRUMENT[self.instrument])[1]))  


    def update(self):
        if self.instrument is not None:
            self.instrument = self.mc.getTrackInst(self.trackID)
            self.instrumentButton.setStyleSheet(style(INSTRUMENT[self.instrument])[0])
            self.track.setStyleSheet("""
                .QPushButton {
                    width: 1750px;
                    height: 70px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: %s;
                } """%(style(INSTRUMENT[self.instrument])[1]))  
            self.vAdjuster.valueChanged[int].connect(self.changeValue)


    def deleteTrack(self):
        ''''
            Delete a track

        '''
        self.deleteLater()

    def paintEvent(self, evt):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        




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

    def initUI(self):
        self.trackScroll = QScrollArea()
        self.trackScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.trackScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.trackScroll.setFixedHeight(400)
        self.trackScroll.setStyleSheet("""
            .QScrollArea {
                background-color: transparent;
            }""")

    def update(self):
        self.tracklist = {}
        trackLayout = QVBoxLayout()
        for trackID in self.mc.getTrackIDList():
            self.tracklist[trackID] = TrackView(self.mc, trackID, self.sheet, self.instc)
            self.tracklist[trackID].update()
            trackLayout.addWidget(self.tracklist[trackID])
        if self.mc.getCurTrackID() is not None:
            self.tracklist[self.mc.getCurTrackID()].selectDraw()

        trackRegion = QWidget()
        trackRegion.setStyleSheet("""
            .QWidget {
                background-color: transparent;
            }""")
        if len(self.tracklist) != 0:
            trackRegion.setLayout(trackLayout)
        self.trackScroll.setWidget(trackRegion)

    def delTrack(self):
        trackID = self.mc.getCurTrackID()
        self.tracklist[trackID].deleteTrack()
        del self.tracklist[trackID]
        self.mc.delTrack(trackID)

        print("Track {0} is deleted !".format(trackID))

    def addTrack(self):
        trackID = self.mc.addTrack(self.mc.getSelectedInst(), vel=50)
        self.mc.setCurTrack(trackID)
        print("Track {0} is added !".format(trackID))

