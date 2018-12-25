# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from controller.mainController import MainController
import view.sheet.pictures_rc


class SheetView_Demo(QtWidgets.QWidget):
    def __init__(self, mc):
        super().__init__()
        self.mc = mc
        self.setupUi(self)
        self.initPianoRoll()
        self.initSheet()

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
        # Change above

    # Sheet
    def initSheet(self):
        for row in range(self.Sheet.rowCount()):
            for column in range(self.Sheet.columnCount()):
                if self.Sheet.itemAtPosition(row, column) is not None:
                    note = self.Sheet.itemAtPosition(row, column).widget()
                    if isinstance(note, QtWidgets.QPushButton):
                        note.clicked.connect(self.note_clicked)

    # Sheet点击事件
    def note_clicked(self):
        sender = self.sender()

        # Change below
        print(sender.objectName() + ': ' +
              ("on" if sender.isChecked() else "off"))
        # Change above

    def setupUi(self, MainWindow):
        # Note 个数
        ROWMAX = 13
        COLMAX = 17

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
            keyName = str(keyType) + "Key_" + str(keyNum)
            self.keyDict[keyName] = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.keyDict[keyName].sizePolicy().hasHeightForWidth())
            self.keyDict[keyName].setSizePolicy(sizePolicy)
            self.keyDict[keyName].setMaximumSize(QtCore.QSize(175, 75))
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
        self.SheetSection.addLayout(self.PianoRoll)

        # Sheet
        self.Sheet = QtWidgets.QGridLayout()
        self.Sheet.setSpacing(0)
        self.Sheet.setObjectName("Sheet")

        # [Sheet] 设置钢琴试音键
        self.noteDict = {}

        def setNote(row, col):
            noteName = 'Note_' + str(row) + '_' + str(col)
            self.noteDict[noteName] = QtWidgets.QPushButton(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.noteDict[noteName].sizePolicy().hasHeightForWidth())
            self.noteDict[noteName].setSizePolicy(sizePolicy)
            self.noteDict[noteName].setStyleSheet(
                "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
                "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
                "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
                "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
            )
            self.noteDict[noteName].setText("")
            self.noteDict[noteName].setCheckable(True)
            self.noteDict[noteName].setObjectName(noteName)
            self.Sheet.addWidget(self.noteDict[noteName], row, col - 1, 1, 1)

        row = ROWMAX
        while row > 0:
            col = COLMAX
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

        measureNum = COLMAX // 4 + 1
        while measureNum > 0:
            setMeasure(measureNum)
            measureNum = measureNum - 1
        self.SheetSection.addLayout(self.Sheet)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        for name in self.measureDict:
            self.measureDict[name].setText(
                _translate("MainWindow", self.measureDict[name].objectName()))
        self.VelocityLabel.setText(_translate("MainWindow", "Velocity"))
