from .note import Note
from .const import *
from mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class Track():
    def __init__(self, inst, vel):
        self.notes = {}
        self.curID = 0
        self.inst = inst
        self.vel = vel
        self.demoNotes = ''

    def getInfo(self):
        '''Return track instrument and velocity'''
        return self.inst, self.vel

    def getNote(self, noteID):
        if noteID not in self.notes:
            raise ValueError('Note not found')
        return self.notes[noteID]

    def getNoteIDList(self):
        return self.notes.keys()

    def setNote(self, noteID, key=None, vel=None, on=None, off=None):
        if noteID not in self.notes:
            raise ValueError('Note not found')
        self.notes[noteID].setAll(key, vel, on, off)

    def addNote(self, key, vel, on, off):
        self.notes[self.curID] = Note(key, vel, on, off)
        self.curID += 1

    def delNote(self, noteID):
        if noteID not in self.notes:
            raise ValueError('Note not found')
        poped = self.notes.pop(noteID)
        del poped
