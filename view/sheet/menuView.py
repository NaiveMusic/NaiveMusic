import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *
from controller.mainController import MainController



class Menu(QWidget):
    def __inti__(self, mc):
        super().__init__()
        self.mc = mc
        self.init()


    def init(self):
        self.menuButton = QPushButton('', self)
        self.menuButton.clicked.connect(self.showDialog)



    def showDialog(self):
        self.dialog = QDialog('', self)
        self.openButton = QPushButton('Open File', self)
        self.openButton.clicked.connec(self.openFile)

        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()


    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '../', "MIDI files (*.midi)")
        self.processFile(fname)


    def processFile(self, filename):

        # TODO 
        pass