# -*- coding: utf-8 -*-
from ...model.const import *
from ...controller.mainController import MainController

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget, QPushButton
from Ui_sheet import Ui_Sheet


class NMusicSheet(QMainWindow, Ui_Sheet):
    def __init__(self, mc, parent=None):
        super(NMusicSheet, self).__init__(parent)
        self.setupUi(self)
        self.initPianoRoll()
        self.initSheet()
        self.mc = mc
        self.metaRow = 0
        self.metaCol = 0
        self.stdKey = 64

    def initUI(self):
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # PianoRoll
    def initPianoRoll(self):
        for row in range(self.PianoRoll.rowCount()):
            for column in range(self.PianoRoll.columnCount()):
                if self.PianoRoll.itemAtPosition(row, column) is not None:
                    key = self.PianoRoll.itemAtPosition(row, column).widget()
                    if isinstance(key, QPushButton):
                        key.clicked.connect(self.key_clicked)

    # PianoRoll点击事件
    def key_clicked(self):
        sender = self.sender()

        # Change below
        print(sender.objectName())
        # Change above

    # Sheet
    def initSheet(self):
        for row in range(self.Sheet.rowCount()):
            for column in range(self.Sheet.columnCount()):
                if self.Sheet.itemAtPosition(row, column) is not None:
                    note = self.Sheet.itemAtPosition(row, column).widget()
                    if isinstance(note, QPushButton):
                        note.clicked.connect(self.note_clicked)

    # Sheet点击事件
    def note_clicked(self):
        sender = self.sender()

        l = sender.split(str='_',)
        key = l[1] + self.metaRow * self.Sheet.rowCount() + stdKey
        on = l[2] - 1 + self.metaCol * self.Sheet.columnCount()
        off = on + 1

        if not self.mc.isOccupied(key,on,off):
            # If not occupied, add the note
            self.mc.addNote(key=key,on=on,off=off)
            self.mc.setCurPosition(off)
        else:
            # else delete the note
            self.mc.delNote(key=key,on=on,off=off)
            self.mc.setCurPosition(on)

        # Change below
        """
        print(sender.objectName() + ': ' +
              ("on" if sender.isChecked() else "off"))
              """
        # Change above
    
    # 解析按钮名称成对应坐标
    def __parse__(self, buttonName):
        l = buttonName.split(str='_',)
        key = l[1] # + metaRow * self.Sheet.rowCount()
        on = l[2] - 1 # + metaCol * self.Sheet.columnCount()
        return({'y':l[1],'x':l[2]})
        pass

    # 绘制Sheet并设置格式
    def update(self):
        """ 应根据controller.state确定绘制的格式；利用controller.getNotesInfo()等函数获得绘图需要的信息。
        例如：
        当state='EMPTY'时，所有按钮不可点击
        当state='EDITING'时，根据controller.curPos(工作位置)确定相对位置，再在对应区域里根据noteInfo绘制按钮状态；并将处于KEY_RANGE外的按钮设置为不可点击
        当state='PLAYING'时，根据controller.curPlayPos(播放位置)确定相对位置，再在对应区域里根据noteInfo绘制按钮状态，并对处于播放位置的note强调
        
        P.S. 不应该在view的输入函数中改变输出
        """
        pass