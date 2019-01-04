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
                background-color: rgb(205, 225, 209);
                image: url('view/Icons/ui/menu.svg');
            } """)
        self.menuButton.clicked.connect(self.showDialog)
        
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.menuButton)
        self.setLayout(hbox)




    def showDialog(self):
        step = 70
        ypos = 30
        self.dialog = QDialog(self)
        self.dialog.setStyleSheet("""
            QDialog {
                background-color: rgb(64, 64, 64);
                border-style: outset;
                border-width: 5px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
            }""")
        self.newButton = QPushButton('New Project', self.dialog)
        self.newButton.setStyleSheet("""
                .QPushButton {
                    width: 200px;
                    height: 25px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                }""")
        self.newButton.clicked.connect(self.newFile)
        self.newButton.move(15, ypos)
        ypos = ypos + step

        self.loadButton = QPushButton('Load Project', self.dialog)
        self.loadButton.setStyleSheet("""
                .QPushButton {
                    width: 200px;
                    height: 25px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                }""")
        self.loadButton.clicked.connect(self.openFile)
        self.loadButton.move(15, ypos)
        ypos = ypos + step

        self.saveButton = QPushButton('Save project', self.dialog)
        self.saveButton.setStyleSheet("""
                .QPushButton {
                    width: 200px;
                    height: 25px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                }""")
        self.saveButton.clicked.connect(self.saveFile)
        self.saveButton.move(15, ypos)
        ypos = ypos + step


        self.exportButton = QPushButton('Export wav', self.dialog)
        self.exportButton.setStyleSheet("""
                .QPushButton {
                    width: 200px;
                    height: 25px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                }""")
        self.exportButton.clicked.connect(self.save2Wav)
        self.exportButton.move(15, ypos)
        ypos = ypos + step


        self.midiButton = QPushButton('Export MIDI', self.dialog)
        self.midiButton.setStyleSheet("""
                .QPushButton {
                    width: 200px;
                    height: 25px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                }""")
        self.midiButton.clicked.connect(self.save2Midi)
        self.midiButton.move(15, ypos)
        ypos = ypos + step


        self.importButton = QPushButton('Import MIDI', self.dialog)
        self.importButton.setStyleSheet("""
                .QPushButton {
                    width: 200px;
                    height: 25px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                }""")
        self.importButton.clicked.connect(self.openFile)
        self.importButton.move(15, ypos)
        ypos = ypos + step

        self.exitButton = QPushButton('Exit', self.dialog)
        self.exitButton.setStyleSheet("""
                .QPushButton {
                    width: 200px;
                    height: 25px;
                    font: 25px Verdana;
                    font-weight: bold;
                    color: white;
                    border-style: outset;
                    border-width: 5px;
                    border-radius: 10px;
                    border-color: black;
                    padding: 15px;
                }""")
        self.exitButton.clicked.connect(self.exit)
        self.exitButton.move(15, ypos)
        ypos = ypos + step + 30

        self.dialog.setWindowTitle("Menu")
        self.dialog.resize(270, ypos)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()

    def newFile(self):
        self.mc.newFile()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '../', "Midi (*.mid)")
        if fname[0]:
            self.mc.loadFile(fname[0])

    def saveFile(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', '../', "NM (*.nm)")
        if fname[0]:
            self.mc.saveFile(fname[0])

    def save2Wav(self):
        fname = QFileDialog.getSaveFileName(self, 'Export to wav', '../', "WAV (*.wav)")
        if fname[0]:
            # self.mc.playAll(self, 'wav', fname[0])
            self.mc.export('wav',fname[0])

    def save2Midi(self):
        fname = QFileDialog.getSaveFileName(self, 'Export to midi', '../', "MIDI (*.mid)")
        if fname[0]:
            # self.mc.playAll(self, 'mid', fname[0])
            self.mc.export('mid',fname[0])

    def exit(self):
        sys.exit()


