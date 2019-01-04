import sys
import pickle
import wave
from io import BytesIO

from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
from controller.audioController import AudioController
from controller.sheetController import SheetController
from lib.mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class MainController(SheetController, AudioController):
    def __init__(self):
        SheetController.__init__(self)
        AudioController.__init__(self)
        self.newFile()
        self._selectedInst = None
        self._state = STATE.EDITING

    # Track part
    def getTrack(self, trackID):
        if trackID not in self._curFile.tracks:
            raise ValueError('Track ID {} not found when get'.format(trackID))
        return self._curFile.tracks[trackID]

    def getTrackIDList(self):
        return self._curFile.tracks.keys()

    def getTrackNum(self):
        return len(self._curFile.tracks)

    def getTrackInst(self, trackID):
        return self.getTrack(trackID).inst

    def getTrackVel(self, trackID):
        return self.getTrack(trackID).vel

    def setCurTrack(self, trackID):
        if trackID == None:
            self._curTrack = None
            self._curTrackID = None
        else:
            self.switchTrack(trackID, self.getTrack(trackID))
        self.notify()

    def setTrackInst(self, trackID, inst):
        if inst not in INSTRUMENT:
            raise ValueError('Instrument {} not found'.format(inst))
        self.getTrack(trackID).inst = inst

    def setTrackVel(self, trackID, vel):
        if not isinstance(vel, int) or vel not in VEL_RANGE:
            raise ValueError('Velocity must be int within 0~127, not {}'.format(vel))
        self.getTrack(trackID).vel = vel

    def addTrack(self, inst=0, vel=100):
        if self.getTrackNum() >= MAX_TRACK_NUM:
            raise OverflowError('Track numbers cannot exceed {}'.format(MAX_TRACK_NUM))
        return self._curFile.addTrack(inst, vel)

    def delTrack(self, trackID):
        if trackID not in self._curFile.tracks:
            raise ValueError('Track ID {} not found when del'.format(trackID))
        self._curFile.delTrack(trackID)
        if trackID == self._curTrackID:
            self.setCurTrack(None)
        self._state = STATE.DEFAULT
        self.notify()

    # File part
    def setBPM(self, bpm):
        if not isinstance(bpm, int) or bpm < 0 or bpm > 200:
            raise ValueError('bmp must be int within 0~200, not {}'.format(bpm))
        self._curFile.bpm = bpm

    def getBPM(self):
        return self._curFile.bpm

    def newFile(self):
        self._curFile = File(bpm=DEFAULT_BPM)

    def saveFile(self, fileName='temp.nm'):
        pickle.dump(self._curFile, fileName)
        return

    def loadFile(self, fileName='temp.nm'):
        try:
            self._curFile = pickle.load(fileName)
        except:
            print('filename not exists!')
        self.notify()
    
    def export(self,fileType,fileName):
        '''
        fileType should be str, current support 'wav' and 'mid'
        '''
        mid = self._curFile.toMidi()
        if fileType == 'mid':
            mid.save(fileName)
        elif fileType == 'wav':
            buf = BytesIO()
            mid.save(file=buf)
            self._getSample(buf, mid.length, export=True, filename=fileName)
        else:
            raise NotImplementedError
        
    
    # Selection part
    def getSelectedInst(self):
        return self._selectedInst

    def setSelectedInst(self, inst):
        self._selectedInst = inst

    # Play part
    def playAll(self):
        mid = self._curFile.toMidi()
        buf = BytesIO()
        mid.save(file=buf)
        self._play(buf, mid.length)

    def playSingle(self, key):
        self._playSingle(self._curTrack.inst, key)

    def pauseAll(self):
        self._pause()

    def playTrack(self, trackID):
        mid = self.getTrack(trackID).toMidi(self.getBPM())
        buf = BytesIO()
        mid.save(file=buf)
        self._play(buf, mid.length)

    # Demo play part
    # def playAllDemo(self):
    #     self.length = self._curFile.toDemoMidi()
    #     self._play(self._curFile.buf, self.length, True)

    # def playTrackDemo(self, trackID):
    #     length = self.getTrack(trackID).toDemoMidi(self.getBPM())
    #     self._play(self.getTrack(trackID).buf, length)