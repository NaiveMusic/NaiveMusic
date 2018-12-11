import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, uic
Ui_MainWindow, QtBaseClass = uic.loadUiType('./demo.ui')

sys.path.append('..')
from const import *

class Demo(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Demo')

        for inst in INSTRUMENT:
            self.instrument.addItem('{} {}'.format(inst, INSTRUMENT[inst]))
        self.instrument.currentIndexChanged.connect(self.ChangeInst)
        self.pitchButtons = QtWidgets.QButtonGroup()
        for i in range(8):
            cur = QtWidgets.QPushButton()
            cur.setText(str(i + 1))
            cur.setObjectName(str(i + 1))
            self.verticalLayout.addWidget(cur)
            self.pitchButtons.addButton(cur)
        self.pitchButtons.buttonClicked.connect(self.MousePlay)
        self.play.clicked.connect(self.MusicPlay)

        self.fs = subprocess.Popen([r'..\fluidsynth\fluidsynth.exe', '-n', r'..\fluidsynth\GeneralUser_GS.sf2'],
                                   stdin=subprocess.PIPE, bufsize=0)
        self.pitch = ['58', '60', '62', '64', '65', '67', '69', '71', '72']

    def send(self, cmd):
        self.fs.stdin.write(bytes(cmd + '\r\n', encoding='utf8'))

    def MusicPlay(self):
        music = self.music.toPlainText()
        tempo = self.tempo.value()
        for i in music:
            if i == ' ':
                self.send('sleep ' + str(tempo))
            elif int(i) > 0 and int(i) < 9:
                self.send('noteon 1 ' + self.pitch[int(i)] + ' 100')
                self.send('sleep ' + str(tempo))
                self.send('noteoff 1 ' + self.pitch[int(i)])

    def MousePlay(self, button):
        note = int(button.objectName())
        print(note)
        self.send('noteon 1 ' + self.pitch[note] + ' 100')

    def ChangeInst(self):
        inst = self.instrument.currentIndex()
        self.send('prog 1 ' + str(inst))

    def keyPressEvent(self, event):
        note = event.key() - 48
        if note > 0 and note < 9:
            print(note)
            self.send('noteon 1 ' + self.pitch[note] + ' 100')


app = QtWidgets.QApplication(sys.argv)
window = Demo()
window.show()
sys.exit(app.exec_())
