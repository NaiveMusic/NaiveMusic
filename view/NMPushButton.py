# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from controller.mainController import MainController
import sys

from model.const import *


class NMPushButton(QtWidgets.QPushButton):
    def __init__(self, row, col, noteDict, mc):
        super().__init__()
        self.mc = mc
        # note坐标，以左上角为(1,1)
        self.row = row
        self.col = col
        # 传入noteDict，使得每个note都能操作其他note
        self.noteDict = noteDict
        # 长note起点列号，为0则不是长note
        self.startFrom = 0
        self.setAcceptDrops(True)

    # 重载点击事件
    def mousePressEvent(self, QMouseEvent):
        if self.mc.getCurTrackID() is None:
            warnDialog = QtWidgets.QDialog(self)
            warnLabel = QtWidgets.QLabel('Please select an track first!',
                                         warnDialog)
            warnLabel.move(100, 100)
            warnDialog.setWindowTitle("Alert")
            warnDialog.resize(500, 200)
            warnDialog.setWindowModality(QtCore.Qt.ApplicationModal)
            warnDialog.exec_()
            return
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.setChecked(True)
        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            if self.startFrom == 0:
                self.setChecked(False)
                print("[DELETE] Single note: " + self.objectName())
                # [Delete] Single note
                key = KEY_TOP - self.row
                on = self.col
                off = on + 1
                self.mc.delNote(keys=[key], on=on, off=off)
            else:
                # 向右删除
                i = self.col
                while True:
                    i = i + 1
                    if ('Note_' + str(self.row) + '_' +
                            str(i)) not in self.noteDict.keys():
                        off = i
                        break
                    if self.noteDict['Note_' + str(self.row) + '_' +
                                     str(i)].startFrom != self.startFrom:
                        off = i
                        break
                    self.noteDict['Note_' + str(self.row) + '_' +
                                  str(i)].setChecked(False)
                    self.noteDict['Note_' + str(self.row) + '_' +
                                  str(i)].startFrom = 0
                    self.noteDict['Note_' + str(self.row) + '_' +
                                  str(i)].applyStyle()
                    off = i + 1
                # 向左删除
                i = self.col
                while True:
                    i = i - 1
                    if ('Note_' + str(self.row) + '_' +
                            str(i)) not in self.noteDict.keys():
                        on = i + 1
                        break
                    if self.noteDict['Note_' + str(self.row) + '_' +
                                     str(i)].startFrom != self.startFrom:
                        on = i + 1
                        break
                    self.noteDict['Note_' + str(self.row) + '_' +
                                  str(i)].setChecked(False)
                    self.noteDict['Note_' + str(self.row) + '_' +
                                  str(i)].startFrom = 0
                    self.noteDict['Note_' + str(self.row) + '_' +
                                  str(i)].applyStyle()
                    on = i
                self.setChecked(False)
                self.startFrom = 0
                self.applyStyle()
                print(
                    f"[DELETE] Long note: from Note_{self.row}_{on} to Note_{self.row}_{off-1}"
                )
                # [Delete] Long note
                key = KEY_TOP - self.row
                self.mc.delNote(keys=[key], on=on, off=off)

    def mouseReleaseEvent(self, QMouseEvent):
        # 对拖拽与右键事件不响应
        if self.startFrom != 0 or QMouseEvent.button(
        ) == QtCore.Qt.RightButton:
            return
        print("[ADD] Single note: " + self.objectName())
        # [ADD] Single note
        key = KEY_TOP - self.row
        on = self.col
        off = on + 1
        self.mc.addNote(key=key, vel=100, on=on, off=off)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.LeftButton:
            return
        mimeData = QtCore.QMimeData()
        # 传输起点坐标名称
        mimeData.setText(self.objectName())
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        dropAction = drag.exec_(QtCore.Qt.MoveAction)

    def dragEnterEvent(self, QMouseEvent):
        if QMouseEvent.mimeData().hasText():
            QMouseEvent.accept()
        else:
            QMouseEvent.ignore()
            return
        # 拖动的起始行列号
        startRow = self.noteDict[QMouseEvent.mimeData().text()].row
        startCol = self.noteDict[QMouseEvent.mimeData().text()].col
        # 列内拖动
        if self.col == startCol:
            if ('Note_' + str(startRow) + '_' +
                    str(self.col - 1)) in self.noteDict.keys():
                if self.noteDict['Note_' + str(startRow) + '_' +
                                 str(self.col - 1)].startFrom == startCol:
                    self.noteDict['Note_' + str(startRow) + '_' +
                                  str(self.col - 1)].setChecked(False)
                    self.noteDict['Note_' + str(startRow) + '_' +
                                  str(self.col - 1)].startFrom = 0
                    self.noteDict['Note_' + str(startRow) + '_' +
                                  str(self.col - 1)].applyStyle()
            if ('Note_' + str(startRow) + '_' +
                    str(self.col + 1)) in self.noteDict.keys():
                if self.noteDict['Note_' + str(startRow) + '_' +
                                 str(self.col + 1)].startFrom == startCol:
                    self.noteDict['Note_' + str(startRow) + '_' +
                                  str(self.col + 1)].setChecked(False)
                    self.noteDict['Note_' + str(startRow) + '_' +
                                  str(self.col + 1)].startFrom = 0
                    self.noteDict['Note_' + str(startRow) + '_' +
                                  str(self.col + 1)].applyStyle()
            return
        # 目前对应列行内的note
        endingNote = self.noteDict['Note_' + str(startRow) + '_' + str(
            self.col)]
        # 行内note延长绘制
        i = startCol
        while i != endingNote.col:
            self.noteDict['Note_' + str(startRow) + '_' +
                          str(i)].setChecked(True)
            self.noteDict['Note_' + str(startRow) + '_' +
                          str(i)].startFrom = startCol
            self.noteDict['Note_' + str(startRow) + '_' + str(i)].applyStyle()
            if i < endingNote.col:
                i = i + 1
            else:
                i = i - 1
        self.noteDict['Note_' + str(startRow) + '_' + str(i)].setChecked(True)
        self.noteDict['Note_' + str(startRow) + '_' +
                      str(i)].startFrom = startCol
        self.noteDict['Note_' + str(startRow) + '_' + str(i)].applyStyle()
        # 删除回退的note
        if endingNote.col < startCol:
            if ('Note_' + str(startRow) + '_' +
                    str(endingNote.col - 1)) in self.noteDict.keys():
                preNote = self.noteDict['Note_' + str(startRow) + '_' +
                                        str(endingNote.col - 1)]
            else:
                return
        else:
            if ('Note_' + str(startRow) + '_' +
                    str(endingNote.col + 1)) in self.noteDict.keys():
                preNote = self.noteDict['Note_' + str(startRow) + '_' +
                                        str(endingNote.col + 1)]
            else:
                return
        if preNote.startFrom == startCol:
            preNote.setChecked(False)
            preNote.startFrom = 0
            preNote.applyStyle()

    def dropEvent(self, QMouseEvent):
        QMouseEvent.setDropAction(QtCore.Qt.MoveAction)
        QMouseEvent.accept()
        startNote = self.noteDict[QMouseEvent.mimeData().text()]
        endNote = self.noteDict['Note_' + str(startNote.row) + '_' + str(
            self.col)]
        if startNote.col == endNote.col:
            startNote.startFrom = 0
            startNote.applyStyle()
            print("[ADD] Single note: " + startNote.objectName())
            # [ADD] Single note
            key = KEY_TOP - startNote.row
            on = startNote.col
            off = on + 1
            self.mc.addNote(key=key, vel=100, on=on, off=off)
        else:
            print("[ADD] Long note: from " + QMouseEvent.mimeData().text() +
                  " to " + endNote.objectName())
            # [ADD] Long note
            key = KEY_TOP - endNote.row
            if startNote.col > endNote.col:
                on = endNote.col
                off = startNote.col + 1
            else:
                on = startNote.col
                off = endNote.col + 1
            self.mc.addNote(key=key, vel=100, on=on, off=off)

    def applyStyle(self):
        if self.startFrom == 0:
            self.setStyleSheet(
                "QPushButton:!hover:!checked { border-image: url('view/Icons/sheet/noCheck.png'); }\n"
                "QPushButton:!hover:checked { border-image: url('view/Icons/sheet/checked.png') }\n"
                "QPushButton:hover:checked { border-image: url('view/Icons/sheet/checked_hover.png') }\n"
                "QPushButton:hover:!checked { border-image: url('view/Icons/sheet/noCheck_hover.png'); }"
            )
        else:
            self.setStyleSheet(
                "QPushButton:!hover:!checked { border-image: url('view/Icons/sheet/noCheck.png'); }\n"
                "QPushButton:!hover:checked { border-image: url('view/Icons/sheet/long_checked.png') }\n"
                "QPushButton:hover:checked { border-image: url('view/Icons/sheet/long_checked_hover.png') }\n"
                "QPushButton:hover:!checked { border-image: url('view/Icons/sheet/noCheck_hover.png'); }"
            )