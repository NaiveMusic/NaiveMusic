# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from controller.mainController import MainController
import sys

from model.const import *
from view.NMPushButton import NMPushButton


class SheetView(QtWidgets.QWidget):
    def __init__(self, mc):
        super().__init__()
        self.mc = mc
        self.mc.register(self)
        self.setupUi(self)
        self.initPianoRoll()

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
        # Change below
        print(sender.objectName())
        key = sender.objectName().split('_')[1]
        self.mc.playSingle(KEY_TOP - int(key))
        # Change above

    def setupUi(self, MainWindow):
        # 当前Track
        self.curTrack = None

        # Note 个数
        self.ROWMAX = 84
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
                    "QPushButton:!pressed { background-color: rgb(0, 0, 0); color: white; }\n"
                    "QPushButton:pressed { background-color: rgb(75, 75, 75); color: white; }"
                )
            self.keyDict[keyName].setText(keyNum)
            self.keyDict[keyName].setCheckable(False)
            self.keyDict[keyName].setObjectName(keyName)
            self.PianoRoll.addWidget(self.keyDict[keyName], place, 0, 1, 1)

        i = 7
        while i > 0:
            offset = 84 - 12 * i
            setKey('main', 'B' + str(i), 1 + offset)
            setKey('black', 'A#' + str(i), 2 + offset)
            setKey('main', 'A' + str(i), 3 + offset)
            setKey('black', 'G#' + str(i), 4 + offset)
            setKey('main', 'G' + str(i), 5 + offset)
            setKey('black', 'F#' + str(i), 6 + offset)
            setKey('main', 'F' + str(i), 7 + offset)
            setKey('main', 'E' + str(i), 8 + offset)
            setKey('black', 'D#' + str(i), 9 + offset)
            setKey('main', 'D' + str(i), 10 + offset)
            setKey('black', 'C#' + str(i), 11 + offset)
            setKey('main', 'C' + str(i), 12 + offset)
            i = i - 1

        self.pianoBoardWidget = QtWidgets.QWidget()
        self.pianoBoardWidget.setLayout(self.PianoRoll)
        self.pianoBoardWidget.setStyleSheet("""
            .QWidget {
                background-color: transparent;
            }""")
        self.pianoScroll = QtWidgets.QScrollArea()
        self.pianoScroll.setWidget(self.pianoBoardWidget)
        self.pianoScroll.setMinimumHeight(350)
        self.pianoScroll.setFixedWidth(160)
        self.pianoScroll.setStyleSheet("""
            .QScrollArea {
                background-color: transparent;
            }""")
        # self.pianoScroll.setVa
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
            # self.noteDict[noteName].setMaximumSize(QtCore.QSize(75, 75))
            self.noteDict[noteName].setFixedSize(QtCore.QSize(35, 35))
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
            self.measureDict[measureName].setStyleSheet("""
            .QLabel {
                color: white;
            }""")
            self.Sheet.addWidget(self.measureDict[measureName], 0,
                                 (num - 1) * 4, 1, 1)

        measureNum = self.COLMAX // 4 + 1
        while measureNum > 0:
            setMeasure(measureNum)
            measureNum = measureNum - 1

        self.sheetBoardWidget = QtWidgets.QWidget()
        self.sheetBoardWidget.setLayout(self.Sheet)
        self.sheetBoardWidget.setStyleSheet("""
            .QWidget {
                background-color: transparent;
            }""")
        self.sheetScroll = QtWidgets.QScrollArea()
        self.sheetScroll.setWidget(self.sheetBoardWidget)
        self.sheetScroll.setStyleSheet("""
            .QScrollArea {
                background-color: transparent;
            }""")
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
        self.pianoScroll.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.sheetScroll.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)

        self.pianoScroll.verticalScrollBar().setValue(1350)
        self.sheetScroll.verticalScrollBar().setValue(1350)

        """
        # Add button
        self.Right = QtWidgets.QGridLayout()
        self.Right.setSpacing(0)
        self.addButton = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.Right.addWidget(self.addButton, 1, 0, 1, 1)
        self.SheetSection.addLayout(self.Right)

        def addSheet():
            print("Add 10 columns.")
            # add notes
            col = self.COLMAX + 1
            self.COLMAX += 10
            while col <= self.COLMAX:
                row = self.ROWMAX
                while row > 0:
                    setNote(row, col)
                    row -= 1
                col += 1
            # add measures
            measureNum = self.COLMAX // 4 + 1
            print(measureNum)
            setMeasure(4)
            while measureNum > 0:
                setMeasure(measureNum)
                measureNum = measureNum - 1
            col = self.COLMAX
            while col > 0:
                self.Sheet.setColumnMinimumWidth(col, 35)
                col -= 1
            temp_sheetBoardWidget = QtWidgets.QWidget()
            temp_sheetBoardWidget.setLayout(self.Sheet)
            self.sheetScroll.setWidget(temp_sheetBoardWidget)
        self.addButton.clicked.connect(addSheet)
        """

        self.setLayout(self.SheetSection)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 更新全部sheet
    def update(self):
        print('updating')
        if self.curTrack is not None:
            # 清空sheet
            eraseList = self.mc.getAnyTrackNotesInfo(
                self.curTrack, keys=KEY_RANGE, on=0, off=self.COLMAX)
            for noteInfo in eraseList:
                # 单音清空
                if noteInfo['On'] == noteInfo['Off'] - 1:
                    self.noteDict['Note_' + str(KEY_TOP - noteInfo['Key']) +
                                  '_' + str(noteInfo['On'])].setChecked(False)
                # 长音清空
                else:
                    i = noteInfo['On']
                    while i < noteInfo['Off']:
                        drawingNote = self.noteDict['Note_' + str(
                            KEY_TOP - noteInfo['Key']) + '_' + str(i)]
                        drawingNote.setChecked(False)
                        drawingNote.startFrom = 0
                        drawingNote.applyStyle()
                        i += 1
        """
        # 暴力清空sheet
        for note in self.noteDict.values():
            note.startFrom = 0
            note.applyStyle()
            note.setChecked(False)
        """
        # 获取note信息并绘制
        self.curTrack = self.mc.getCurTrackID()
        if self.curTrack is not None:
            noteInfoList = self.mc.getAnyTrackNotesInfo(
                self.curTrack, keys=KEY_RANGE, on=0, off=self.COLMAX)
            for noteInfo in noteInfoList:
                # 单音绘制
                if noteInfo['On'] == noteInfo['Off'] - 1:
                    self.noteDict['Note_' + str(KEY_TOP - noteInfo['Key']) +
                                  '_' + str(noteInfo['On'])].setChecked(True)
                # 长音绘制
                else:
                    i = noteInfo['On']
                    while i < noteInfo['Off']:
                        drawingNote = self.noteDict['Note_' + str(
                            KEY_TOP - noteInfo['Key']) + '_' + str(i)]
                        drawingNote.setChecked(True)
                        drawingNote.startFrom = noteInfo['On']
                        drawingNote.applyStyle()
                        i += 1
        print('update finished')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        for name in self.measureDict:
            self.measureDict[name].setText(
                _translate("MainWindow", self.measureDict[name].objectName()))
