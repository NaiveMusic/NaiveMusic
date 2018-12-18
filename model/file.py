from model.track import Track
from mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage

class File():
    def __init__(self, bpm):
        self.tracks = {}
        self.curID = 0
        self.bpm = bpm

    def addTrack(self,inst,vel):
        self.tracks[self.curID] = Track(inst, vel)
        trackID = self.curID
        self.curID += 1
        return trackID

    def delTrack(self,trackID):
        poped = self.tracks.pop(trackID)
        del poped

    def toMidi(self):
        mid = MidiFile()
        for i, track in enumerate(self.tracks.values()):
            midiTrack = track.toMidi(bpm=self.bpm, channel=i, save=False)
            mid.tracks.append(midiTrack)
        mid.save('fluidsynth/tmp.mid')
