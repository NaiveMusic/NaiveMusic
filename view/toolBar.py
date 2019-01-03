#####################################################################################
##
##  author: Siyuan sun
##  github: 
##  
##  This file is a UI part of NaiveMusic software, which is used as a project in 
##  Tsinghua University software engineer class. Feel free to download and check it.
##  
######################################################################################

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *
from controller.mainController import MainController

class ToolBar(QWidget):
    def __init__(self, mc, menu, tc):
        super().__init__()
        '''
            property:
                menu: menu class, deal with outside work
                mc: maincontroller class
                isPlay: bool, controll playbutton state

        '''
        self.menu = menu
        self.mc = mc
        self.tc = tc
        self.isPlay = True
        self.init()
        self.initUI()



    def init(self):
        '''
            Initialize toolbar ui, including:

                playtrack icon: play the selected track
                playall icon: play all track together
                pause icon: pause
                BPM setting: set global BPM
                global volume: set global volume
                menu icon: menu, save, load .etc

            No args required
        '''
        self.playButton = QPushButton('', self)
        self.playButton.setStyleSheet("""
            .QPushButton {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/ui/play.svg');
            } """)
        self.playButton.clicked.connect(self.playTrack)


        self.playAllButton = QPushButton('', self)
        self.playAllButton.setStyleSheet("""
            .QPushButton {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/ui/playAll.svg');
            } """)
        self.playAllButton.clicked.connect(self.playAll)


        self.stopButton = QPushButton('', self)
        self.stopButton.setStyleSheet("""
            .QPushButton {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/ui/stop.svg');
            } """)
        self.stopButton.clicked.connect(self.stop)


        self.bpm = QLabel('BPM', self)
        self.bpm.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.bpm.setStyleSheet("""
            .QLabel {
                width: 30px;
                height: 10px;
                border-style: outset;
                border-width: 2px;
                border-radius: 5px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(111, 255, 255)

            }""")



        self.bpmBox = QSpinBox()
        self.bpmBox.setAlignment(Qt.AlignRight)
        self.bpmBox.setMaximum(600)
        self.bpmBox.setValue(120)
        self.bpmBox.valueChanged.connect(self.setBPM)
        self.bpmBox.setStyleSheet("""
            .QSpinBox {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 5px;
                border-color: beige;
                background-color: rgb(111, 255, 255)

            }""")


        self.volume = QLabel('Volume', self)
        self.volume.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.volume.setStyleSheet("""
            .QLabel {
                width: 30px;
                height: 10px;
                border-style: outset;
                border-width: 2px;
                border-radius: 5px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(111, 255, 255)

            }""")

        self.volAdjuster = QSpinBox()
        self.volAdjuster.setAlignment(Qt.AlignRight)
        self.volAdjuster.setMaximum(100)
        self.volAdjuster.setValue(50)
        self.volAdjuster.valueChanged.connect(self.setBPM)
        self.volAdjuster.setStyleSheet("""
            .QSpinBox {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 5px;
                border-color: beige;
                background-color: rgb(111, 255, 255)

            }""")

        self.addButton = QPushButton('', self)
        self.addButton.setStyleSheet("""
            .QPushButton {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/ui/addTrack.svg');
            } """)
        self.addButton.clicked.connect(self.addTrack)

        self.delButton = QPushButton('', self)
        self.delButton.setStyleSheet("""
            .QPushButton {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/ui/delTrack.svg');
            } """)
        self.delButton.clicked.connect(self.delTrack)

    def initUI(self):
        '''
            Initialize the layout of tool bar

        '''
        hbox = QHBoxLayout()
        hbox.addWidget(self.bpm)
        hbox.addWidget(self.bpmBox)
        hbox.addStretch(0)
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.playButton)
        hbox.addWidget(self.playAllButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.delButton)
        hbox.addWidget(self.menu)
        hbox.addStretch(0)
        hbox.addWidget(self.volume)
        hbox.addWidget(self.volAdjuster)
        self.setLayout(hbox)


    def playTrack(self):
        if self.isPlay:
            self.playButton.setStyleSheet("""
                .QPushButton {
                    width: 30px;
                    height: 30px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(255, 255, 111);
                    image: url('view/Icons/ui/pause.svg');
                } """)
            self.isPlay = False
            self.pause()
            print('Track {0} now paused. '.format(self.mc.getCurTrackID()))

        else: 
            self.playButton.setStyleSheet("""
            .QPushButton {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/ui/play.svg');
            } """)
            self.isPlay = True
            self.mc.playTrackDemo(self.mc.getCurTrackID())
            print('Track {0} is playing. '.format(self.mc.getCurTrackID()))

    def playAll(self):

        self.mc.playAll()
        pass

    def pause(self):

        # TODO
        pass

    def stop(self):
        self.mc.pauseAll()
        # TODO 

    def changeVol(self):
        pass

    def setBPM(self):
        self.mc.setBPM(self.bpmBox.value())

        # TODO

    def addTrack(self):
        self.tc.addTrack()

    def delTrack(self):
        self.tc.delTrack()




