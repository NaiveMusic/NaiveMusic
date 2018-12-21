# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from NMusicSheet import NMusicSheet

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = NMusicSheet()
    myWin.initUI()
    sys.exit(app.exec_())
