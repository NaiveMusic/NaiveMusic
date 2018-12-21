# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from NMusicWindow import NMusicWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = NMusicWindow()
    myWin.initUI()
    sys.exit(app.exec_())
