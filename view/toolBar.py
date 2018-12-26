import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *
from controller.mainController import MainController

class ToolBar(QWidget):
    def __init__(self, mc, menu):
        super().__init__()
        self.menu = menu
        self.mc = mc
        self.isPlay = False
        self.init()
        self.initUI()



    def init(self):
        '''
            Initialize toolbar ui, including a:

                playtrack icon, playall icon, pause icon, BPM setting, global volume setting and menu icon

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
                image: url('view/Icons/ui/pause.svg');
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


    def initUI(self):
        hbox = QHBoxLayout()
        hbox.addStretch(0)
        hbox.addWidget(self.playButton)
        hbox.addWidget(self.playAllButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.menu)
        hbox.addStretch(0)
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
            self.mc.playTrack(self.mc.getCurTrackID())
            print('Track {0} is playing. '.format(self.mc.getCurTrackID()))

    def playAll(self):

        self.mc.playAll()
        pass

    def pause(self):

        # TODO
        pass

    def stop(self):
        self.mc.stopAll()
        # TODO 


    def setBPM(self):
        self.mc.setBPM(bmp)

        # TODO



