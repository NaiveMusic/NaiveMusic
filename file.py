from track import Track
from const import *


class File():
    def __init__(self):
        self.__tracks = {}
        self.__curID = 0

    def getTrack(self, trackID):
        if trackID not in self.__tracks:
            raise ValueError('Track not found')
        return self.__tracks[trackID]

    def addTrack(self, inst=0, vel=100):
        self.__tracks[self.__curID] = Track(inst, vel)
        self.__curID += 1

    def delTrack(self, trackID):
        if trackID not in self.__tracks:
            raise ValueError('Track not found')
        poped = self.__tracks.pop(trackID)
        del poped

    def toEvents(self):
        # TODO
        return

    def saveFile(self):
        # TODO: use serialization
        return
