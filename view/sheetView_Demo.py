# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from controller.mainController import MainController
import sys

from model.const import *


class SheetView_Demo(QtWidgets.QWidget):
    def __init__(self, mc):
        super().__init__()
        self.mc = mc
        self.mc.register(self)
        self.setupUi(self)
        self.initPianoRoll()
        # self.ROWMAX = 0
        # self.COLMAX = 0

    # PianoRoll
    def initPianoRoll(self):
        for row in range(self.PianoRoll.rowCount()):
            for column in range(self.PianoRoll.columnCount()):
                if self.PianoRoll.itemAtPosition(row, column) is not None:
                    key = self.PianoRoll.itemAtPosition(row, column).widget()
                    if isinstance(key, QtWidgets.QPushButton):
                        key.clicked.connect(self.key_clicked)

    # PianoRoll点击事件
    def key_clicked(self):
        sender = self.sender()

        # Change below
        print(sender.objectName())
        key = sender.objectName().split('_')[1]
        self.mc.playSingle(KEY_TOP - int(key))
        # Change above

    def setupUi(self, MainWindow):
        # Note 个数
        self.ROWMAX = 13
        self.COLMAX = 50

        # sheetSection: PianoRoll, Sheet, Velocity
        self.SheetSection = QtWidgets.QHBoxLayout()
        self.SheetSection.setObjectName("SheetSection")

        # PianoRoll
        self.PianoRoll = QtWidgets.QGridLayout()
        self.PianoRoll.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.PianoRoll.setSpacing(0)
        self.PianoRoll.setObjectName("PianoRoll")
        self.pianoTopBlank = QtWidgets.QLabel(self)

        # [PianoRoll] 顶部空白标签
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pianoTopBlank.sizePolicy().hasHeightForWidth())
        self.pianoTopBlank.setSizePolicy(sizePolicy)
        self.pianoTopBlank.setMaximumSize(QtCore.QSize(175, 75))
        self.pianoTopBlank.setText("")
        self.pianoTopBlank.setObjectName("pianoTopBlank")
        self.PianoRoll.addWidget(self.pianoTopBlank, 0, 0, 1, 1)

        # [PianoRoll] 设置钢琴试音键
        self.keyDict = {}

        # [PianoRoll] 设置单个琴键
        # keyType: main-主音; black-升音
        # keyNum: 音高
        # place: 从上到下的位置
        def setKey(keyType, keyNum, place):
            keyName = str(keyType) + "Key_" + str(place)
            self.keyDict[keyName] = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.keyDict[keyName].sizePolicy().hasHeightForWidth())
            self.keyDict[keyName].setSizePolicy(sizePolicy)
            self.keyDict[keyName].setMaximumSize(QtCore.QSize(175, 75))
            self.keyDict[keyName].setMinimumSize(QtCore.QSize(120, 35))
            if (keyType == 'main'):
                self.keyDict[keyName].setStyleSheet(
                    "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
                    "QPushButton:pressed { background-color: rgb(250, 250, 250); }"
                )
            else:
                self.keyDict[keyName].setStyleSheet(
                    "QPushButton:!pressed { background-color: rgb(0, 0, 0); }\n"
                    "QPushButton:pressed { background-color: rgb(75, 75, 75); }"
                )
            self.keyDict[keyName].setText("")
            self.keyDict[keyName].setCheckable(False)
            self.keyDict[keyName].setObjectName(keyName)
            self.PianoRoll.addWidget(self.keyDict[keyName], place, 0, 1, 1)

        setKey('main', 8, 1)
        setKey('main', 7, 2)
        setKey('black', 6, 3)
        setKey('main', 6, 4)
        setKey('black', 5, 5)
        setKey('main', 5, 6)
        setKey('black', 4, 7)
        setKey('main', 4, 8)
        setKey('main', 3, 9)
        setKey('black', 2, 10)
        setKey('main', 2, 11)
        setKey('black', 1, 12)
        setKey('main', 1, 13)

        self.pianoBoardWidget = QtWidgets.QWidget()
        self.pianoBoardWidget.setLayout(self.PianoRoll)
        self.pianoScroll = QtWidgets.QScrollArea()
        self.pianoScroll.setWidget(self.pianoBoardWidget)
        self.pianoScroll.setMinimumHeight(350)
        self.pianoScroll.setFixedWidth(160)
        self.SheetSection.addWidget(self.pianoScroll)

        # Sheet
        self.Sheet = QtWidgets.QGridLayout()
        self.Sheet.setSpacing(0)
        self.Sheet.setObjectName("Sheet")

        # [Sheet] 设置钢琴试音键
        self.noteDict = {}

        def setNote(row, col):
            noteName = 'Note_' + str(row) + '_' + str(col)
            self.noteDict[noteName] = NMPushButton(row, col, self.noteDict,
                                                   self.mc)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.noteDict[noteName].sizePolicy().hasHeightForWidth())
            self.noteDict[noteName].setSizePolicy(sizePolicy)
            self.noteDict[noteName].setMaximumSize(QtCore.QSize(75, 75))
            self.noteDict[noteName].setMinimumSize(QtCore.QSize(35, 35))
            self.noteDict[noteName].setStyleSheet(
                "QPushButton:!hover:!checked { border-image: url('view/Icons/sheet/noCheck.png'); }\n"
                "QPushButton:!hover:checked { border-image: url('view/Icons/sheet/checked.png') }\n"
                "QPushButton:hover:checked { border-image: url('view/Icons/sheet/checked_hover.png') }\n"
                "QPushButton:hover:!checked { border-image: url('view/Icons/sheet/noCheck_hover.png'); }"
            )
            self.noteDict[noteName].setText("")
            self.noteDict[noteName].setCheckable(True)
            self.noteDict[noteName].setObjectName(noteName)
            self.Sheet.addWidget(self.noteDict[noteName], row, col - 1, 1, 1)

        row = self.ROWMAX
        while row > 0:
            col = self.COLMAX
            while col > 0:
                setNote(row, col)
                col = col - 1
            row = row - 1

        # [Sheet] 设置小节号
        self.measureDict = {}

        # [Sheet] 设置单个小节号
        def setMeasure(num):
            measureName = "Measure_" + str(num)
            self.measureDict[measureName] = QtWidgets.QLabel(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.measureDict[measureName].sizePolicy().hasHeightForWidth())
            self.measureDict[measureName].setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(10)
            self.measureDict[measureName].setFont(font)
            self.measureDict[measureName].setObjectName(str(num))
            self.Sheet.addWidget(self.measureDict[measureName], 0,
                                 (num - 1) * 4, 1, 1)

        measureNum = self.COLMAX // 4 + 1
        while measureNum > 0:
            setMeasure(measureNum)
            measureNum = measureNum - 1
        self.sheetBoardWidget = QtWidgets.QWidget()
        self.sheetBoardWidget.setLayout(self.Sheet)
        self.sheetScroll = QtWidgets.QScrollArea()
        self.sheetScroll.setWidget(self.sheetBoardWidget)
        self.SheetSection.addWidget(self.sheetScroll)

        # 同步滚动
        self.pianoScroll.verticalScrollBar().valueChanged.connect(
            self.sheetScroll.verticalScrollBar().setValue)
        self.sheetScroll.verticalScrollBar().valueChanged.connect(
            self.pianoScroll.verticalScrollBar().setValue)
        # 滚动条消隐
        self.pianoScroll.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.sheetScroll.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)

        # Velocity
        self.Velocity = QtWidgets.QGridLayout()
        self.Velocity.setSpacing(0)
        self.Velocity.setObjectName("Velocity")

        # [Velocity] 顶部标签
        self.VelocityLabel = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.VelocityLabel.sizePolicy().hasHeightForWidth())
        self.VelocityLabel.setSizePolicy(sizePolicy)
        self.VelocityLabel.setMinimumSize(QtCore.QSize(40, 40))
        self.VelocityLabel.setMaximumSize(QtCore.QSize(175, 75))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.VelocityLabel.setFont(font)
        self.VelocityLabel.setObjectName("VelocityLabel")
        self.Velocity.addWidget(self.VelocityLabel, 0, 0, 1, 1)

        # [Velocity] 音量条
        self.VelocitySlider = QtWidgets.QSlider(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.VelocitySlider.sizePolicy().hasHeightForWidth())
        self.VelocitySlider.setSizePolicy(sizePolicy)
        self.VelocitySlider.setMaximumSize(QtCore.QSize(75, 16777215))
        self.VelocitySlider.setOrientation(QtCore.Qt.Vertical)
        self.VelocitySlider.setObjectName("VelocitySlider")
        self.Velocity.addWidget(self.VelocitySlider, 1, 0, 1, 1)
        self.SheetSection.addLayout(self.Velocity)

        self.setLayout(self.SheetSection)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 更新全部sheet
    def update(self):
        print('updating')
        return
        # 清空sheet
        for note in self.noteDict.values():
            note.startFrom = 0
            note.applyStyle()
            note.setChecked(False)
        # 获取note信息并绘制
        noteInfoList = self.mc.getNotesInfo(
            keys=KEY_RANGE, on=0, off=self.COLMAX)
        for noteInfo in noteInfoList:
            # 单音绘制
            if noteInfo['On'] == noteInfo['Off'] - 1:
                self.noteDict['Note_' + str(KEY_TOP - noteInfo['Key']) + '_' +
                              str(noteInfo['On'])].setChecked(True)
            # 长音绘制
            else:
                i = noteInfo['On']
                while i < noteInfo['Off']:
                    drawingNote = self.noteDict['Note_' +
                                                str(KEY_TOP - noteInfo['Key'])
                                                + '_' + str(i)]
                    drawingNote.setChecked(True)
                    drawingNote.startFrom = noteInfo['On']
                    drawingNote.applyStyle()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        for name in self.measureDict:
            self.measureDict[name].setText(
                _translate("MainWindow", self.measureDict[name].objectName()))
        self.VelocityLabel.setText(_translate("MainWindow", "Velocity"))


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
                self.mc.delNote(key=key, on=on, off=off)
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
                self.mc.delNote(key=key, on=on, off=off)

    def mouseReleaseEvent(self, QMouseEvent):
        # 对拖拽与右键事件不响应
        if self.startFrom != 0 or QMouseEvent.button() == QtCore.Qt.RightButton:
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
