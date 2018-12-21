import sys
import pickle
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
        self._curFile = File(bpm=120)
        self._curView = None

    # View part
    def setCurView(self, view):
        self._curView = view

    # Track part
    def getTrack(self, trackID):
        if trackID not in self._curFile.tracks:
            raise ValueError('Track ID {} not found when get'.format(trackID))
        return self._curFile.tracks[trackID]

    def getTrackNum(self):
        return len(self._curFile.tracks)

    def getTrackInst(self, trackID):
        return self.getTrack(trackID).inst

    def getTrackVel(self, trackID):
        return self.getTrack(trackID).vel

    def setCurTrack(self, trackID):
        self._curTrackID = trackID
        self._curTrack = self.getTrack(trackID)
        self._curPos = 0
        self._curView.update()

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
        self._curView.update()

    # File part
    def setBPM(self, bpm):
        if not isinstance(bpm, int) or bpm < 0 or bpm > 200:
            raise ValueError('bmp must be int within 0~200, not {}'.format(bpm))
        self._curFile.bpm = bpm

    def getBPM(self):
        return self._curFile.bpm

    def saveFile(self):
        # TODO: use serialization
        return

    # Play part
    def playAll(self):
        if self.changed:
            self.length = self._curFile.toMidi()
            self.changed = False
            self._play(self._curFile.buf, self.length, True)
        else:
            self._play(self._curFile.buf, self.length, False)


    def stopAll(self):
        self._stop()

    def playTrack(self, trackID):
        length = self.getTrack(trackID).toMidi(self.getBPM())
        self._play(self._curFile.buf, length)
