import sys
import pickle
from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
from controller.audioController import AudioController
from controller.sheetController import SheetController
from mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class MainController(SheetController, AudioController):
    def __init__(self):
        SheetController.__init__(self)
        AudioController.__init__(self)
        self._curFile = File(bpm=120)

    def setCurTrack(self, trackID):
        self._curTrackID = trackID
        self._curTrack = self.getTrack(trackID)

    def playAll(self):
        self.toDemoMidi()
        self._play()

    def playTrack(self, trackID):
        self.getTrack(trackID).toDemoMidi(self.getBPM())
        self._play()

    def getTrackNum(self):
        return len(self._curFile.tracks)

    def getTrack(self, trackID):
        if trackID not in self._curFile.tracks:
            raise ValueError('Track ID {} not found when get'.format(trackID))
        return self._curFile.tracks[trackID]

    def addTrack(self, inst=0, vel=100):
        if len(self._curFile.tracks) >= MAX_TRACK_NUM:
            raise OverflowError('Track numbers cannot exceed {}'.format(MAX_TRACK_NUM))
        self._curFile.tracks[self._curFile.curID] = Track(inst, vel)
        trackID = self._curFile.curID
        self._curFile.curID += 1
        return trackID

    def delTrack(self, trackID):
        if trackID not in self._curFile.tracks:
            raise ValueError('Track ID {} not found when del'.format(trackID))
        poped = self._curFile.tracks.pop(trackID)
        del poped

    def setBPM(self, bpm):
        if not isinstance(bpm, int) or bpm < 0 or bpm > 200:
            raise ValueError('bmp must be int within 0~200, not {}'.format(bpm))
        self._curFile.bpm = bpm

    def getBPM(self):
        return self._curFile.bpm

    def toEvents(self):
        # TODO
        return

    def saveFile(self):
        # TODO: use serialization
        return

    def toDemoMidi(self):
        mid = MidiFile()

        for i, track in enumerate(self._curFile.tracks.values()):
            midiTrack = track.toDemoMidi(bpm=self._curFile.bpm, channel=i, save=False)
            mid.tracks.append(midiTrack)
        mid.save('fluidsynth/tmp.mid')
