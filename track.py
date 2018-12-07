from note import Note
from const import *
import mido


class Track():
    def __init__(self, inst, vel):
        self.__notes = {}
        self.__curID = 0
        self.setInst(inst)
        self.setVel(vel)

    def getInfo(self):
        '''Return track instrument and velocity'''
        return self.__inst, self.__vel

    def getNote(self, noteID):
        if noteID not in self.__notes:
            raise ValueError('Note not found')
        return self.__notes[noteID]

    def setNote(self, noteID, key=None, vel=None, on=None, off=None):
        if noteID not in self.__notes:
            raise ValueError('Note not found')
        self.__notes[noteID].setAll(key, vel, on, off)

    def addNote(self, key, vel, on, off):
        self.__notes[self.__curID] = Note(key, vel, on, off)
        self.__curID += 1

    def delNote(self, noteID):
        if noteID not in self.__notes:
            raise ValueError('Note not found')
        poped = self.__notes.pop(noteID)
        del poped

    def setInst(self, inst):
        if inst not in INSTRUMENT:
            raise ValueError('Instrument not found')
        self.__inst = inst

    def setVel(self, vel):
        if not isinstance(vel, int) or vel < 0 or vel > 127:
            raise ValueError('Velocity must be int within 0~127')
        self.__vel = vel

    def toEvents(self):
        # TODO: sort notes based on note start time
        # translate them into midi noteon and noteoff events
        return  #list of events

    def toMidi(self):
        pass
        
