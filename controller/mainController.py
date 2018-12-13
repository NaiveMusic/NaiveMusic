import sys
import pickle
from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
from controller.audioController import AudioController
from controller.trackController import TrackController


class MainController(TrackController, AudioController):
    def __init__(self):
        TrackController.__init__(self)
        AudioController.__init__(self)
        self.curFile = File(bpm=120)

    def setCurTrack(self, trackID):
        self._curTrackID = trackID
        self._curTrack = self.curFile.getTrack(trackID)

    def playAll(self):
        self.curFile.toDemoMidi()
        self._play()

    def playTrack(self, trackID):
        self.curFile.getTrack(trackID).toDemoMidi(self.curFile.getBPM())
        self._play()
