from io import BytesIO

from model.track import Track
from model.const import *
from lib.mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage, tempo2bpm


class File():
    def __init__(self, bpm=120):
        self.tracks = {}
        self.curID = 0
        self.bpm = bpm

    def addTrack(self, inst, vel):
        self.tracks[self.curID] = Track(inst, vel)
        trackID = self.curID
        self.curID += 1
        return trackID

    def delTrack(self, trackID):
        poped = self.tracks.pop(trackID)
        del poped

    def toMidi(self):
        """ Transform entire file into midi events 
        """
        mid = MidiFile()
        for i, track in enumerate(self.tracks.values()):
            midiTrack = track.toMidi(bpm=self.bpm, channel=i, save=False)
            mid.tracks.append(midiTrack)
        return mid

    def midiToFile(self, file='output.mid'):
        """ Transform .mid format into current file
        """
        mid = MidiFile(file)
        self.tracks.clear()
        self.curID = 0
        for i, track in enumerate(mid.tracks):
            trackID = self.addTrack(0, 100)
            curTrack = self.tracks[trackID]
            curTime = 0
            notOffYet = {}
            for msg in track:
                print(msg)
                if msg.type == 'note_on':
                    noteID = curTrack.addNote(key=msg.note, vel=msg.velocity, on=msg.time + curTime,
                                              off=msg.time + curTime + DELTA)
                    notOffYet[msg.note] = noteID
                elif msg.type == 'note_off':
                    noteID = notOffYet.pop(msg.note)
                    curTrack.setNote(noteID, off=curTime + msg.time)
                elif msg.type == 'program_change':
                    curTrack.inst = msg.program
                elif msg.type == 'control_change' and msg.control == 7:
                    curTrack.vel = msg.value
                elif msg.type == 'set_tempo':
                    self.bpm = tempo2bpm(msg.tempo)
                elif msg.type == 'end_of_track':
                    pass
                else:
                    print(f'Message {msg} not supported yet!')
                if not msg.is_meta:
                    curTime += msg.time
    #Demo part
    """
    def toDemoMidi(self):
        mid = MidiFile()
        for i, track in enumerate(self.tracks.values()):
            midiTrack = track.toDemoMidi(bpm=self.bpm, channel=i, save=False)
            mid.tracks.append(midiTrack)
        self.buf = BytesIO()
        mid.save(file=self.buf)
        return mid.length
    """
