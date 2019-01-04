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
        self.isPlay = False
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
                background-color: rgb(205, 225, 209);
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
                background-color: rgb(205, 225, 209);
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
                background-color: rgb(205, 225, 209);
                image: url('view/Icons/ui/pauseAll.svg');
            } """)
        self.stopButton.clicked.connect(self.stop)


        self.bpm = QLabel('BPM', self)
        self.bpm.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.bpm.setStyleSheet("""
            .QLabel {
                font: 25px Verdana;
                font-weight: bold;
                color: white;

            }""")



        self.bpmBox = QSpinBox()
        self.bpmBox.setAlignment(Qt.AlignRight)
        self.bpmBox.setMaximum(600)
        self.bpmBox.setValue(120)
        self.bpmBox.valueChanged.connect(self.setBPM)
        self.bpmBox.setStyleSheet("""
            .QSpinBox {
                width: 70px;
                height: 40px;
                border-style: outset;
                border-width: 2px;
                border-radius: 5px;
                border-color: beige;
                font: 20px Verdana;
                font-weight: bold;
                color: black;
            }""")


        self.volume = QLabel('VOL', self)
        self.volume.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.volume.setStyleSheet("""
            .QLabel {
                font: 25px Verdana;
                font-weight: bold;
                color: white;

            }""")

        self.volAdjuster = QSpinBox()
        self.volAdjuster.setAlignment(Qt.AlignRight)
        self.volAdjuster.setMaximum(100)
        self.volAdjuster.setValue(50)
        self.volAdjuster.valueChanged.connect(self.setBPM)
        self.volAdjuster.setStyleSheet("""
            .QSpinBox {
                width: 70px;
                height: 40px;
                border-style: outset;
                border-width: 2px;
                border-radius: 5px;
                border-color: beige;
                font: 20px Verdana;
                font-weight: bold;
                color: black;
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
                background-color: rgb(205, 225, 209);
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
                background-color: rgb(205, 225, 209);
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
            pass
            # self.playButton.setStyleSheet("""
            #     .QPushButton {
            #         width: 30px;
            #         height: 30px;
            #         border-style: outset;
            #         border-width: 2px;
            #         border-radius: 10px;
            #         border-color: beige;
            #         padding: 15px;
            #         background-color: rgb(205, 225, 209);
            #         image: url('view/Icons/ui/play.svg');
            #     } """)
            # self.isPlay = False
            # self.pause()
            # print('Track {0} now paused. '.format(self.mc.getCurTrackID()))

        else:
            if self.mc.getCurTrackID() is None:
                self.alert("Please select a track to play !")
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
                    background-color: rgb(205, 225, 209);
                    image: url('view/Icons/ui/play.svg');
                } """)
                # self.isPlay = True
                self.mc.playTrack(self.mc.getCurTrackID())
                print('Track {0} is playing. '.format(self.mc.getCurTrackID()))

    def playAll(self):
        if self.isPlay:
            pass
            # self.playAllButton.setStyleSheet("""
            #     .QPushButton {
            #         width: 30px;
            #         height: 30px;
            #         border-style: outset;
            #         border-width: 2px;
            #         border-radius: 10px;
            #         border-color: beige;
            #         padding: 15px;
            #         background-color: rgb(205, 225, 209);
            #         image: url('view/Icons/ui/playAll.svg');
            #     } """)
            # self.isPlay = False
            # self.pause()
            # print('All paused. ')

        else:
            if self.mc.getTrackNum() == 0:
                self.alert("There is no track added !")
            else:
                self.playAllButton.setStyleSheet("""
                .QPushButton {
                    width: 30px;
                    height: 30px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(205, 225, 209);
                    image: url('view/Icons/ui/playAll.svg');
                } """)
                # self.isPlay = True
                self.mc.playAll()
                print('All are playing. ')

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

    def addTrack(self):
        if self.mc.getTrackNum() >= MAX_TRACK_NUM:
            self.alert('Reach the max number of tracks !')
        else:
            self.tc.addTrack()

    def delTrack(self):
        if self.mc.getCurTrackID() is None:
            self.alert('Please select a track to delete !')
        else:
            self.tc.delTrack()
            self.mc.reset()

    def alert(self, info):
            warnDialog = QDialog(self)
            warnLabel = QLabel(info, warnDialog)
            warnLabel.move(100, 100)
            warnDialog.setWindowTitle("Alert")
            warnDialog.resize(500, 200)
            warnDialog.setWindowModality(Qt.ApplicationModal)
            warnDialog.exec_()




