import sys
import pickle
from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
from controller.audioController import AudioController


class MainController():
    def __init__(self):
        self.curFile = File(bpm=120)
        self.__curTrackID = None
        self.__curTrack = None
        self.ac = AudioController()

    def setCurTrack(self, trackID):
        self.__curTrackID = trackID
        self.__curTrack = self.curFile.getTrack(trackID)

    @property
    def curTrackID(self):
        return self.__curTrackID

    @property
    def curTrack(self):
        return self.__curTrack

    def playAll(self):
        self.curFile.toDemoMidi()
        self.ac.play()

    def playTrack(self, trackID):
        self.curFile.getTrack(trackID).toDemoMidi(self.curFile.getBPM())
        self.ac.play()
