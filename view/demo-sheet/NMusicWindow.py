# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget, QPushButton
from Ui_mainWindow import Ui_MainWindow


class NMusicWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(NMusicWindow, self).__init__(parent)
        self.setupUi(self)
        self.initPianoRoll()
        self.initSheet()

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
                note = self.Sheet.itemAtPosition(row, column).widget()
                if isinstance(note, QPushButton):
                    note.clicked.connect(self.note_clicked)

    # Sheet点击事件
    def note_clicked(self):
        sender = self.sender()

        # Change below
        print(sender.objectName())
        # Change above
