import os
import wave
import time
import subprocess
from ctypes import *
from ctypes.util import find_library
from io import BytesIO

from model.const import *
from controller.baseController import BaseController
from lib.pyaudio import pyaudio
from lib.mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage


class AudioController(BaseController):
    def __init__(self):
        os.chdir('./lib/fluidsynth')
        if os.sys.platform.startswith('win'):
            lib = windll.LoadLibrary('libfluidsynth-2.dll')
        elif os.sys.platform.startswith('linux'):
            raise NotImplementedError('TODO')
        elif os.sys.platform.startswith('darwin'):
            raise NotImplementedError('TODO for wu tong xue')

        if lib is None:
            raise ImportError("Couldn't find the FluidSynth library.")

        self._fl = lib
        self._initFuncs()
        self._settings = self._new_fluid_settings()
        self._fluid_settings_setstr(self._settings, b"player.timing-source", b"sample")
        self._fluid_settings_setint(self._settings, b"synth.lock-memory", 0)
        self._synth = self._new_fluid_synth(self._settings)
        self._fluid_synth_sfload(self._synth, b"GeneralUser_GS.sf2", 1)
        os.chdir('../..')

        self._pa = pyaudio.PyAudio()
        self._strm = self._pa.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True, start=False,
                                   stream_callback=self._callback)
        self._strm2 = self._pa.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True, start=False,
                                   stream_callback=self._callback)

    def __del__(self):
        self._delete_fluid_synth(self._synth)
        self._delete_fluid_settings(self._settings)
        self._pa.terminate()
        self._wf.close()

    def _callback(self, in_data, frame_count, time_info, status):
        data = self._wf.readframes(frame_count)
        if len(data) < 4096:
            self._state = STATE.EDITING
        return (data, pyaudio.paContinue)

    def _play(self, buf, length):
        if self._strm.is_active():
            print('playing!')
            return
        if self._state != STATE.PAUSING:
            self._getSample(buf, length)
        self._state = STATE.PLAYING
        self._strm.stop_stream()
        self._strm.start_stream()

    def _pause(self):
        if self._strm.is_active():
            self._state = STATE.PAUSING
        self._strm.stop_stream()

    def _playSingle(self, inst, key):
        track = MidiTrack()
        track.append(Message('program_change', channel=0, program=inst, time=0))
        track.append(Message('note_on', channel=0, note=key, velocity=100, time=0))
        track.append(Message('note_off', channel=0, note=key, velocity=0, time=DELTA//2))
        track.append(Message('note_on', channel=0, note=key, velocity=0, time=0))
        track.append(Message('note_off', channel=0, note=key, velocity=0, time=DELTA//4))
        buf = BytesIO()
        mid = MidiFile()
        mid.tracks.append(track)
        mid.save(file=buf)
        self._getSample(buf, mid.length)
        self._strm2.stop_stream()
        self._strm2.start_stream()

    def _getSample(self, buf, length,export=False,filename=None):
        buf.seek(0)
        buf = buf.read()

        player = self._new_fluid_player(self._synth)
        self._fluid_player_add_mem(player, buf, len(buf))
        self._fluid_player_play(player)

        length = int(44100 * length)
        buf = create_string_buffer(length * 4)
        self._fluid_synth_write_s16(self._synth, length, buf, 0, 2, buf, 1, 2)
        sample = buf.raw

        self._fluid_player_stop(player)
        self._fluid_player_join(player)
        self._delete_fluid_player(player)
        if export: buf = open(filename,'rb')
        else: buf = BytesIO()

        with wave.open(buf, 'wb') as wf:
            wf.setparams((2, 2, 44100, 0, 'NONE', 'NONE'))
            wf.writeframes(sample)
        buf.seek(0)
        
        if export: buf.close()
        else: self._wf = wave.open(buf, 'rb')


    def _cfunc(self, name, result, *args):
        atypes, aflags = [], []
        for arg in args:
            atypes.append(arg[1])
            aflags.append((arg[2], arg[0]) + arg[3:])
        return CFUNCTYPE(result, *atypes)((name, self._fl), tuple(aflags))

    def _initFuncs(self):
        #settings
        self._new_fluid_settings = self._cfunc('new_fluid_settings', c_void_p)

        self._fluid_settings_setstr = self._cfunc('fluid_settings_setstr', c_int,\
                                                ('settings', c_void_p, 1),\
                                                ('name', c_char_p, 1),\
                                                ('str', c_char_p, 1))

        self._fluid_settings_setint = self._cfunc('fluid_settings_setint', c_int,\
                                                ('settings', c_void_p, 1),\
                                                ('name', c_char_p, 1),\
                                                ('val', c_int, 1))

        #new
        self._new_fluid_synth = self._cfunc('new_fluid_synth', c_void_p,\
                                          ('settings', c_void_p, 1))

        self._new_fluid_player = self._cfunc('new_fluid_player',c_void_p,\
                                           ('synth',c_void_p,1))

        self._new_fluid_audio_driver = self._cfunc('new_fluid_audio_driver', c_void_p, \
                                                 ('settings', c_void_p, 1),\
                                                 ('synth', c_void_p, 1))

        self._fluid_synth_sfload = self._cfunc('fluid_synth_sfload', c_int,\
                                             ('synth', c_void_p, 1),\
                                             ('filename', c_char_p, 1),\
                                             ('update_midi_presets', c_int, 1))\

        #player
        self._fluid_player_add = self._cfunc('fluid_player_add',c_void_p,\
                                           ('player',c_void_p,1),\
                                           ('midifile',c_char_p,1))

        self._fluid_player_add_mem = self._cfunc('fluid_player_add_mem',c_void_p,\
                                               ('player',c_void_p,1),\
                                               ('buffer',c_void_p,1),\
                                               ('len',c_uint,1))

        self._fluid_player_play = self._cfunc('fluid_player_play',c_void_p,\
                                            ('player',c_void_p,1))

        self._fluid_player_stop = self._cfunc('fluid_player_stop',c_void_p,\
                                            ('player',c_void_p,1))

        self._fluid_player_join = self._cfunc('fluid_player_join',c_void_p,\
                                            ('player',c_void_p,1))

        #delete
        self._delete_fluid_audio_driver = self._cfunc('delete_fluid_audio_driver', None,\
                                                    ('driver', c_void_p, 1))

        self._delete_fluid_synth = self._cfunc('delete_fluid_synth', None,\
                                             ('synth', c_void_p, 1))

        self._delete_fluid_settings = self._cfunc('delete_fluid_settings', None,\
                                                ('settings', c_void_p, 1))

        self._delete_fluid_player = self._cfunc('delete_fluid_player',c_void_p,\
                                              ('player',c_void_p,1))

        self._fluid_synth_write_s16 = self._cfunc('fluid_synth_write_s16', c_void_p,\
                                                ('synth', c_void_p, 1),\
                                                ('len', c_int, 1),\
                                                ('lbuf', c_void_p, 1),\
                                                ('loff', c_int, 1),\
                                                ('lincr', c_int, 1),\
                                                ('rbuf', c_void_p, 1),\
                                                ('roff', c_int, 1),\
                                                ('rincr', c_int, 1))
