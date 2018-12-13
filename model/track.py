from .note import Note
from .const import *
from mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class Track():
    def __init__(self, inst, vel):
        self.__notes = {}
        self.__curID = 0
        self.setInst(inst)
        self.setVel(vel)
        self.demoNotes = ''

    def getInfo(self):
        '''Return track instrument and velocity'''
        return self.__inst, self.__vel

    def getNote(self, noteID):
        if noteID not in self.__notes:
            raise ValueError('Note not found')
        return self.__notes[noteID]

    def getNoteIDList(self):
        return self.__notes.keys()

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
            raise ValueError('Instrument {} not found'.format(inst))
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

    def toDemoMidi(self, bpm, channel=0, save=True):
        pass

        mid = MidiFile()

        track = MidiTrack()
        pitch = [58, 60, 62, 64, 65, 67, 69, 71, 72]

        mid.tracks.append(track)
        track.append(Message('program_change', channel=channel, program=self.__inst, time=0))
        track.append(Message('control_change', channel=channel, control=7, value=self.__vel, time=0))
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
            mid.save('fluidsynth/tmp.mid')
        return track