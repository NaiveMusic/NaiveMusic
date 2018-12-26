import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *
from controller.mainController import MainController



class Menu(QWidget):
    def __init__(self, mc):
        super().__init__()
        self.mc = mc
        self.init()


    def init(self):
        self.menuButton = QPushButton('', self)
        self.menuButton.setStyleSheet("""
            .QPushButton {
                width: 30px;
                height: 30px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/ui/menu.svg');
            } """)
        self.menuButton.clicked.connect(self.showDialog)
        
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.menuButton)
        self.setLayout(hbox)




    def showDialog(self):
        self.dialog = QDialog(self)
        self.openButton = QPushButton('Open File', self.dialog)
        self.openButton.clicked.connect(self.openFile)
        self.openButton.move(100, 100)
        self.dialog.setWindowTitle("Dialog")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()


    def openFile(self):
        '''
            Load a file either midi or project from system

            File name is further processed via maincontroller
            
        '''
        fname = QFileDialog.getOpenFileName(self, 'Open file', '../', "MIDI files (*.midi)")
        self.processFile(fname)


    def processFile(self, filename):
        print('{0} process complete !'.format(filename))
        # TODO 
        pass