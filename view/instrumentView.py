import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *



class InstrumentView(QWidget):
    def __init__(self, instID, name, mc, style="""
            .QPushButton {
                    width: 20px;
                    height: 20px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    background-color: rgb(255, 255, 111);
                } """):
        super().__init__()
        self.instrumentID = instID
        self.instName = name
        self.style = style
        self.mc = mc
        self.init()
        self.initUI()
        self.setMinimumSize(85, 85)


    def init(self):
        # Regular Expression to set stylesheet

        p1 = r"Piano"
        p2 = r"Grand"
        p3 = r"Bass"
        p4 = r"Guitar"
        p5 = r"Drum"
        p6 = r"Organ"

        if re.search(p1, self.name) or re.search(p2, self.name) or re.search(p6, self.name) :
            self.style = """
                .QPushButton {
                    width: 20px;
                    height: 20px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(255, 255, 111);
                    image: url('view/Icons/instrument/keyboard.svg');
                
                }"""
        else if re.search(p3, self.name):
            self.style = """
                .QPushButton {
                    width: 20px;
                    height: 20px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(255, 255, 111);
                    image: url('view/Icons/instrument/bass.svg');
                
                }"""

        else if re.search(p4, self.name):
            self.style = """
                .QPushButton {
                    width: 20px;
                    height: 20px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(255, 255, 111);
                    image: url('view/Icons/instrument/guitar.svg');
                
                }"""
        else if re.search(p5, self.name):
            self.style = """
                .QPushButton {
                    width: 20px;
                    height: 20px;
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    padding: 15px;
                    background-color: rgb(255, 255, 111);
                    image: url('view/Icons/instrument/drum.svg');
                
                }"""
        else:
            pass





    def initUI(self):
        self.instrumentButton = QPushButton('', self)
        self.instrumentButton.setStyleSheet(self.style)  
        self.instrumentButton.setGeometry(QRect(0, 0, 80, 80))
        self.instrumentButton.clicked.connect(self.setInst)
        self.cancelButton = QPushButton('', self)
        self.cancelButton.setGeometry(QRect(70, 0, 10, 10))
        self.cancelButton.setIcon(QIcon('view/Icons/ui/cancel.svg'))
        self.cancelButton.clicked.connect(self.deleteInstrument)


    def deleteInstrument(self):
        self.deleteLater()

    def setInst(self):
        self.mc.setSelectedInst(self.instrumentID)
        print("Instrument {0} selected !".format(self.instrumentID))


class InstrumentContainer(QWidget, mc):
    def __init__(self):
        super().__init__()
        self.instList = {}
        self.mc = mc


    def init(self):
    	instList[1] = InstrumentView(1, INSTRUMENT[1], self.mc)
    	instList[26] = InstrumentView(26, INSTRUMENT[26], self.mc)
    	instList[33] = InstrumentView(33, INSTRUMENT[33], self.mc)
        

    def initUI(self):
        self.instLayout = QHBoxLayout()
        self.addStretch(0)
        for instID, inst in instList.items():
        	self.instLayout.addWidget(inst)
        self.instLib = QComboBox()
        self.instLib.addItems(['{} {}'.format(i, INSTRUMENT[i]) for i in INSTRUMENT])
        self.instLib.currentIndexChanged.connect(self.addInst)
        self.instLayout.addWidget(self.instLib)
        self.instLayout.addStretch(0)
        self.setLayout(self.instLayout)


    def getCurInstStyle(self):
        return instList[self.mc.getSelectedInst()].style

    def addInst(self):
    	pass


