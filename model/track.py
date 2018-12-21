from io import BytesIO

from .note import Note
from .const import *
from lib.mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class Track():
    def __init__(self, inst, vel):
        self.notes = {}
        self.curID = 0
        self.inst = inst
        self.vel = vel
        self.demoNotes = ''

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

    def search(self, on, off, keys=KEY_RANGE):
        """ Search for all notes satisfying that
            1) note.key is in keys;
            2) the interval [note.on, note.off) has non-empty intersection with [on,off).
            Return a list of noteID

        Args:
            keys (<list>int): the range of 'key' property. Defaults to all keys.
            on (int): the start time of the interval.
            off(int): the end time of the interval.

        P.S. we don't search on 'vel' property because it is not characteristic.
        """
        resultList = []
        for noteID, note in self.notes:
            if (note.key in keys and self.__intersect(on, off, note.on, note.off)):
                resultList.append(noteID)
        return resultList

    def __intersect(self, on1, off1, on2, off2):
        """ Return boolen value for the condition
            whether interval [on1,off1) intersects with [on2,off2)
        """
        if max(on1, off1) <= on2:
            return False
        if min(on1, off1) >= off2:
            return False
        return True

    def toMidi(self, bpm, channel=0, save=True):
        track = MidiTrack()
        pitch = [58, 60, 62, 64, 65, 67, 69, 71, 72]

        track.append(Message('program_change', channel=channel, program=self.inst, time=0))
        track.append(Message('control_change', channel=channel, control=7, value=self.vel, time=0))
        track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
        for note in self.demoNotes:
            if note == ' ':
                track.append(Message('note_on', channel=channel, note=64, velocity=0, time=0))
                track.append(Message('note_off', channel=channel, note=64, velocity=0, time=192))
            elif int(note) > 0 and int(note) < 9:
                note = int(note)
                track.append(Message('note_on', channel=channel, note=pitch[note], velocity=100, time=0))
                track.append(Message('note_off', channel=channel, note=pitch[note], velocity=100, time=192))
        if save:
            self.buf = BytesIO()
            mid = MidiFile()
            mid.tracks.append(track)
            mid.save(file=self.buf)
            return mid.length
        return track
