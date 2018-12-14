# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Tom\Documents\GitHub\NaiveMusic\view\demo-sheet\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 785)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/global/src/global/logo.png"), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SheetSection = QtWidgets.QHBoxLayout()
        self.SheetSection.setObjectName("SheetSection")
        self.PianoRoll = QtWidgets.QGridLayout()
        self.PianoRoll.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.PianoRoll.setSpacing(0)
        self.PianoRoll.setObjectName("PianoRoll")
        self.pianoTopBlank = QtWidgets.QLabel(self.centralwidget)
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
        self.mainKey_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_8.sizePolicy().hasHeightForWidth())
        self.mainKey_8.setSizePolicy(sizePolicy)
        self.mainKey_8.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_8.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_8.setText("")
        self.mainKey_8.setCheckable(False)
        self.mainKey_8.setObjectName("mainKey_8")
        self.PianoRoll.addWidget(self.mainKey_8, 1, 0, 1, 1)
        self.mainKey_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_7.sizePolicy().hasHeightForWidth())
        self.mainKey_7.setSizePolicy(sizePolicy)
        self.mainKey_7.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_7.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_7.setText("")
        self.mainKey_7.setCheckable(False)
        self.mainKey_7.setObjectName("mainKey_7")
        self.PianoRoll.addWidget(self.mainKey_7, 2, 0, 1, 1)
        self.blackKey_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.blackKey_6.sizePolicy().hasHeightForWidth())
        self.blackKey_6.setSizePolicy(sizePolicy)
        self.blackKey_6.setMaximumSize(QtCore.QSize(175, 75))
        self.blackKey_6.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(0, 0, 0); }\n"
            "QPushButton:pressed { background-color: rgb(75, 75, 75); }")
        self.blackKey_6.setText("")
        self.blackKey_6.setCheckable(False)
        self.blackKey_6.setObjectName("blackKey_6")
        self.PianoRoll.addWidget(self.blackKey_6, 3, 0, 1, 1)
        self.mainKey_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_6.sizePolicy().hasHeightForWidth())
        self.mainKey_6.setSizePolicy(sizePolicy)
        self.mainKey_6.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_6.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_6.setText("")
        self.mainKey_6.setCheckable(False)
        self.mainKey_6.setObjectName("mainKey_6")
        self.PianoRoll.addWidget(self.mainKey_6, 4, 0, 1, 1)
        self.blackKey_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.blackKey_5.sizePolicy().hasHeightForWidth())
        self.blackKey_5.setSizePolicy(sizePolicy)
        self.blackKey_5.setMaximumSize(QtCore.QSize(175, 75))
        self.blackKey_5.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(0, 0, 0); }\n"
            "QPushButton:pressed { background-color: rgb(75, 75, 75); }")
        self.blackKey_5.setText("")
        self.blackKey_5.setCheckable(False)
        self.blackKey_5.setObjectName("blackKey_5")
        self.PianoRoll.addWidget(self.blackKey_5, 5, 0, 1, 1)
        self.mainKey_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_5.sizePolicy().hasHeightForWidth())
        self.mainKey_5.setSizePolicy(sizePolicy)
        self.mainKey_5.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_5.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_5.setText("")
        self.mainKey_5.setCheckable(False)
        self.mainKey_5.setObjectName("mainKey_5")
        self.PianoRoll.addWidget(self.mainKey_5, 6, 0, 1, 1)
        self.blackKey_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.blackKey_4.sizePolicy().hasHeightForWidth())
        self.blackKey_4.setSizePolicy(sizePolicy)
        self.blackKey_4.setMaximumSize(QtCore.QSize(175, 75))
        self.blackKey_4.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(0, 0, 0); }\n"
            "QPushButton:pressed { background-color: rgb(75, 75, 75); }")
        self.blackKey_4.setText("")
        self.blackKey_4.setCheckable(False)
        self.blackKey_4.setObjectName("blackKey_4")
        self.PianoRoll.addWidget(self.blackKey_4, 7, 0, 1, 1)
        self.mainKey_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_4.sizePolicy().hasHeightForWidth())
        self.mainKey_4.setSizePolicy(sizePolicy)
        self.mainKey_4.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_4.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_4.setText("")
        self.mainKey_4.setCheckable(False)
        self.mainKey_4.setObjectName("mainKey_4")
        self.PianoRoll.addWidget(self.mainKey_4, 8, 0, 1, 1)
        self.mainKey_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_3.sizePolicy().hasHeightForWidth())
        self.mainKey_3.setSizePolicy(sizePolicy)
        self.mainKey_3.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_3.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_3.setText("")
        self.mainKey_3.setCheckable(False)
        self.mainKey_3.setObjectName("mainKey_3")
        self.PianoRoll.addWidget(self.mainKey_3, 9, 0, 1, 1)
        self.blackKey_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.blackKey_2.sizePolicy().hasHeightForWidth())
        self.blackKey_2.setSizePolicy(sizePolicy)
        self.blackKey_2.setMaximumSize(QtCore.QSize(175, 75))
        self.blackKey_2.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(0, 0, 0); }\n"
            "QPushButton:pressed { background-color: rgb(75, 75, 75); }")
        self.blackKey_2.setText("")
        self.blackKey_2.setCheckable(False)
        self.blackKey_2.setObjectName("blackKey_2")
        self.PianoRoll.addWidget(self.blackKey_2, 10, 0, 1, 1)
        self.mainKey_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_2.sizePolicy().hasHeightForWidth())
        self.mainKey_2.setSizePolicy(sizePolicy)
        self.mainKey_2.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_2.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_2.setText("")
        self.mainKey_2.setCheckable(False)
        self.mainKey_2.setObjectName("mainKey_2")
        self.PianoRoll.addWidget(self.mainKey_2, 11, 0, 1, 1)
        self.blackKey_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.blackKey_1.sizePolicy().hasHeightForWidth())
        self.blackKey_1.setSizePolicy(sizePolicy)
        self.blackKey_1.setMaximumSize(QtCore.QSize(175, 75))
        self.blackKey_1.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(0, 0, 0); }\n"
            "QPushButton:pressed { background-color: rgb(75, 75, 75); }")
        self.blackKey_1.setText("")
        self.blackKey_1.setCheckable(False)
        self.blackKey_1.setObjectName("blackKey_1")
        self.PianoRoll.addWidget(self.blackKey_1, 12, 0, 1, 1)
        self.mainKey_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainKey_1.sizePolicy().hasHeightForWidth())
        self.mainKey_1.setSizePolicy(sizePolicy)
        self.mainKey_1.setMaximumSize(QtCore.QSize(175, 75))
        self.mainKey_1.setStyleSheet(
            "QPushButton:!pressed { background-color: rgb(255, 255, 255); }\n"
            "QPushButton:pressed { background-color: rgb(250, 250, 250); }")
        self.mainKey_1.setText("")
        self.mainKey_1.setCheckable(False)
        self.mainKey_1.setObjectName("mainKey_1")
        self.PianoRoll.addWidget(self.mainKey_1, 13, 0, 1, 1)
        self.SheetSection.addLayout(self.PianoRoll)
        self.Sheet = QtWidgets.QGridLayout()
        self.Sheet.setSpacing(0)
        self.Sheet.setObjectName("Sheet")
        self.Note5_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_6.sizePolicy().hasHeightForWidth())
        self.Note5_6.setSizePolicy(sizePolicy)
        self.Note5_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_6.setText("")
        self.Note5_6.setCheckable(True)
        self.Note5_6.setObjectName("Note5_6")
        self.Sheet.addWidget(self.Note5_6, 8, 4, 1, 1)
        self.Note4_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_6.sizePolicy().hasHeightForWidth())
        self.Note4_6.setSizePolicy(sizePolicy)
        self.Note4_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_6.setText("")
        self.Note4_6.setCheckable(True)
        self.Note4_6.setObjectName("Note4_6")
        self.Sheet.addWidget(self.Note4_6, 8, 3, 1, 1)
        self.Note4_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_5.sizePolicy().hasHeightForWidth())
        self.Note4_5.setSizePolicy(sizePolicy)
        self.Note4_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_5.setText("")
        self.Note4_5.setCheckable(True)
        self.Note4_5.setObjectName("Note4_5")
        self.Sheet.addWidget(self.Note4_5, 9, 3, 1, 1)
        self.Note4_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_7.sizePolicy().hasHeightForWidth())
        self.Note4_7.setSizePolicy(sizePolicy)
        self.Note4_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_7.setText("")
        self.Note4_7.setCheckable(True)
        self.Note4_7.setObjectName("Note4_7")
        self.Sheet.addWidget(self.Note4_7, 7, 3, 1, 1)
        self.Note4_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_3.sizePolicy().hasHeightForWidth())
        self.Note4_3.setSizePolicy(sizePolicy)
        self.Note4_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_3.setText("")
        self.Note4_3.setCheckable(True)
        self.Note4_3.setObjectName("Note4_3")
        self.Sheet.addWidget(self.Note4_3, 11, 3, 1, 1)
        self.Note4_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_8.sizePolicy().hasHeightForWidth())
        self.Note4_8.setSizePolicy(sizePolicy)
        self.Note4_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_8.setText("")
        self.Note4_8.setCheckable(True)
        self.Note4_8.setObjectName("Note4_8")
        self.Sheet.addWidget(self.Note4_8, 6, 3, 1, 1)
        self.Note4_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_4.sizePolicy().hasHeightForWidth())
        self.Note4_4.setSizePolicy(sizePolicy)
        self.Note4_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_4.setText("")
        self.Note4_4.setCheckable(True)
        self.Note4_4.setObjectName("Note4_4")
        self.Sheet.addWidget(self.Note4_4, 10, 3, 1, 1)
        self.Note12_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_9.sizePolicy().hasHeightForWidth())
        self.Note12_9.setSizePolicy(sizePolicy)
        self.Note12_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_9.setText("")
        self.Note12_9.setCheckable(True)
        self.Note12_9.setObjectName("Note12_9")
        self.Sheet.addWidget(self.Note12_9, 5, 11, 1, 1)
        self.Note6_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_6.sizePolicy().hasHeightForWidth())
        self.Note6_6.setSizePolicy(sizePolicy)
        self.Note6_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_6.setText("")
        self.Note6_6.setCheckable(True)
        self.Note6_6.setObjectName("Note6_6")
        self.Sheet.addWidget(self.Note6_6, 8, 5, 1, 1)
        self.Note8_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_6.sizePolicy().hasHeightForWidth())
        self.Note8_6.setSizePolicy(sizePolicy)
        self.Note8_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_6.setText("")
        self.Note8_6.setCheckable(True)
        self.Note8_6.setObjectName("Note8_6")
        self.Sheet.addWidget(self.Note8_6, 8, 7, 1, 1)
        self.Note13_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_12.sizePolicy().hasHeightForWidth())
        self.Note13_12.setSizePolicy(sizePolicy)
        self.Note13_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_12.setText("")
        self.Note13_12.setCheckable(True)
        self.Note13_12.setObjectName("Note13_12")
        self.Sheet.addWidget(self.Note13_12, 2, 12, 1, 1)
        self.Note13_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_5.sizePolicy().hasHeightForWidth())
        self.Note13_5.setSizePolicy(sizePolicy)
        self.Note13_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_5.setText("")
        self.Note13_5.setCheckable(True)
        self.Note13_5.setObjectName("Note13_5")
        self.Sheet.addWidget(self.Note13_5, 9, 12, 1, 1)
        self.Note5_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_5.sizePolicy().hasHeightForWidth())
        self.Note5_5.setSizePolicy(sizePolicy)
        self.Note5_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_5.setText("")
        self.Note5_5.setCheckable(True)
        self.Note5_5.setObjectName("Note5_5")
        self.Sheet.addWidget(self.Note5_5, 9, 4, 1, 1)
        self.Note12_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_10.sizePolicy().hasHeightForWidth())
        self.Note12_10.setSizePolicy(sizePolicy)
        self.Note12_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_10.setText("")
        self.Note12_10.setCheckable(True)
        self.Note12_10.setObjectName("Note12_10")
        self.Sheet.addWidget(self.Note12_10, 4, 11, 1, 1)
        self.Note5_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_13.sizePolicy().hasHeightForWidth())
        self.Note5_13.setSizePolicy(sizePolicy)
        self.Note5_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_13.setText("")
        self.Note5_13.setCheckable(True)
        self.Note5_13.setObjectName("Note5_13")
        self.Sheet.addWidget(self.Note5_13, 1, 4, 1, 1)
        self.Note7_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_4.sizePolicy().hasHeightForWidth())
        self.Note7_4.setSizePolicy(sizePolicy)
        self.Note7_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_4.setText("")
        self.Note7_4.setCheckable(True)
        self.Note7_4.setObjectName("Note7_4")
        self.Sheet.addWidget(self.Note7_4, 10, 6, 1, 1)
        self.Note7_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_8.sizePolicy().hasHeightForWidth())
        self.Note7_8.setSizePolicy(sizePolicy)
        self.Note7_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_8.setText("")
        self.Note7_8.setCheckable(True)
        self.Note7_8.setObjectName("Note7_8")
        self.Sheet.addWidget(self.Note7_8, 6, 6, 1, 1)
        self.Note7_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_12.sizePolicy().hasHeightForWidth())
        self.Note7_12.setSizePolicy(sizePolicy)
        self.Note7_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_12.setText("")
        self.Note7_12.setCheckable(True)
        self.Note7_12.setObjectName("Note7_12")
        self.Sheet.addWidget(self.Note7_12, 2, 6, 1, 1)
        self.Note7_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_3.sizePolicy().hasHeightForWidth())
        self.Note7_3.setSizePolicy(sizePolicy)
        self.Note7_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_3.setText("")
        self.Note7_3.setCheckable(True)
        self.Note7_3.setObjectName("Note7_3")
        self.Sheet.addWidget(self.Note7_3, 11, 6, 1, 1)
        self.Note7_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_5.sizePolicy().hasHeightForWidth())
        self.Note7_5.setSizePolicy(sizePolicy)
        self.Note7_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_5.setText("")
        self.Note7_5.setCheckable(True)
        self.Note7_5.setObjectName("Note7_5")
        self.Sheet.addWidget(self.Note7_5, 9, 6, 1, 1)
        self.Note7_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_6.sizePolicy().hasHeightForWidth())
        self.Note7_6.setSizePolicy(sizePolicy)
        self.Note7_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_6.setText("")
        self.Note7_6.setCheckable(True)
        self.Note7_6.setObjectName("Note7_6")
        self.Sheet.addWidget(self.Note7_6, 8, 6, 1, 1)
        self.Note7_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_9.sizePolicy().hasHeightForWidth())
        self.Note7_9.setSizePolicy(sizePolicy)
        self.Note7_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_9.setText("")
        self.Note7_9.setCheckable(True)
        self.Note7_9.setObjectName("Note7_9")
        self.Sheet.addWidget(self.Note7_9, 5, 6, 1, 1)
        self.Note8_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_3.sizePolicy().hasHeightForWidth())
        self.Note8_3.setSizePolicy(sizePolicy)
        self.Note8_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_3.setText("")
        self.Note8_3.setCheckable(True)
        self.Note8_3.setObjectName("Note8_3")
        self.Sheet.addWidget(self.Note8_3, 11, 7, 1, 1)
        self.Note7_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_11.sizePolicy().hasHeightForWidth())
        self.Note7_11.setSizePolicy(sizePolicy)
        self.Note7_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_11.setText("")
        self.Note7_11.setCheckable(True)
        self.Note7_11.setObjectName("Note7_11")
        self.Sheet.addWidget(self.Note7_11, 3, 6, 1, 1)
        self.Note7_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_10.sizePolicy().hasHeightForWidth())
        self.Note7_10.setSizePolicy(sizePolicy)
        self.Note7_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_10.setText("")
        self.Note7_10.setCheckable(True)
        self.Note7_10.setObjectName("Note7_10")
        self.Sheet.addWidget(self.Note7_10, 4, 6, 1, 1)
        self.Note7_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_7.sizePolicy().hasHeightForWidth())
        self.Note7_7.setSizePolicy(sizePolicy)
        self.Note7_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_7.setText("")
        self.Note7_7.setCheckable(True)
        self.Note7_7.setObjectName("Note7_7")
        self.Sheet.addWidget(self.Note7_7, 7, 6, 1, 1)
        self.Note8_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_4.sizePolicy().hasHeightForWidth())
        self.Note8_4.setSizePolicy(sizePolicy)
        self.Note8_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_4.setText("")
        self.Note8_4.setCheckable(True)
        self.Note8_4.setObjectName("Note8_4")
        self.Sheet.addWidget(self.Note8_4, 10, 7, 1, 1)
        self.Note8_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_2.sizePolicy().hasHeightForWidth())
        self.Note8_2.setSizePolicy(sizePolicy)
        self.Note8_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_2.setText("")
        self.Note8_2.setCheckable(True)
        self.Note8_2.setObjectName("Note8_2")
        self.Sheet.addWidget(self.Note8_2, 12, 7, 1, 1)
        self.Note7_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_13.sizePolicy().hasHeightForWidth())
        self.Note7_13.setSizePolicy(sizePolicy)
        self.Note7_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_13.setText("")
        self.Note7_13.setCheckable(True)
        self.Note7_13.setObjectName("Note7_13")
        self.Sheet.addWidget(self.Note7_13, 1, 6, 1, 1)
        self.Note13_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_8.sizePolicy().hasHeightForWidth())
        self.Note13_8.setSizePolicy(sizePolicy)
        self.Note13_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_8.setText("")
        self.Note13_8.setCheckable(True)
        self.Note13_8.setObjectName("Note13_8")
        self.Sheet.addWidget(self.Note13_8, 6, 12, 1, 1)
        self.Note15_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_2.sizePolicy().hasHeightForWidth())
        self.Note15_2.setSizePolicy(sizePolicy)
        self.Note15_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_2.setText("")
        self.Note15_2.setCheckable(True)
        self.Note15_2.setObjectName("Note15_2")
        self.Sheet.addWidget(self.Note15_2, 12, 14, 1, 1)
        self.Note3_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_5.sizePolicy().hasHeightForWidth())
        self.Note3_5.setSizePolicy(sizePolicy)
        self.Note3_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_5.setText("")
        self.Note3_5.setCheckable(True)
        self.Note3_5.setObjectName("Note3_5")
        self.Sheet.addWidget(self.Note3_5, 9, 2, 1, 1)
        self.Note3_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_11.sizePolicy().hasHeightForWidth())
        self.Note3_11.setSizePolicy(sizePolicy)
        self.Note3_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_11.setText("")
        self.Note3_11.setCheckable(True)
        self.Note3_11.setObjectName("Note3_11")
        self.Sheet.addWidget(self.Note3_11, 3, 2, 1, 1)
        self.Note3_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_8.sizePolicy().hasHeightForWidth())
        self.Note3_8.setSizePolicy(sizePolicy)
        self.Note3_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_8.setText("")
        self.Note3_8.setCheckable(True)
        self.Note3_8.setObjectName("Note3_8")
        self.Sheet.addWidget(self.Note3_8, 6, 2, 1, 1)
        self.Note4_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_1.sizePolicy().hasHeightForWidth())
        self.Note4_1.setSizePolicy(sizePolicy)
        self.Note4_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_1.setText("")
        self.Note4_1.setCheckable(True)
        self.Note4_1.setObjectName("Note4_1")
        self.Sheet.addWidget(self.Note4_1, 13, 3, 1, 1)
        self.Note1_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_1.sizePolicy().hasHeightForWidth())
        self.Note1_1.setSizePolicy(sizePolicy)
        self.Note1_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_1.setText("")
        self.Note1_1.setCheckable(True)
        self.Note1_1.setObjectName("Note1_1")
        self.Sheet.addWidget(self.Note1_1, 13, 0, 1, 1)
        self.Note2_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_2.sizePolicy().hasHeightForWidth())
        self.Note2_2.setSizePolicy(sizePolicy)
        self.Note2_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_2.setText("")
        self.Note2_2.setCheckable(True)
        self.Note2_2.setObjectName("Note2_2")
        self.Sheet.addWidget(self.Note2_2, 12, 1, 1, 1)
        self.Note1_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_4.sizePolicy().hasHeightForWidth())
        self.Note1_4.setSizePolicy(sizePolicy)
        self.Note1_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_4.setText("")
        self.Note1_4.setCheckable(True)
        self.Note1_4.setObjectName("Note1_4")
        self.Sheet.addWidget(self.Note1_4, 10, 0, 1, 1)
        self.Note1_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_3.sizePolicy().hasHeightForWidth())
        self.Note1_3.setSizePolicy(sizePolicy)
        self.Note1_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_3.setText("")
        self.Note1_3.setCheckable(True)
        self.Note1_3.setObjectName("Note1_3")
        self.Sheet.addWidget(self.Note1_3, 11, 0, 1, 1)
        self.Note1_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_2.sizePolicy().hasHeightForWidth())
        self.Note1_2.setSizePolicy(sizePolicy)
        self.Note1_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_2.setText("")
        self.Note1_2.setCheckable(True)
        self.Note1_2.setObjectName("Note1_2")
        self.Sheet.addWidget(self.Note1_2, 12, 0, 1, 1)
        self.Note1_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_9.sizePolicy().hasHeightForWidth())
        self.Note1_9.setSizePolicy(sizePolicy)
        self.Note1_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_9.setText("")
        self.Note1_9.setCheckable(True)
        self.Note1_9.setObjectName("Note1_9")
        self.Sheet.addWidget(self.Note1_9, 5, 0, 1, 1)
        self.Note1_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_7.sizePolicy().hasHeightForWidth())
        self.Note1_7.setSizePolicy(sizePolicy)
        self.Note1_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_7.setText("")
        self.Note1_7.setCheckable(True)
        self.Note1_7.setObjectName("Note1_7")
        self.Sheet.addWidget(self.Note1_7, 7, 0, 1, 1)
        self.Note1_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_6.sizePolicy().hasHeightForWidth())
        self.Note1_6.setSizePolicy(sizePolicy)
        self.Note1_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_6.setText("")
        self.Note1_6.setCheckable(True)
        self.Note1_6.setObjectName("Note1_6")
        self.Sheet.addWidget(self.Note1_6, 8, 0, 1, 1)
        self.Note1_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_5.sizePolicy().hasHeightForWidth())
        self.Note1_5.setSizePolicy(sizePolicy)
        self.Note1_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_5.setText("")
        self.Note1_5.setCheckable(True)
        self.Note1_5.setObjectName("Note1_5")
        self.Sheet.addWidget(self.Note1_5, 9, 0, 1, 1)
        self.Note1_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_8.sizePolicy().hasHeightForWidth())
        self.Note1_8.setSizePolicy(sizePolicy)
        self.Note1_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_8.setText("")
        self.Note1_8.setCheckable(True)
        self.Note1_8.setObjectName("Note1_8")
        self.Sheet.addWidget(self.Note1_8, 6, 0, 1, 1)
        self.Note1_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_10.sizePolicy().hasHeightForWidth())
        self.Note1_10.setSizePolicy(sizePolicy)
        self.Note1_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_10.setText("")
        self.Note1_10.setCheckable(True)
        self.Note1_10.setObjectName("Note1_10")
        self.Sheet.addWidget(self.Note1_10, 4, 0, 1, 1)
        self.Note1_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_11.sizePolicy().hasHeightForWidth())
        self.Note1_11.setSizePolicy(sizePolicy)
        self.Note1_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_11.setText("")
        self.Note1_11.setCheckable(True)
        self.Note1_11.setObjectName("Note1_11")
        self.Sheet.addWidget(self.Note1_11, 3, 0, 1, 1)
        self.Note1_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_12.sizePolicy().hasHeightForWidth())
        self.Note1_12.setSizePolicy(sizePolicy)
        self.Note1_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_12.setText("")
        self.Note1_12.setCheckable(True)
        self.Note1_12.setObjectName("Note1_12")
        self.Sheet.addWidget(self.Note1_12, 2, 0, 1, 1)
        self.Note2_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_10.sizePolicy().hasHeightForWidth())
        self.Note2_10.setSizePolicy(sizePolicy)
        self.Note2_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_10.setText("")
        self.Note2_10.setCheckable(True)
        self.Note2_10.setObjectName("Note2_10")
        self.Sheet.addWidget(self.Note2_10, 4, 1, 1, 1)
        self.Note3_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_12.sizePolicy().hasHeightForWidth())
        self.Note3_12.setSizePolicy(sizePolicy)
        self.Note3_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_12.setText("")
        self.Note3_12.setCheckable(True)
        self.Note3_12.setObjectName("Note3_12")
        self.Sheet.addWidget(self.Note3_12, 2, 2, 1, 1)
        self.Note3_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_9.sizePolicy().hasHeightForWidth())
        self.Note3_9.setSizePolicy(sizePolicy)
        self.Note3_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_9.setText("")
        self.Note3_9.setCheckable(True)
        self.Note3_9.setObjectName("Note3_9")
        self.Sheet.addWidget(self.Note3_9, 5, 2, 1, 1)
        self.Note3_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_6.sizePolicy().hasHeightForWidth())
        self.Note3_6.setSizePolicy(sizePolicy)
        self.Note3_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_6.setText("")
        self.Note3_6.setCheckable(True)
        self.Note3_6.setObjectName("Note3_6")
        self.Sheet.addWidget(self.Note3_6, 8, 2, 1, 1)
        self.Note3_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_10.sizePolicy().hasHeightForWidth())
        self.Note3_10.setSizePolicy(sizePolicy)
        self.Note3_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_10.setText("")
        self.Note3_10.setCheckable(True)
        self.Note3_10.setObjectName("Note3_10")
        self.Sheet.addWidget(self.Note3_10, 4, 2, 1, 1)
        self.Note3_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_7.sizePolicy().hasHeightForWidth())
        self.Note3_7.setSizePolicy(sizePolicy)
        self.Note3_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_7.setText("")
        self.Note3_7.setCheckable(True)
        self.Note3_7.setObjectName("Note3_7")
        self.Sheet.addWidget(self.Note3_7, 7, 2, 1, 1)
        self.Note5_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_1.sizePolicy().hasHeightForWidth())
        self.Note5_1.setSizePolicy(sizePolicy)
        self.Note5_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_1.setText("")
        self.Note5_1.setCheckable(True)
        self.Note5_1.setObjectName("Note5_1")
        self.Sheet.addWidget(self.Note5_1, 13, 4, 1, 1)
        self.Note3_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_13.sizePolicy().hasHeightForWidth())
        self.Note3_13.setSizePolicy(sizePolicy)
        self.Note3_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_13.setText("")
        self.Note3_13.setCheckable(True)
        self.Note3_13.setObjectName("Note3_13")
        self.Sheet.addWidget(self.Note3_13, 1, 2, 1, 1)
        self.Note2_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_3.sizePolicy().hasHeightForWidth())
        self.Note2_3.setSizePolicy(sizePolicy)
        self.Note2_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_3.setText("")
        self.Note2_3.setCheckable(True)
        self.Note2_3.setObjectName("Note2_3")
        self.Sheet.addWidget(self.Note2_3, 11, 1, 1, 1)
        self.Note2_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_11.sizePolicy().hasHeightForWidth())
        self.Note2_11.setSizePolicy(sizePolicy)
        self.Note2_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_11.setText("")
        self.Note2_11.setCheckable(True)
        self.Note2_11.setObjectName("Note2_11")
        self.Sheet.addWidget(self.Note2_11, 3, 1, 1, 1)
        self.Note2_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_1.sizePolicy().hasHeightForWidth())
        self.Note2_1.setSizePolicy(sizePolicy)
        self.Note2_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_1.setText("")
        self.Note2_1.setCheckable(True)
        self.Note2_1.setObjectName("Note2_1")
        self.Sheet.addWidget(self.Note2_1, 13, 1, 1, 1)
        self.Note2_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_8.sizePolicy().hasHeightForWidth())
        self.Note2_8.setSizePolicy(sizePolicy)
        self.Note2_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_8.setText("")
        self.Note2_8.setCheckable(True)
        self.Note2_8.setObjectName("Note2_8")
        self.Sheet.addWidget(self.Note2_8, 6, 1, 1, 1)
        self.Note3_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_1.sizePolicy().hasHeightForWidth())
        self.Note3_1.setSizePolicy(sizePolicy)
        self.Note3_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_1.setText("")
        self.Note3_1.setCheckable(True)
        self.Note3_1.setObjectName("Note3_1")
        self.Sheet.addWidget(self.Note3_1, 13, 2, 1, 1)
        self.Note2_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_6.sizePolicy().hasHeightForWidth())
        self.Note2_6.setSizePolicy(sizePolicy)
        self.Note2_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_6.setText("")
        self.Note2_6.setCheckable(True)
        self.Note2_6.setObjectName("Note2_6")
        self.Sheet.addWidget(self.Note2_6, 8, 1, 1, 1)
        self.Note2_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_4.sizePolicy().hasHeightForWidth())
        self.Note2_4.setSizePolicy(sizePolicy)
        self.Note2_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_4.setText("")
        self.Note2_4.setCheckable(True)
        self.Note2_4.setObjectName("Note2_4")
        self.Sheet.addWidget(self.Note2_4, 10, 1, 1, 1)
        self.Note3_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_4.sizePolicy().hasHeightForWidth())
        self.Note3_4.setSizePolicy(sizePolicy)
        self.Note3_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_4.setText("")
        self.Note3_4.setCheckable(True)
        self.Note3_4.setObjectName("Note3_4")
        self.Sheet.addWidget(self.Note3_4, 10, 2, 1, 1)
        self.Note2_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_7.sizePolicy().hasHeightForWidth())
        self.Note2_7.setSizePolicy(sizePolicy)
        self.Note2_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_7.setText("")
        self.Note2_7.setCheckable(True)
        self.Note2_7.setObjectName("Note2_7")
        self.Sheet.addWidget(self.Note2_7, 7, 1, 1, 1)
        self.Note1_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note1_13.sizePolicy().hasHeightForWidth())
        self.Note1_13.setSizePolicy(sizePolicy)
        self.Note1_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note1_13.setText("")
        self.Note1_13.setCheckable(True)
        self.Note1_13.setObjectName("Note1_13")
        self.Sheet.addWidget(self.Note1_13, 1, 0, 1, 1)
        self.Note2_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_5.sizePolicy().hasHeightForWidth())
        self.Note2_5.setSizePolicy(sizePolicy)
        self.Note2_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_5.setText("")
        self.Note2_5.setCheckable(True)
        self.Note2_5.setObjectName("Note2_5")
        self.Sheet.addWidget(self.Note2_5, 9, 1, 1, 1)
        self.Note2_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_12.sizePolicy().hasHeightForWidth())
        self.Note2_12.setSizePolicy(sizePolicy)
        self.Note2_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_12.setText("")
        self.Note2_12.setCheckable(True)
        self.Note2_12.setObjectName("Note2_12")
        self.Sheet.addWidget(self.Note2_12, 2, 1, 1, 1)
        self.Note2_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_13.sizePolicy().hasHeightForWidth())
        self.Note2_13.setSizePolicy(sizePolicy)
        self.Note2_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_13.setText("")
        self.Note2_13.setCheckable(True)
        self.Note2_13.setObjectName("Note2_13")
        self.Sheet.addWidget(self.Note2_13, 1, 1, 1, 1)
        self.Note3_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_2.sizePolicy().hasHeightForWidth())
        self.Note3_2.setSizePolicy(sizePolicy)
        self.Note3_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_2.setText("")
        self.Note3_2.setCheckable(True)
        self.Note3_2.setObjectName("Note3_2")
        self.Sheet.addWidget(self.Note3_2, 12, 2, 1, 1)
        self.Note2_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note2_9.sizePolicy().hasHeightForWidth())
        self.Note2_9.setSizePolicy(sizePolicy)
        self.Note2_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note2_9.setText("")
        self.Note2_9.setCheckable(True)
        self.Note2_9.setObjectName("Note2_9")
        self.Sheet.addWidget(self.Note2_9, 5, 1, 1, 1)
        self.Note3_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note3_3.sizePolicy().hasHeightForWidth())
        self.Note3_3.setSizePolicy(sizePolicy)
        self.Note3_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note3_3.setText("")
        self.Note3_3.setCheckable(True)
        self.Note3_3.setObjectName("Note3_3")
        self.Sheet.addWidget(self.Note3_3, 11, 2, 1, 1)
        self.Note7_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_1.sizePolicy().hasHeightForWidth())
        self.Note7_1.setSizePolicy(sizePolicy)
        self.Note7_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_1.setText("")
        self.Note7_1.setCheckable(True)
        self.Note7_1.setObjectName("Note7_1")
        self.Sheet.addWidget(self.Note7_1, 13, 6, 1, 1)
        self.Note6_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_1.sizePolicy().hasHeightForWidth())
        self.Note6_1.setSizePolicy(sizePolicy)
        self.Note6_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_1.setText("")
        self.Note6_1.setCheckable(True)
        self.Note6_1.setObjectName("Note6_1")
        self.Sheet.addWidget(self.Note6_1, 13, 5, 1, 1)
        self.Note16_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_9.sizePolicy().hasHeightForWidth())
        self.Note16_9.setSizePolicy(sizePolicy)
        self.Note16_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_9.setText("")
        self.Note16_9.setCheckable(True)
        self.Note16_9.setObjectName("Note16_9")
        self.Sheet.addWidget(self.Note16_9, 5, 15, 1, 1)
        self.Note16_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_8.sizePolicy().hasHeightForWidth())
        self.Note16_8.setSizePolicy(sizePolicy)
        self.Note16_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_8.setText("")
        self.Note16_8.setCheckable(True)
        self.Note16_8.setObjectName("Note16_8")
        self.Sheet.addWidget(self.Note16_8, 6, 15, 1, 1)
        self.Note17_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_8.sizePolicy().hasHeightForWidth())
        self.Note17_8.setSizePolicy(sizePolicy)
        self.Note17_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_8.setText("")
        self.Note17_8.setCheckable(True)
        self.Note17_8.setObjectName("Note17_8")
        self.Sheet.addWidget(self.Note17_8, 6, 16, 1, 1)
        self.Note16_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_6.sizePolicy().hasHeightForWidth())
        self.Note16_6.setSizePolicy(sizePolicy)
        self.Note16_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_6.setText("")
        self.Note16_6.setCheckable(True)
        self.Note16_6.setObjectName("Note16_6")
        self.Sheet.addWidget(self.Note16_6, 8, 15, 1, 1)
        self.Note16_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_10.sizePolicy().hasHeightForWidth())
        self.Note16_10.setSizePolicy(sizePolicy)
        self.Note16_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_10.setText("")
        self.Note16_10.setCheckable(True)
        self.Note16_10.setObjectName("Note16_10")
        self.Sheet.addWidget(self.Note16_10, 4, 15, 1, 1)
        self.Note17_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_6.sizePolicy().hasHeightForWidth())
        self.Note17_6.setSizePolicy(sizePolicy)
        self.Note17_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_6.setText("")
        self.Note17_6.setCheckable(True)
        self.Note17_6.setObjectName("Note17_6")
        self.Sheet.addWidget(self.Note17_6, 8, 16, 1, 1)
        self.Note16_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_7.sizePolicy().hasHeightForWidth())
        self.Note16_7.setSizePolicy(sizePolicy)
        self.Note16_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_7.setText("")
        self.Note16_7.setCheckable(True)
        self.Note16_7.setObjectName("Note16_7")
        self.Sheet.addWidget(self.Note16_7, 7, 15, 1, 1)
        self.Note17_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_7.sizePolicy().hasHeightForWidth())
        self.Note17_7.setSizePolicy(sizePolicy)
        self.Note17_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_7.setText("")
        self.Note17_7.setCheckable(True)
        self.Note17_7.setObjectName("Note17_7")
        self.Sheet.addWidget(self.Note17_7, 7, 16, 1, 1)
        self.Note17_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_9.sizePolicy().hasHeightForWidth())
        self.Note17_9.setSizePolicy(sizePolicy)
        self.Note17_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_9.setText("")
        self.Note17_9.setCheckable(True)
        self.Note17_9.setObjectName("Note17_9")
        self.Sheet.addWidget(self.Note17_9, 5, 16, 1, 1)
        self.Note17_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_10.sizePolicy().hasHeightForWidth())
        self.Note17_10.setSizePolicy(sizePolicy)
        self.Note17_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_10.setText("")
        self.Note17_10.setCheckable(True)
        self.Note17_10.setObjectName("Note17_10")
        self.Sheet.addWidget(self.Note17_10, 4, 16, 1, 1)
        self.Note5_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_9.sizePolicy().hasHeightForWidth())
        self.Note5_9.setSizePolicy(sizePolicy)
        self.Note5_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_9.setText("")
        self.Note5_9.setCheckable(True)
        self.Note5_9.setObjectName("Note5_9")
        self.Sheet.addWidget(self.Note5_9, 5, 4, 1, 1)
        self.Note6_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_13.sizePolicy().hasHeightForWidth())
        self.Note6_13.setSizePolicy(sizePolicy)
        self.Note6_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_13.setText("")
        self.Note6_13.setCheckable(True)
        self.Note6_13.setObjectName("Note6_13")
        self.Sheet.addWidget(self.Note6_13, 1, 5, 1, 1)
        self.Note6_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_3.sizePolicy().hasHeightForWidth())
        self.Note6_3.setSizePolicy(sizePolicy)
        self.Note6_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_3.setText("")
        self.Note6_3.setCheckable(True)
        self.Note6_3.setObjectName("Note6_3")
        self.Sheet.addWidget(self.Note6_3, 11, 5, 1, 1)
        self.Note6_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_12.sizePolicy().hasHeightForWidth())
        self.Note6_12.setSizePolicy(sizePolicy)
        self.Note6_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_12.setText("")
        self.Note6_12.setCheckable(True)
        self.Note6_12.setObjectName("Note6_12")
        self.Sheet.addWidget(self.Note6_12, 2, 5, 1, 1)
        self.Note4_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_2.sizePolicy().hasHeightForWidth())
        self.Note4_2.setSizePolicy(sizePolicy)
        self.Note4_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_2.setText("")
        self.Note4_2.setCheckable(True)
        self.Note4_2.setObjectName("Note4_2")
        self.Sheet.addWidget(self.Note4_2, 12, 3, 1, 1)
        self.Note6_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_10.sizePolicy().hasHeightForWidth())
        self.Note6_10.setSizePolicy(sizePolicy)
        self.Note6_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_10.setText("")
        self.Note6_10.setCheckable(True)
        self.Note6_10.setObjectName("Note6_10")
        self.Sheet.addWidget(self.Note6_10, 4, 5, 1, 1)
        self.Note5_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_12.sizePolicy().hasHeightForWidth())
        self.Note5_12.setSizePolicy(sizePolicy)
        self.Note5_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_12.setText("")
        self.Note5_12.setCheckable(True)
        self.Note5_12.setObjectName("Note5_12")
        self.Sheet.addWidget(self.Note5_12, 2, 4, 1, 1)
        self.Note7_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note7_2.sizePolicy().hasHeightForWidth())
        self.Note7_2.setSizePolicy(sizePolicy)
        self.Note7_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note7_2.setText("")
        self.Note7_2.setCheckable(True)
        self.Note7_2.setObjectName("Note7_2")
        self.Sheet.addWidget(self.Note7_2, 12, 6, 1, 1)
        self.Note12_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_13.sizePolicy().hasHeightForWidth())
        self.Note12_13.setSizePolicy(sizePolicy)
        self.Note12_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_13.setText("")
        self.Note12_13.setCheckable(True)
        self.Note12_13.setObjectName("Note12_13")
        self.Sheet.addWidget(self.Note12_13, 1, 11, 1, 1)
        self.Note11_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_6.sizePolicy().hasHeightForWidth())
        self.Note11_6.setSizePolicy(sizePolicy)
        self.Note11_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_6.setText("")
        self.Note11_6.setCheckable(True)
        self.Note11_6.setObjectName("Note11_6")
        self.Sheet.addWidget(self.Note11_6, 8, 10, 1, 1)
        self.Note12_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_7.sizePolicy().hasHeightForWidth())
        self.Note12_7.setSizePolicy(sizePolicy)
        self.Note12_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_7.setText("")
        self.Note12_7.setCheckable(True)
        self.Note12_7.setObjectName("Note12_7")
        self.Sheet.addWidget(self.Note12_7, 7, 11, 1, 1)
        self.Note13_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_3.sizePolicy().hasHeightForWidth())
        self.Note13_3.setSizePolicy(sizePolicy)
        self.Note13_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_3.setText("")
        self.Note13_3.setCheckable(True)
        self.Note13_3.setObjectName("Note13_3")
        self.Sheet.addWidget(self.Note13_3, 11, 12, 1, 1)
        self.Note10_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_11.sizePolicy().hasHeightForWidth())
        self.Note10_11.setSizePolicy(sizePolicy)
        self.Note10_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_11.setText("")
        self.Note10_11.setCheckable(True)
        self.Note10_11.setObjectName("Note10_11")
        self.Sheet.addWidget(self.Note10_11, 3, 9, 1, 1)
        self.Note17_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_4.sizePolicy().hasHeightForWidth())
        self.Note17_4.setSizePolicy(sizePolicy)
        self.Note17_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_4.setText("")
        self.Note17_4.setCheckable(True)
        self.Note17_4.setObjectName("Note17_4")
        self.Sheet.addWidget(self.Note17_4, 10, 16, 1, 1)
        self.Note11_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_2.sizePolicy().hasHeightForWidth())
        self.Note11_2.setSizePolicy(sizePolicy)
        self.Note11_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_2.setText("")
        self.Note11_2.setCheckable(True)
        self.Note11_2.setObjectName("Note11_2")
        self.Sheet.addWidget(self.Note11_2, 12, 10, 1, 1)
        self.Note11_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_3.sizePolicy().hasHeightForWidth())
        self.Note11_3.setSizePolicy(sizePolicy)
        self.Note11_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_3.setText("")
        self.Note11_3.setCheckable(True)
        self.Note11_3.setObjectName("Note11_3")
        self.Sheet.addWidget(self.Note11_3, 11, 10, 1, 1)
        self.Note10_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_13.sizePolicy().hasHeightForWidth())
        self.Note10_13.setSizePolicy(sizePolicy)
        self.Note10_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_13.setText("")
        self.Note10_13.setCheckable(True)
        self.Note10_13.setObjectName("Note10_13")
        self.Sheet.addWidget(self.Note10_13, 1, 9, 1, 1)
        self.Note11_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_4.sizePolicy().hasHeightForWidth())
        self.Note11_4.setSizePolicy(sizePolicy)
        self.Note11_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_4.setText("")
        self.Note11_4.setCheckable(True)
        self.Note11_4.setObjectName("Note11_4")
        self.Sheet.addWidget(self.Note11_4, 10, 10, 1, 1)
        self.Note11_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_5.sizePolicy().hasHeightForWidth())
        self.Note11_5.setSizePolicy(sizePolicy)
        self.Note11_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_5.setText("")
        self.Note11_5.setCheckable(True)
        self.Note11_5.setObjectName("Note11_5")
        self.Sheet.addWidget(self.Note11_5, 9, 10, 1, 1)
        self.Note10_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_10.sizePolicy().hasHeightForWidth())
        self.Note10_10.setSizePolicy(sizePolicy)
        self.Note10_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_10.setText("")
        self.Note10_10.setCheckable(True)
        self.Note10_10.setObjectName("Note10_10")
        self.Sheet.addWidget(self.Note10_10, 4, 9, 1, 1)
        self.Note11_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_7.sizePolicy().hasHeightForWidth())
        self.Note11_7.setSizePolicy(sizePolicy)
        self.Note11_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_7.setText("")
        self.Note11_7.setCheckable(True)
        self.Note11_7.setObjectName("Note11_7")
        self.Sheet.addWidget(self.Note11_7, 7, 10, 1, 1)
        self.Note10_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_8.sizePolicy().hasHeightForWidth())
        self.Note10_8.setSizePolicy(sizePolicy)
        self.Note10_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_8.setText("")
        self.Note10_8.setCheckable(True)
        self.Note10_8.setObjectName("Note10_8")
        self.Sheet.addWidget(self.Note10_8, 6, 9, 1, 1)
        self.Note11_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_9.sizePolicy().hasHeightForWidth())
        self.Note11_9.setSizePolicy(sizePolicy)
        self.Note11_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_9.setText("")
        self.Note11_9.setCheckable(True)
        self.Note11_9.setObjectName("Note11_9")
        self.Sheet.addWidget(self.Note11_9, 5, 10, 1, 1)
        self.Note11_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_10.sizePolicy().hasHeightForWidth())
        self.Note11_10.setSizePolicy(sizePolicy)
        self.Note11_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_10.setText("")
        self.Note11_10.setCheckable(True)
        self.Note11_10.setObjectName("Note11_10")
        self.Sheet.addWidget(self.Note11_10, 4, 10, 1, 1)
        self.Note11_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_13.sizePolicy().hasHeightForWidth())
        self.Note11_13.setSizePolicy(sizePolicy)
        self.Note11_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_13.setText("")
        self.Note11_13.setCheckable(True)
        self.Note11_13.setObjectName("Note11_13")
        self.Sheet.addWidget(self.Note11_13, 1, 10, 1, 1)
        self.Note12_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_4.sizePolicy().hasHeightForWidth())
        self.Note12_4.setSizePolicy(sizePolicy)
        self.Note12_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_4.setText("")
        self.Note12_4.setCheckable(True)
        self.Note12_4.setObjectName("Note12_4")
        self.Sheet.addWidget(self.Note12_4, 10, 11, 1, 1)
        self.Note12_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_5.sizePolicy().hasHeightForWidth())
        self.Note12_5.setSizePolicy(sizePolicy)
        self.Note12_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_5.setText("")
        self.Note12_5.setCheckable(True)
        self.Note12_5.setObjectName("Note12_5")
        self.Sheet.addWidget(self.Note12_5, 9, 11, 1, 1)
        self.Note12_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_8.sizePolicy().hasHeightForWidth())
        self.Note12_8.setSizePolicy(sizePolicy)
        self.Note12_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_8.setText("")
        self.Note12_8.setCheckable(True)
        self.Note12_8.setObjectName("Note12_8")
        self.Sheet.addWidget(self.Note12_8, 6, 11, 1, 1)
        self.Note11_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_11.sizePolicy().hasHeightForWidth())
        self.Note11_11.setSizePolicy(sizePolicy)
        self.Note11_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_11.setText("")
        self.Note11_11.setCheckable(True)
        self.Note11_11.setObjectName("Note11_11")
        self.Sheet.addWidget(self.Note11_11, 3, 10, 1, 1)
        self.Note12_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_2.sizePolicy().hasHeightForWidth())
        self.Note12_2.setSizePolicy(sizePolicy)
        self.Note12_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_2.setText("")
        self.Note12_2.setCheckable(True)
        self.Note12_2.setObjectName("Note12_2")
        self.Sheet.addWidget(self.Note12_2, 12, 11, 1, 1)
        self.Note13_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_10.sizePolicy().hasHeightForWidth())
        self.Note13_10.setSizePolicy(sizePolicy)
        self.Note13_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_10.setText("")
        self.Note13_10.setCheckable(True)
        self.Note13_10.setObjectName("Note13_10")
        self.Sheet.addWidget(self.Note13_10, 4, 12, 1, 1)
        self.Note12_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_3.sizePolicy().hasHeightForWidth())
        self.Note12_3.setSizePolicy(sizePolicy)
        self.Note12_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_3.setText("")
        self.Note12_3.setCheckable(True)
        self.Note12_3.setObjectName("Note12_3")
        self.Sheet.addWidget(self.Note12_3, 11, 11, 1, 1)
        self.Note11_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_8.sizePolicy().hasHeightForWidth())
        self.Note11_8.setSizePolicy(sizePolicy)
        self.Note11_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_8.setText("")
        self.Note11_8.setCheckable(True)
        self.Note11_8.setObjectName("Note11_8")
        self.Sheet.addWidget(self.Note11_8, 6, 10, 1, 1)
        self.Note11_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_12.sizePolicy().hasHeightForWidth())
        self.Note11_12.setSizePolicy(sizePolicy)
        self.Note11_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_12.setText("")
        self.Note11_12.setCheckable(True)
        self.Note11_12.setObjectName("Note11_12")
        self.Sheet.addWidget(self.Note11_12, 2, 10, 1, 1)
        self.Note10_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_5.sizePolicy().hasHeightForWidth())
        self.Note10_5.setSizePolicy(sizePolicy)
        self.Note10_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_5.setText("")
        self.Note10_5.setCheckable(True)
        self.Note10_5.setObjectName("Note10_5")
        self.Sheet.addWidget(self.Note10_5, 9, 9, 1, 1)
        self.Note10_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_4.sizePolicy().hasHeightForWidth())
        self.Note10_4.setSizePolicy(sizePolicy)
        self.Note10_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_4.setText("")
        self.Note10_4.setCheckable(True)
        self.Note10_4.setObjectName("Note10_4")
        self.Sheet.addWidget(self.Note10_4, 10, 9, 1, 1)
        self.Note12_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_6.sizePolicy().hasHeightForWidth())
        self.Note12_6.setSizePolicy(sizePolicy)
        self.Note12_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_6.setText("")
        self.Note12_6.setCheckable(True)
        self.Note12_6.setObjectName("Note12_6")
        self.Sheet.addWidget(self.Note12_6, 8, 11, 1, 1)
        self.Note10_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_9.sizePolicy().hasHeightForWidth())
        self.Note10_9.setSizePolicy(sizePolicy)
        self.Note10_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_9.setText("")
        self.Note10_9.setCheckable(True)
        self.Note10_9.setObjectName("Note10_9")
        self.Sheet.addWidget(self.Note10_9, 5, 9, 1, 1)
        self.Note10_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_6.sizePolicy().hasHeightForWidth())
        self.Note10_6.setSizePolicy(sizePolicy)
        self.Note10_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_6.setText("")
        self.Note10_6.setCheckable(True)
        self.Note10_6.setObjectName("Note10_6")
        self.Sheet.addWidget(self.Note10_6, 8, 9, 1, 1)
        self.Note10_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_12.sizePolicy().hasHeightForWidth())
        self.Note10_12.setSizePolicy(sizePolicy)
        self.Note10_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_12.setText("")
        self.Note10_12.setCheckable(True)
        self.Note10_12.setObjectName("Note10_12")
        self.Sheet.addWidget(self.Note10_12, 2, 9, 1, 1)
        self.Note10_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_3.sizePolicy().hasHeightForWidth())
        self.Note10_3.setSizePolicy(sizePolicy)
        self.Note10_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_3.setText("")
        self.Note10_3.setCheckable(True)
        self.Note10_3.setObjectName("Note10_3")
        self.Sheet.addWidget(self.Note10_3, 11, 9, 1, 1)
        self.Note10_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_7.sizePolicy().hasHeightForWidth())
        self.Note10_7.setSizePolicy(sizePolicy)
        self.Note10_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_7.setText("")
        self.Note10_7.setCheckable(True)
        self.Note10_7.setObjectName("Note10_7")
        self.Sheet.addWidget(self.Note10_7, 7, 9, 1, 1)
        self.Note15_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_13.sizePolicy().hasHeightForWidth())
        self.Note15_13.setSizePolicy(sizePolicy)
        self.Note15_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_13.setText("")
        self.Note15_13.setCheckable(True)
        self.Note15_13.setObjectName("Note15_13")
        self.Sheet.addWidget(self.Note15_13, 1, 14, 1, 1)
        self.Note9_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_11.sizePolicy().hasHeightForWidth())
        self.Note9_11.setSizePolicy(sizePolicy)
        self.Note9_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_11.setText("")
        self.Note9_11.setCheckable(True)
        self.Note9_11.setObjectName("Note9_11")
        self.Sheet.addWidget(self.Note9_11, 3, 8, 1, 1)
        self.Note8_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_11.sizePolicy().hasHeightForWidth())
        self.Note8_11.setSizePolicy(sizePolicy)
        self.Note8_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_11.setText("")
        self.Note8_11.setCheckable(True)
        self.Note8_11.setObjectName("Note8_11")
        self.Sheet.addWidget(self.Note8_11, 3, 7, 1, 1)
        self.Note17_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_2.sizePolicy().hasHeightForWidth())
        self.Note17_2.setSizePolicy(sizePolicy)
        self.Note17_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_2.setText("")
        self.Note17_2.setCheckable(True)
        self.Note17_2.setObjectName("Note17_2")
        self.Sheet.addWidget(self.Note17_2, 12, 16, 1, 1)
        self.Note8_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_12.sizePolicy().hasHeightForWidth())
        self.Note8_12.setSizePolicy(sizePolicy)
        self.Note8_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_12.setText("")
        self.Note8_12.setCheckable(True)
        self.Note8_12.setObjectName("Note8_12")
        self.Sheet.addWidget(self.Note8_12, 2, 7, 1, 1)
        self.Note8_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_10.sizePolicy().hasHeightForWidth())
        self.Note8_10.setSizePolicy(sizePolicy)
        self.Note8_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_10.setText("")
        self.Note8_10.setCheckable(True)
        self.Note8_10.setObjectName("Note8_10")
        self.Sheet.addWidget(self.Note8_10, 4, 7, 1, 1)
        self.Note16_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_3.sizePolicy().hasHeightForWidth())
        self.Note16_3.setSizePolicy(sizePolicy)
        self.Note16_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_3.setText("")
        self.Note16_3.setCheckable(True)
        self.Note16_3.setObjectName("Note16_3")
        self.Sheet.addWidget(self.Note16_3, 11, 15, 1, 1)
        self.Note8_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_9.sizePolicy().hasHeightForWidth())
        self.Note8_9.setSizePolicy(sizePolicy)
        self.Note8_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_9.setText("")
        self.Note8_9.setCheckable(True)
        self.Note8_9.setObjectName("Note8_9")
        self.Sheet.addWidget(self.Note8_9, 5, 7, 1, 1)
        self.Note8_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_13.sizePolicy().hasHeightForWidth())
        self.Note8_13.setSizePolicy(sizePolicy)
        self.Note8_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_13.setText("")
        self.Note8_13.setCheckable(True)
        self.Note8_13.setObjectName("Note8_13")
        self.Sheet.addWidget(self.Note8_13, 1, 7, 1, 1)
        self.Note9_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_2.sizePolicy().hasHeightForWidth())
        self.Note9_2.setSizePolicy(sizePolicy)
        self.Note9_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_2.setText("")
        self.Note9_2.setCheckable(True)
        self.Note9_2.setObjectName("Note9_2")
        self.Sheet.addWidget(self.Note9_2, 12, 8, 1, 1)
        self.Note8_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_8.sizePolicy().hasHeightForWidth())
        self.Note8_8.setSizePolicy(sizePolicy)
        self.Note8_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_8.setText("")
        self.Note8_8.setCheckable(True)
        self.Note8_8.setObjectName("Note8_8")
        self.Sheet.addWidget(self.Note8_8, 6, 7, 1, 1)
        self.Note13_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_6.sizePolicy().hasHeightForWidth())
        self.Note13_6.setSizePolicy(sizePolicy)
        self.Note13_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_6.setText("")
        self.Note13_6.setCheckable(True)
        self.Note13_6.setObjectName("Note13_6")
        self.Sheet.addWidget(self.Note13_6, 8, 12, 1, 1)
        self.Note16_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_2.sizePolicy().hasHeightForWidth())
        self.Note16_2.setSizePolicy(sizePolicy)
        self.Note16_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_2.setText("")
        self.Note16_2.setCheckable(True)
        self.Note16_2.setObjectName("Note16_2")
        self.Sheet.addWidget(self.Note16_2, 12, 15, 1, 1)
        self.Note14_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_12.sizePolicy().hasHeightForWidth())
        self.Note14_12.setSizePolicy(sizePolicy)
        self.Note14_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_12.setText("")
        self.Note14_12.setCheckable(True)
        self.Note14_12.setObjectName("Note14_12")
        self.Sheet.addWidget(self.Note14_12, 2, 13, 1, 1)
        self.Note9_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_10.sizePolicy().hasHeightForWidth())
        self.Note9_10.setSizePolicy(sizePolicy)
        self.Note9_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_10.setText("")
        self.Note9_10.setCheckable(True)
        self.Note9_10.setObjectName("Note9_10")
        self.Sheet.addWidget(self.Note9_10, 4, 8, 1, 1)
        self.Note9_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_7.sizePolicy().hasHeightForWidth())
        self.Note9_7.setSizePolicy(sizePolicy)
        self.Note9_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_7.setText("")
        self.Note9_7.setCheckable(True)
        self.Note9_7.setObjectName("Note9_7")
        self.Sheet.addWidget(self.Note9_7, 7, 8, 1, 1)
        self.Note14_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_13.sizePolicy().hasHeightForWidth())
        self.Note14_13.setSizePolicy(sizePolicy)
        self.Note14_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_13.setText("")
        self.Note14_13.setCheckable(True)
        self.Note14_13.setObjectName("Note14_13")
        self.Sheet.addWidget(self.Note14_13, 1, 13, 1, 1)
        self.Note12_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_12.sizePolicy().hasHeightForWidth())
        self.Note12_12.setSizePolicy(sizePolicy)
        self.Note12_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_12.setText("")
        self.Note12_12.setCheckable(True)
        self.Note12_12.setObjectName("Note12_12")
        self.Sheet.addWidget(self.Note12_12, 2, 11, 1, 1)
        self.Note9_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_4.sizePolicy().hasHeightForWidth())
        self.Note9_4.setSizePolicy(sizePolicy)
        self.Note9_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_4.setText("")
        self.Note9_4.setCheckable(True)
        self.Note9_4.setObjectName("Note9_4")
        self.Sheet.addWidget(self.Note9_4, 10, 8, 1, 1)
        self.Note15_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_11.sizePolicy().hasHeightForWidth())
        self.Note15_11.setSizePolicy(sizePolicy)
        self.Note15_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_11.setText("")
        self.Note15_11.setCheckable(True)
        self.Note15_11.setObjectName("Note15_11")
        self.Sheet.addWidget(self.Note15_11, 3, 14, 1, 1)
        self.Note16_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_5.sizePolicy().hasHeightForWidth())
        self.Note16_5.setSizePolicy(sizePolicy)
        self.Note16_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_5.setText("")
        self.Note16_5.setCheckable(True)
        self.Note16_5.setObjectName("Note16_5")
        self.Sheet.addWidget(self.Note16_5, 9, 15, 1, 1)
        self.Note9_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_13.sizePolicy().hasHeightForWidth())
        self.Note9_13.setSizePolicy(sizePolicy)
        self.Note9_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_13.setText("")
        self.Note9_13.setCheckable(True)
        self.Note9_13.setObjectName("Note9_13")
        self.Sheet.addWidget(self.Note9_13, 1, 8, 1, 1)
        self.Note15_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_12.sizePolicy().hasHeightForWidth())
        self.Note15_12.setSizePolicy(sizePolicy)
        self.Note15_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_12.setText("")
        self.Note15_12.setCheckable(True)
        self.Note15_12.setObjectName("Note15_12")
        self.Sheet.addWidget(self.Note15_12, 2, 14, 1, 1)
        self.Note9_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_5.sizePolicy().hasHeightForWidth())
        self.Note9_5.setSizePolicy(sizePolicy)
        self.Note9_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_5.setText("")
        self.Note9_5.setCheckable(True)
        self.Note9_5.setObjectName("Note9_5")
        self.Sheet.addWidget(self.Note9_5, 9, 8, 1, 1)
        self.Note9_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_9.sizePolicy().hasHeightForWidth())
        self.Note9_9.setSizePolicy(sizePolicy)
        self.Note9_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_9.setText("")
        self.Note9_9.setCheckable(True)
        self.Note9_9.setObjectName("Note9_9")
        self.Sheet.addWidget(self.Note9_9, 5, 8, 1, 1)
        self.Note10_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_2.sizePolicy().hasHeightForWidth())
        self.Note10_2.setSizePolicy(sizePolicy)
        self.Note10_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_2.setText("")
        self.Note10_2.setCheckable(True)
        self.Note10_2.setObjectName("Note10_2")
        self.Sheet.addWidget(self.Note10_2, 12, 9, 1, 1)
        self.Note9_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_3.sizePolicy().hasHeightForWidth())
        self.Note9_3.setSizePolicy(sizePolicy)
        self.Note9_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_3.setText("")
        self.Note9_3.setCheckable(True)
        self.Note9_3.setObjectName("Note9_3")
        self.Sheet.addWidget(self.Note9_3, 11, 8, 1, 1)
        self.Note9_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_8.sizePolicy().hasHeightForWidth())
        self.Note9_8.setSizePolicy(sizePolicy)
        self.Note9_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_8.setText("")
        self.Note9_8.setCheckable(True)
        self.Note9_8.setObjectName("Note9_8")
        self.Sheet.addWidget(self.Note9_8, 6, 8, 1, 1)
        self.Note9_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_12.sizePolicy().hasHeightForWidth())
        self.Note9_12.setSizePolicy(sizePolicy)
        self.Note9_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_12.setText("")
        self.Note9_12.setCheckable(True)
        self.Note9_12.setObjectName("Note9_12")
        self.Sheet.addWidget(self.Note9_12, 2, 8, 1, 1)
        self.Note9_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_6.sizePolicy().hasHeightForWidth())
        self.Note9_6.setSizePolicy(sizePolicy)
        self.Note9_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_6.setText("")
        self.Note9_6.setCheckable(True)
        self.Note9_6.setObjectName("Note9_6")
        self.Sheet.addWidget(self.Note9_6, 8, 8, 1, 1)
        self.Note16_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_12.sizePolicy().hasHeightForWidth())
        self.Note16_12.setSizePolicy(sizePolicy)
        self.Note16_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_12.setText("")
        self.Note16_12.setCheckable(True)
        self.Note16_12.setObjectName("Note16_12")
        self.Sheet.addWidget(self.Note16_12, 2, 15, 1, 1)
        self.Note5_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_3.sizePolicy().hasHeightForWidth())
        self.Note5_3.setSizePolicy(sizePolicy)
        self.Note5_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_3.setText("")
        self.Note5_3.setCheckable(True)
        self.Note5_3.setObjectName("Note5_3")
        self.Sheet.addWidget(self.Note5_3, 11, 4, 1, 1)
        self.Note16_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_1.sizePolicy().hasHeightForWidth())
        self.Note16_1.setSizePolicy(sizePolicy)
        self.Note16_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_1.setText("")
        self.Note16_1.setCheckable(True)
        self.Note16_1.setObjectName("Note16_1")
        self.Sheet.addWidget(self.Note16_1, 13, 15, 1, 1)
        self.Note17_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_13.sizePolicy().hasHeightForWidth())
        self.Note17_13.setSizePolicy(sizePolicy)
        self.Note17_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_13.setText("")
        self.Note17_13.setCheckable(True)
        self.Note17_13.setObjectName("Note17_13")
        self.Sheet.addWidget(self.Note17_13, 1, 16, 1, 1)
        self.Note6_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_5.sizePolicy().hasHeightForWidth())
        self.Note6_5.setSizePolicy(sizePolicy)
        self.Note6_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_5.setText("")
        self.Note6_5.setCheckable(True)
        self.Note6_5.setObjectName("Note6_5")
        self.Sheet.addWidget(self.Note6_5, 9, 5, 1, 1)
        self.Note17_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_1.sizePolicy().hasHeightForWidth())
        self.Note17_1.setSizePolicy(sizePolicy)
        self.Note17_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_1.setText("")
        self.Note17_1.setCheckable(True)
        self.Note17_1.setObjectName("Note17_1")
        self.Sheet.addWidget(self.Note17_1, 13, 16, 1, 1)
        self.Note17_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_12.sizePolicy().hasHeightForWidth())
        self.Note17_12.setSizePolicy(sizePolicy)
        self.Note17_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_12.setText("")
        self.Note17_12.setCheckable(True)
        self.Note17_12.setObjectName("Note17_12")
        self.Sheet.addWidget(self.Note17_12, 2, 16, 1, 1)
        self.Note16_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_13.sizePolicy().hasHeightForWidth())
        self.Note16_13.setSizePolicy(sizePolicy)
        self.Note16_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_13.setText("")
        self.Note16_13.setCheckable(True)
        self.Note16_13.setObjectName("Note16_13")
        self.Sheet.addWidget(self.Note16_13, 1, 15, 1, 1)
        self.Note4_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_9.sizePolicy().hasHeightForWidth())
        self.Note4_9.setSizePolicy(sizePolicy)
        self.Note4_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_9.setText("")
        self.Note4_9.setCheckable(True)
        self.Note4_9.setObjectName("Note4_9")
        self.Sheet.addWidget(self.Note4_9, 5, 3, 1, 1)
        self.Note4_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_10.sizePolicy().hasHeightForWidth())
        self.Note4_10.setSizePolicy(sizePolicy)
        self.Note4_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_10.setText("")
        self.Note4_10.setCheckable(True)
        self.Note4_10.setObjectName("Note4_10")
        self.Sheet.addWidget(self.Note4_10, 4, 3, 1, 1)
        self.Note5_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_7.sizePolicy().hasHeightForWidth())
        self.Note5_7.setSizePolicy(sizePolicy)
        self.Note5_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_7.setText("")
        self.Note5_7.setCheckable(True)
        self.Note5_7.setObjectName("Note5_7")
        self.Sheet.addWidget(self.Note5_7, 7, 4, 1, 1)
        self.Note6_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_9.sizePolicy().hasHeightForWidth())
        self.Note6_9.setSizePolicy(sizePolicy)
        self.Note6_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_9.setText("")
        self.Note6_9.setCheckable(True)
        self.Note6_9.setObjectName("Note6_9")
        self.Sheet.addWidget(self.Note6_9, 5, 5, 1, 1)
        self.Note5_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_11.sizePolicy().hasHeightForWidth())
        self.Note5_11.setSizePolicy(sizePolicy)
        self.Note5_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_11.setText("")
        self.Note5_11.setCheckable(True)
        self.Note5_11.setObjectName("Note5_11")
        self.Sheet.addWidget(self.Note5_11, 3, 4, 1, 1)
        self.Note4_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_11.sizePolicy().hasHeightForWidth())
        self.Note4_11.setSizePolicy(sizePolicy)
        self.Note4_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_11.setText("")
        self.Note4_11.setCheckable(True)
        self.Note4_11.setObjectName("Note4_11")
        self.Sheet.addWidget(self.Note4_11, 3, 3, 1, 1)
        self.Note13_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_9.sizePolicy().hasHeightForWidth())
        self.Note13_9.setSizePolicy(sizePolicy)
        self.Note13_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_9.setText("")
        self.Note13_9.setCheckable(True)
        self.Note13_9.setObjectName("Note13_9")
        self.Sheet.addWidget(self.Note13_9, 5, 12, 1, 1)
        self.Note5_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_10.sizePolicy().hasHeightForWidth())
        self.Note5_10.setSizePolicy(sizePolicy)
        self.Note5_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_10.setText("")
        self.Note5_10.setCheckable(True)
        self.Note5_10.setObjectName("Note5_10")
        self.Sheet.addWidget(self.Note5_10, 4, 4, 1, 1)
        self.Note8_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_5.sizePolicy().hasHeightForWidth())
        self.Note8_5.setSizePolicy(sizePolicy)
        self.Note8_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_5.setText("")
        self.Note8_5.setCheckable(True)
        self.Note8_5.setObjectName("Note8_5")
        self.Sheet.addWidget(self.Note8_5, 9, 7, 1, 1)
        self.Note13_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_4.sizePolicy().hasHeightForWidth())
        self.Note13_4.setSizePolicy(sizePolicy)
        self.Note13_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_4.setText("")
        self.Note13_4.setCheckable(True)
        self.Note13_4.setObjectName("Note13_4")
        self.Sheet.addWidget(self.Note13_4, 10, 12, 1, 1)
        self.Note5_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_2.sizePolicy().hasHeightForWidth())
        self.Note5_2.setSizePolicy(sizePolicy)
        self.Note5_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_2.setText("")
        self.Note5_2.setCheckable(True)
        self.Note5_2.setObjectName("Note5_2")
        self.Sheet.addWidget(self.Note5_2, 12, 4, 1, 1)
        self.Note13_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_1.sizePolicy().hasHeightForWidth())
        self.Note13_1.setSizePolicy(sizePolicy)
        self.Note13_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_1.setText("")
        self.Note13_1.setCheckable(True)
        self.Note13_1.setObjectName("Note13_1")
        self.Sheet.addWidget(self.Note13_1, 13, 12, 1, 1)
        self.Note12_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_11.sizePolicy().hasHeightForWidth())
        self.Note12_11.setSizePolicy(sizePolicy)
        self.Note12_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_11.setText("")
        self.Note12_11.setCheckable(True)
        self.Note12_11.setObjectName("Note12_11")
        self.Sheet.addWidget(self.Note12_11, 3, 11, 1, 1)
        self.Note9_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note9_1.sizePolicy().hasHeightForWidth())
        self.Note9_1.setSizePolicy(sizePolicy)
        self.Note9_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note9_1.setText("")
        self.Note9_1.setCheckable(True)
        self.Note9_1.setObjectName("Note9_1")
        self.Sheet.addWidget(self.Note9_1, 13, 8, 1, 1)
        self.Note12_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note12_1.sizePolicy().hasHeightForWidth())
        self.Note12_1.setSizePolicy(sizePolicy)
        self.Note12_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note12_1.setText("")
        self.Note12_1.setCheckable(True)
        self.Note12_1.setObjectName("Note12_1")
        self.Sheet.addWidget(self.Note12_1, 13, 11, 1, 1)
        self.Note13_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_13.sizePolicy().hasHeightForWidth())
        self.Note13_13.setSizePolicy(sizePolicy)
        self.Note13_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_13.setText("")
        self.Note13_13.setCheckable(True)
        self.Note13_13.setObjectName("Note13_13")
        self.Sheet.addWidget(self.Note13_13, 1, 12, 1, 1)
        self.Note11_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note11_1.sizePolicy().hasHeightForWidth())
        self.Note11_1.setSizePolicy(sizePolicy)
        self.Note11_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note11_1.setText("")
        self.Note11_1.setCheckable(True)
        self.Note11_1.setObjectName("Note11_1")
        self.Sheet.addWidget(self.Note11_1, 13, 10, 1, 1)
        self.Note13_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_7.sizePolicy().hasHeightForWidth())
        self.Note13_7.setSizePolicy(sizePolicy)
        self.Note13_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_7.setText("")
        self.Note13_7.setCheckable(True)
        self.Note13_7.setObjectName("Note13_7")
        self.Sheet.addWidget(self.Note13_7, 7, 12, 1, 1)
        self.Note8_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_1.sizePolicy().hasHeightForWidth())
        self.Note8_1.setSizePolicy(sizePolicy)
        self.Note8_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_1.setText("")
        self.Note8_1.setCheckable(True)
        self.Note8_1.setObjectName("Note8_1")
        self.Sheet.addWidget(self.Note8_1, 13, 7, 1, 1)
        self.Note6_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_11.sizePolicy().hasHeightForWidth())
        self.Note6_11.setSizePolicy(sizePolicy)
        self.Note6_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_11.setText("")
        self.Note6_11.setCheckable(True)
        self.Note6_11.setObjectName("Note6_11")
        self.Sheet.addWidget(self.Note6_11, 3, 5, 1, 1)
        self.Note13_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_2.sizePolicy().hasHeightForWidth())
        self.Note13_2.setSizePolicy(sizePolicy)
        self.Note13_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_2.setText("")
        self.Note13_2.setCheckable(True)
        self.Note13_2.setObjectName("Note13_2")
        self.Sheet.addWidget(self.Note13_2, 12, 12, 1, 1)
        self.Note10_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note10_1.sizePolicy().hasHeightForWidth())
        self.Note10_1.setSizePolicy(sizePolicy)
        self.Note10_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note10_1.setText("")
        self.Note10_1.setCheckable(True)
        self.Note10_1.setObjectName("Note10_1")
        self.Sheet.addWidget(self.Note10_1, 13, 9, 1, 1)
        self.Note8_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note8_7.sizePolicy().hasHeightForWidth())
        self.Note8_7.setSizePolicy(sizePolicy)
        self.Note8_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note8_7.setText("")
        self.Note8_7.setCheckable(True)
        self.Note8_7.setObjectName("Note8_7")
        self.Sheet.addWidget(self.Note8_7, 7, 7, 1, 1)
        self.Note6_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_8.sizePolicy().hasHeightForWidth())
        self.Note6_8.setSizePolicy(sizePolicy)
        self.Note6_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_8.setText("")
        self.Note6_8.setCheckable(True)
        self.Note6_8.setObjectName("Note6_8")
        self.Sheet.addWidget(self.Note6_8, 6, 5, 1, 1)
        self.Note5_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_8.sizePolicy().hasHeightForWidth())
        self.Note5_8.setSizePolicy(sizePolicy)
        self.Note5_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_8.setText("")
        self.Note5_8.setCheckable(True)
        self.Note5_8.setObjectName("Note5_8")
        self.Sheet.addWidget(self.Note5_8, 6, 4, 1, 1)
        self.Note6_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_4.sizePolicy().hasHeightForWidth())
        self.Note6_4.setSizePolicy(sizePolicy)
        self.Note6_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_4.setText("")
        self.Note6_4.setCheckable(True)
        self.Note6_4.setObjectName("Note6_4")
        self.Sheet.addWidget(self.Note6_4, 10, 5, 1, 1)
        self.Note15_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_1.sizePolicy().hasHeightForWidth())
        self.Note15_1.setSizePolicy(sizePolicy)
        self.Note15_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_1.setText("")
        self.Note15_1.setCheckable(True)
        self.Note15_1.setObjectName("Note15_1")
        self.Sheet.addWidget(self.Note15_1, 13, 14, 1, 1)
        self.Note14_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_1.sizePolicy().hasHeightForWidth())
        self.Note14_1.setSizePolicy(sizePolicy)
        self.Note14_1.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_1.setText("")
        self.Note14_1.setCheckable(True)
        self.Note14_1.setObjectName("Note14_1")
        self.Sheet.addWidget(self.Note14_1, 13, 13, 1, 1)
        self.Note5_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note5_4.sizePolicy().hasHeightForWidth())
        self.Note5_4.setSizePolicy(sizePolicy)
        self.Note5_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note5_4.setText("")
        self.Note5_4.setCheckable(True)
        self.Note5_4.setObjectName("Note5_4")
        self.Sheet.addWidget(self.Note5_4, 10, 4, 1, 1)
        self.Measure_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Measure_2.sizePolicy().hasHeightForWidth())
        self.Measure_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Measure_2.setFont(font)
        self.Measure_2.setObjectName("Measure_2")
        self.Sheet.addWidget(self.Measure_2, 0, 4, 1, 1)
        self.Measure_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Measure_1.sizePolicy().hasHeightForWidth())
        self.Measure_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Measure_1.setFont(font)
        self.Measure_1.setObjectName("Measure_1")
        self.Sheet.addWidget(self.Measure_1, 0, 0, 1, 1)
        self.Note14_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_6.sizePolicy().hasHeightForWidth())
        self.Note14_6.setSizePolicy(sizePolicy)
        self.Note14_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_6.setText("")
        self.Note14_6.setCheckable(True)
        self.Note14_6.setObjectName("Note14_6")
        self.Sheet.addWidget(self.Note14_6, 8, 13, 1, 1)
        self.Note14_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_4.sizePolicy().hasHeightForWidth())
        self.Note14_4.setSizePolicy(sizePolicy)
        self.Note14_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_4.setText("")
        self.Note14_4.setCheckable(True)
        self.Note14_4.setObjectName("Note14_4")
        self.Sheet.addWidget(self.Note14_4, 10, 13, 1, 1)
        self.Note15_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_4.sizePolicy().hasHeightForWidth())
        self.Note15_4.setSizePolicy(sizePolicy)
        self.Note15_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_4.setText("")
        self.Note15_4.setCheckable(True)
        self.Note15_4.setObjectName("Note15_4")
        self.Sheet.addWidget(self.Note15_4, 10, 14, 1, 1)
        self.Note15_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_3.sizePolicy().hasHeightForWidth())
        self.Note15_3.setSizePolicy(sizePolicy)
        self.Note15_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_3.setText("")
        self.Note15_3.setCheckable(True)
        self.Note15_3.setObjectName("Note15_3")
        self.Sheet.addWidget(self.Note15_3, 11, 14, 1, 1)
        self.Note14_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_5.sizePolicy().hasHeightForWidth())
        self.Note14_5.setSizePolicy(sizePolicy)
        self.Note14_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_5.setText("")
        self.Note14_5.setCheckable(True)
        self.Note14_5.setObjectName("Note14_5")
        self.Sheet.addWidget(self.Note14_5, 9, 13, 1, 1)
        self.Note14_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_3.sizePolicy().hasHeightForWidth())
        self.Note14_3.setSizePolicy(sizePolicy)
        self.Note14_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_3.setText("")
        self.Note14_3.setCheckable(True)
        self.Note14_3.setObjectName("Note14_3")
        self.Sheet.addWidget(self.Note14_3, 11, 13, 1, 1)
        self.Note15_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_5.sizePolicy().hasHeightForWidth())
        self.Note15_5.setSizePolicy(sizePolicy)
        self.Note15_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_5.setText("")
        self.Note15_5.setCheckable(True)
        self.Note15_5.setObjectName("Note15_5")
        self.Sheet.addWidget(self.Note15_5, 9, 14, 1, 1)
        self.Note16_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_11.sizePolicy().hasHeightForWidth())
        self.Note16_11.setSizePolicy(sizePolicy)
        self.Note16_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_11.setText("")
        self.Note16_11.setCheckable(True)
        self.Note16_11.setObjectName("Note16_11")
        self.Sheet.addWidget(self.Note16_11, 3, 15, 1, 1)
        self.Note17_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_11.sizePolicy().hasHeightForWidth())
        self.Note17_11.setSizePolicy(sizePolicy)
        self.Note17_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_11.setText("")
        self.Note17_11.setCheckable(True)
        self.Note17_11.setObjectName("Note17_11")
        self.Sheet.addWidget(self.Note17_11, 3, 16, 1, 1)
        self.Note15_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_6.sizePolicy().hasHeightForWidth())
        self.Note15_6.setSizePolicy(sizePolicy)
        self.Note15_6.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_6.setText("")
        self.Note15_6.setCheckable(True)
        self.Note15_6.setObjectName("Note15_6")
        self.Sheet.addWidget(self.Note15_6, 8, 14, 1, 1)
        self.Note14_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_11.sizePolicy().hasHeightForWidth())
        self.Note14_11.setSizePolicy(sizePolicy)
        self.Note14_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_11.setText("")
        self.Note14_11.setCheckable(True)
        self.Note14_11.setObjectName("Note14_11")
        self.Sheet.addWidget(self.Note14_11, 3, 13, 1, 1)
        self.Note14_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_10.sizePolicy().hasHeightForWidth())
        self.Note14_10.setSizePolicy(sizePolicy)
        self.Note14_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_10.setText("")
        self.Note14_10.setCheckable(True)
        self.Note14_10.setObjectName("Note14_10")
        self.Sheet.addWidget(self.Note14_10, 4, 13, 1, 1)
        self.Note14_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_7.sizePolicy().hasHeightForWidth())
        self.Note14_7.setSizePolicy(sizePolicy)
        self.Note14_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_7.setText("")
        self.Note14_7.setCheckable(True)
        self.Note14_7.setObjectName("Note14_7")
        self.Sheet.addWidget(self.Note14_7, 7, 13, 1, 1)
        self.Note15_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_9.sizePolicy().hasHeightForWidth())
        self.Note15_9.setSizePolicy(sizePolicy)
        self.Note15_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_9.setText("")
        self.Note15_9.setCheckable(True)
        self.Note15_9.setObjectName("Note15_9")
        self.Sheet.addWidget(self.Note15_9, 5, 14, 1, 1)
        self.Note17_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_3.sizePolicy().hasHeightForWidth())
        self.Note17_3.setSizePolicy(sizePolicy)
        self.Note17_3.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_3.setText("")
        self.Note17_3.setCheckable(True)
        self.Note17_3.setObjectName("Note17_3")
        self.Sheet.addWidget(self.Note17_3, 11, 16, 1, 1)
        self.Note15_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_8.sizePolicy().hasHeightForWidth())
        self.Note15_8.setSizePolicy(sizePolicy)
        self.Note15_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_8.setText("")
        self.Note15_8.setCheckable(True)
        self.Note15_8.setObjectName("Note15_8")
        self.Sheet.addWidget(self.Note15_8, 6, 14, 1, 1)
        self.Note15_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_10.sizePolicy().hasHeightForWidth())
        self.Note15_10.setSizePolicy(sizePolicy)
        self.Note15_10.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_10.setText("")
        self.Note15_10.setCheckable(True)
        self.Note15_10.setObjectName("Note15_10")
        self.Sheet.addWidget(self.Note15_10, 4, 14, 1, 1)
        self.Note16_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note16_4.sizePolicy().hasHeightForWidth())
        self.Note16_4.setSizePolicy(sizePolicy)
        self.Note16_4.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note16_4.setText("")
        self.Note16_4.setCheckable(True)
        self.Note16_4.setObjectName("Note16_4")
        self.Sheet.addWidget(self.Note16_4, 10, 15, 1, 1)
        self.Note14_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_9.sizePolicy().hasHeightForWidth())
        self.Note14_9.setSizePolicy(sizePolicy)
        self.Note14_9.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_9.setText("")
        self.Note14_9.setCheckable(True)
        self.Note14_9.setObjectName("Note14_9")
        self.Sheet.addWidget(self.Note14_9, 5, 13, 1, 1)
        self.Note14_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_8.sizePolicy().hasHeightForWidth())
        self.Note14_8.setSizePolicy(sizePolicy)
        self.Note14_8.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_8.setText("")
        self.Note14_8.setCheckable(True)
        self.Note14_8.setObjectName("Note14_8")
        self.Sheet.addWidget(self.Note14_8, 6, 13, 1, 1)
        self.Note15_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note15_7.sizePolicy().hasHeightForWidth())
        self.Note15_7.setSizePolicy(sizePolicy)
        self.Note15_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note15_7.setText("")
        self.Note15_7.setCheckable(True)
        self.Note15_7.setObjectName("Note15_7")
        self.Sheet.addWidget(self.Note15_7, 7, 14, 1, 1)
        self.Note17_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note17_5.sizePolicy().hasHeightForWidth())
        self.Note17_5.setSizePolicy(sizePolicy)
        self.Note17_5.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note17_5.setText("")
        self.Note17_5.setCheckable(True)
        self.Note17_5.setObjectName("Note17_5")
        self.Sheet.addWidget(self.Note17_5, 9, 16, 1, 1)
        self.Note14_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note14_2.sizePolicy().hasHeightForWidth())
        self.Note14_2.setSizePolicy(sizePolicy)
        self.Note14_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note14_2.setText("")
        self.Note14_2.setCheckable(True)
        self.Note14_2.setObjectName("Note14_2")
        self.Sheet.addWidget(self.Note14_2, 12, 13, 1, 1)
        self.Note6_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_7.sizePolicy().hasHeightForWidth())
        self.Note6_7.setSizePolicy(sizePolicy)
        self.Note6_7.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_7.setText("")
        self.Note6_7.setCheckable(True)
        self.Note6_7.setObjectName("Note6_7")
        self.Sheet.addWidget(self.Note6_7, 7, 5, 1, 1)
        self.Note6_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note6_2.sizePolicy().hasHeightForWidth())
        self.Note6_2.setSizePolicy(sizePolicy)
        self.Note6_2.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note6_2.setText("")
        self.Note6_2.setCheckable(True)
        self.Note6_2.setObjectName("Note6_2")
        self.Sheet.addWidget(self.Note6_2, 12, 5, 1, 1)
        self.Note4_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_13.sizePolicy().hasHeightForWidth())
        self.Note4_13.setSizePolicy(sizePolicy)
        self.Note4_13.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_13.setText("")
        self.Note4_13.setCheckable(True)
        self.Note4_13.setObjectName("Note4_13")
        self.Sheet.addWidget(self.Note4_13, 1, 3, 1, 1)
        self.Note13_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note13_11.sizePolicy().hasHeightForWidth())
        self.Note13_11.setSizePolicy(sizePolicy)
        self.Note13_11.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note13_11.setText("")
        self.Note13_11.setCheckable(True)
        self.Note13_11.setObjectName("Note13_11")
        self.Sheet.addWidget(self.Note13_11, 3, 12, 1, 1)
        self.Note4_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Note4_12.sizePolicy().hasHeightForWidth())
        self.Note4_12.setSizePolicy(sizePolicy)
        self.Note4_12.setStyleSheet(
            "QPushButton:!hover:!checked { border-image: url(:/sheet/src/sheet/noCheck.png); }\n"
            "QPushButton:!hover:checked { border-image: url(:/sheet/src/sheet/checked.png) }\n"
            "QPushButton:!checked:pressed, QPushButton:hover:checked:!pressed { border-image: url(:/sheet/src/sheet/checked_hover.png) }\n"
            "QPushButton:checked:pressed, QPushButton:hover:!checked:!pressed { border-image: url(:/sheet/src/sheet/noCheck_hover.png); }"
        )
        self.Note4_12.setText("")
        self.Note4_12.setCheckable(True)
        self.Note4_12.setObjectName("Note4_12")
        self.Sheet.addWidget(self.Note4_12, 2, 3, 1, 1)
        self.Measure_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Measure_5.sizePolicy().hasHeightForWidth())
        self.Measure_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Measure_5.setFont(font)
        self.Measure_5.setObjectName("Measure_5")
        self.Sheet.addWidget(self.Measure_5, 0, 16, 1, 1)
        self.Measure_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Measure_3.sizePolicy().hasHeightForWidth())
        self.Measure_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Measure_3.setFont(font)
        self.Measure_3.setObjectName("Measure_3")
        self.Sheet.addWidget(self.Measure_3, 0, 8, 1, 1)
        self.Measure_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Measure_4.sizePolicy().hasHeightForWidth())
        self.Measure_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Measure_4.setFont(font)
        self.Measure_4.setObjectName("Measure_4")
        self.Sheet.addWidget(self.Measure_4, 0, 12, 1, 1)
        self.SheetSection.addLayout(self.Sheet)
        self.Velocity = QtWidgets.QGridLayout()
        self.Velocity.setSpacing(0)
        self.Velocity.setObjectName("Velocity")
        self.VelocityLabel = QtWidgets.QLabel(self.centralwidget)
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
        self.VelocitySlider = QtWidgets.QSlider(self.centralwidget)
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
        self.verticalLayout_2.addLayout(self.SheetSection)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuOthers = QtWidgets.QMenu(self.menubar)
        self.menuOthers.setObjectName("menuOthers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionSystem = QtWidgets.QAction(MainWindow)
        self.actionSystem.setObjectName("actionSystem")
        self.actionTheme = QtWidgets.QAction(MainWindow)
        self.actionTheme.setObjectName("actionTheme")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuSettings.addAction(self.actionSystem)
        self.menuSettings.addAction(self.actionTheme)
        self.menuOthers.addAction(self.actionAbout)
        self.menuOthers.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuOthers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NaiveMusic"))
        self.Measure_2.setText(_translate("MainWindow", "2"))
        self.Measure_1.setText(_translate("MainWindow", "1"))
        self.Measure_5.setText(_translate("MainWindow", "5"))
        self.Measure_3.setText(_translate("MainWindow", "3"))
        self.Measure_4.setText(_translate("MainWindow", "4"))
        self.VelocityLabel.setText(_translate("MainWindow", "Velocity"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuOthers.setTitle(_translate("MainWindow", "Others"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionSystem.setText(_translate("MainWindow", "System"))
        self.actionTheme.setText(_translate("MainWindow", "Theme"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


import pictures_rc
