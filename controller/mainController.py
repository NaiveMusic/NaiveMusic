import sys
import pickle
from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
from controller.audioController import AudioController
from controller.sheetController import SheetController
from mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class MainController(SheetController, AudioController):
    def __init__(self):
        SheetController.__init__(self)
        AudioController.__init__(self)
        self._curFile = File(bpm=120)
        self.curView = None

    # Track part
    def getTrack(self, trackID):
        if trackID not in self._curFile.tracks:
            raise ValueError('Track ID {} not found when get'.format(trackID))
        return self._curFile.tracks[trackID]

    def getTrackNum(self):
        return len(self._curFile.tracks)

    def getTrackInst(self, trackID):
        return self.getTrack(trackID).inst

    def getTrackVel(self, trackID):
        return self.getTrack(trackID).vel

    def setCurTrack(self, trackID):
        self._curTrackID = trackID
        self._curTrack = self.getTrack(trackID)
        self._curPos = 0
        self.curView.update()

    def setTrackInst(self, trackID, inst):
        if inst not in INSTRUMENT:
            raise ValueError('Instrument {} not found'.format(inst))
        self.getTrack(trackID).inst = inst

    def setTrackVel(self, trackID, vel):
        if not isinstance(vel, int) or vel not in VEL_RANGE:
            raise ValueError('Velocity must be int within 0~127, not {}'.format(vel))
        self.getTrack(trackID).vel = vel

    def addTrack(self, inst=0, vel=100):
        if self.getTrackNum() >= MAX_TRACK_NUM:
            raise OverflowError('Track numbers cannot exceed {}'.format(MAX_TRACK_NUM))
        return self._curFile.addTrack(inst, vel)

    def delTrack(self, trackID):
        if trackID not in self._curFile.tracks:
            raise ValueError('Track ID {} not found when del'.format(trackID))
        self._curFile.delTrack(trackID)
        self.curView.update()

    # File part
    def setBPM(self, bpm):
        if not isinstance(bpm, int) or bpm < 0 or bpm > 200:
            raise ValueError('bmp must be int within 0~200, not {}'.format(bpm))
        self._curFile.bpm = bpm

    def getBPM(self):
        return self._curFile.bpm

    def saveFile(self):
        # TODO: use serialization
        return

    # Play part
    def playAll(self):
        self.toFileMidi()
        self._play()

    def playTrack(self, trackID):
        self.toTrackMidi(trackID, self.getBPM())
        self._play()

    def toFileMidi(self):
        mid = MidiFile()

        for i, trackID in enumerate(self._curFile.tracks):
            midiTrack = self.toTrackMidi(trackID=trackID, bpm=self.getBPM(), channel=i, save=False)
            mid.tracks.append(midiTrack)
        mid.save('fluidsynth/tmp.mid')

    def toTrackMidi(self, trackID, bpm, channel=0, save=True):
        track = MidiTrack()
        curTrack = self.getTrack(trackID)
        pitch = [58, 60, 62, 64, 65, 67, 69, 71, 72]

        track.append(Message('program_change', channel=channel, program=curTrack.inst, time=0))
        track.append(Message('control_change', channel=channel, control=7, value=curTrack.vel, time=0))
        track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
        for note in curTrack.demoNotes:
            if note == ' ':
                track.append(Message('note_on', channel=channel, note=64, velocity=0, time=0))
                track.append(Message('note_off', channel=channel, note=64, velocity=0, time=192))
            elif int(note) > 0 and int(note) < 9:
                note = int(note)
                track.append(Message('note_on', channel=channel, note=pitch[note], velocity=100, time=0))
                track.append(Message('note_off', channel=channel, note=pitch[note], velocity=100, time=192))
        if save:
            mid = MidiFile()
            mid.tracks.append(track)
            mid.save('fluidsynth/tmp.mid')
        return track

    def sortedNote(self, trackID):
        pass
