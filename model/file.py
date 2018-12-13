from .track import Track
from .const import *
from mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class File():
    def __init__(self, bpm):
        self.__tracks = {}
        self.__curID = 0
        self.__bpm = bpm

    def getLen(self):
        return len(self.__tracks)

    def getTrack(self, trackID):
        if trackID not in self.__tracks:
            raise ValueError('Track ID {} not found'.format(trackID))
        return self.__tracks[trackID]

    def addTrack(self, inst=0, vel=100):
        if len(self.__tracks) >= MAX_TRACK_NUM:
            raise OverflowError('Track numbers cannot exceed {}'.format(MAX_TRACK_NUM))
        self.__tracks[self.__curID] = Track(inst, vel)
        trackID = self.__curID
        self.__curID += 1
        return trackID

    def delTrack(self, trackID):
        if trackID not in self.__tracks:
            raise ValueError('Track ID {} not found'.format(trackID))
        poped = self.__tracks.pop(trackID)
        del poped

    def setBPM(self, bpm):
        if not isinstance(bpm, int) or bpm < 0 or bpm > 200:
            raise ValueError('bmp must be int within 0~200, not {}'.format(bpm))
        self.__bpm = bpm

    def getBPM(self):
        return self.__bpm

    def toEvents(self):
        # TODO
        return

    def saveFile(self):
        # TODO: use serialization
        return

    def toDemoMidi(self):
        mid = MidiFile()

        for i, track in enumerate(self.__tracks.values()):
            midiTrack = track.toDemoMidi(bpm=self.__bpm, channel=i, save=False)
            mid.tracks.append(midiTrack)
        mid.save('fluidsynth/tmp.mid')
