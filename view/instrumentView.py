import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model.const import *



class InstrumentView(QWidget):
    def __init__(self, instID, instName, mc, style="""
            .QPushButton {
                width: 20px;
                height: 20px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/instrument/default.svg');
                
                } """):
        super().__init__()
        self.instrumentID = instID
        self.instName = instName
        self.style = style
        self.mc = mc
        self.init()
        self.initUI()
        self.setMinimumSize(85, 85)


    def init(self):
        # Regular Expression to set stylesheet
        self.style = style(self.instName)





    def initUI(self):
        self.instrumentButton = QPushButton('', self)
        self.instrumentButton.setStyleSheet(self.style)  
        self.instrumentButton.setGeometry(QRect(0, 0, 80, 80))
        self.instrumentButton.clicked.connect(self.setInst)
        self.cancelButton = QPushButton('', self)
        self.cancelButton.setGeometry(QRect(70, 0, 10, 10))
        self.cancelButton.setStyleSheet("""
            .QPushButton {
                width: 10px;
                height: 10px;
                border: none;
            }""")
        self.cancelButton.setIcon(QIcon('view/Icons/ui/cancel.svg'))
        self.cancelButton.clicked.connect(self.deleteInstrument)


    def deleteInstrument(self):
        self.deleteLater()
        if self.mc.getSelectedInst() is not None and self.instrumentID == self.mc.getSelectedInst():
            self.mc.setSelectedInst(None)

    def setInst(self):
        self.mc.setSelectedInst(self.instrumentID)
        print("Instrument {0} selected !".format(self.instrumentID))


class InstrumentContainer(QWidget):
    def __init__(self, mc):
        super().__init__()
        self.instList = {}
        self.mc = mc
        self.init()
        self.initUI()


    def init(self):
    	self.instList[1] = InstrumentView(1, INSTRUMENT[1], self.mc)
    	self.instList[26] = InstrumentView(26, INSTRUMENT[26], self.mc)
    	self.instList[33] = InstrumentView(33, INSTRUMENT[33], self.mc)
        

    def initUI(self):
        self.instLayout = QHBoxLayout()
        self.instLayout.addStretch(0)
        for instID, inst in self.instList.items():
        	self.instLayout.addWidget(inst)
        self.instLib = QComboBox()
        self.instLib.addItems(['{} {}'.format(i, INSTRUMENT[i]) for i in INSTRUMENT])
        self.instLib.currentIndexChanged.connect(self.addInst)
        self.instLayout.addWidget(self.instLib)
        self.instLayout.addStretch(0)
        self.setLayout(self.instLayout)


    def getCurInstStyle(self):
        return self.instList[self.mc.getSelectedInst()].style

    def getCurInstID(self):
        return self.mc.getSelectedInst()

    def addInst(self):
        instID = self.instLib.currentIndex()
        newInst = InstrumentView(instID, INSTRUMENT[instID], self.mc)
        self.instList[instID] = newInst
        self.instLayout.insertWidget(self.instLayout.count()-2, newInst)

