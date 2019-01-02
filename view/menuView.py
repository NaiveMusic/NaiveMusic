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
        self.newButton = QPushButton('New Project', self.dialog)
        self.newButton.clicked.connect(self.openFile)
        self.newButton.move(100, 100)

        self.loadButton = QPushButton('Load Project', self.dialog)
        self.loadButton.clicked.connect(self.openFile)
        self.loadButton.move(100, 150)

        self.saveButton = QPushButton('Save project', self.dialog)
        self.saveButton.clicked.connect(self.openFile)
        self.saveButton.move(100, 200)


        self.exportButton = QPushButton('Export to wav', self.dialog)
        self.exportButton.clicked.connect(self.openFile)
        self.exportButton.move(100, 250)


        self.midiButton = QPushButton('Export to MIDI', self.dialog)
        self.midiButton.clicked.connect(self.openFile)
        self.midiButton.move(100, 300)


        self.importButton = QPushButton('Import MIDI', self.dialog)
        self.importButton.clicked.connect(self.openFile)
        self.importButton.move(100, 350)


        self.dialog.setWindowTitle("Menu")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()


    def openFile(self):
        '''
            Load a file either midi or project from system

            File name is further processed via maincontroller
            
        '''
        fname = QFileDialog.getOpenFileName(self, 'Open file', '../', "TEXT files (*.txt)")
        if fname[0]:
            self.processFile(fname[0])

    def saveFile(self):
        pass


    def processFile(self, filename):
        print('{0} process complete !'.format(filename))
        # TODO Process input file
        pass