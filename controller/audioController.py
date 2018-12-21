import os
import subprocess
import numpy as np
from ctypes import *
from ctypes.util import find_library
import threading
from lib.pyaudio import pyaudio

import wave
from io import BytesIO
import time

class AudioController():
    def __init__(self):
        os.chdir('./lib/fluidsynth')
        if os.sys.platform.startswith('win'):
            lib = find_library('libfluidsynth-2.dll')
        elif os.sys.platform.startswith('linux'):
            raise NotImplementedError('TODO')
        elif os.sys.platform.startswith('darwin'):
            raise NotImplementedError('TODO for wu tong xue')
        if lib is None:
            raise ImportError("Couldn't find the FluidSynth library.")

        self.changed = True

        self._fl = CDLL(lib)
        self._initFuncs()
        self.settings = self.new_fluid_settings()
        self.fluid_settings_setstr(self.settings, b"player.timing-source", b"sample")
        self.fluid_settings_setint(self.settings, b"synth.lock-memory", 0)
        self.synth = self.new_fluid_synth(self.settings)
        self.fluid_synth_sfload(self.synth, b"GeneralUser_GS.sf2", 1)
        os.chdir('../..')

        self.pa = pyaudio.PyAudio()
        self.strm = self.pa.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True, start=False,
                                 stream_callback=self._callback)
        # self.strm = self.pa.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True)

    def __del__(self):
        self.delete_fluid_synth(self.synth)
        self.delete_fluid_settings(self.settings)
        self.pa.terminate()
        self.wf.close()

    def _callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def _play(self, buf, length, changed=True):
        if changed:
            sample = self._getSample(buf, length)
        if self.strm.is_active():
            print('playing!')
            return
        self.strm.stop_stream()
        # self.wf.
        # self.strm.write(sample)
        self.strm.start_stream()

    def _stop(self):
        self.strm.stop_stream()

    def _getSample(self, buf, length):
        buf.seek(0)
        buf = buf.read()

        player = self.new_fluid_player(self.synth)
        self.fluid_player_add_mem(player, buf, len(buf))
        self.fluid_player_play(player)

        length = int(44100 * length)
        buf = create_string_buffer(length * 4)
        self.fluid_synth_write_s16(self.synth, length, buf, 0, 2, buf, 1, 2)
        sample = np.frombuffer(buf, dtype=np.int16).tobytes()

        self.fluid_player_stop(player)
        self.fluid_player_join(player)
        self.delete_fluid_player(player)
        buf = BytesIO()
        with wave.open(buf, 'wb') as wf:
            wf.setparams((2, 2, 44100, 0, 'NONE', 'NONE'))
            wf.writeframes(sample)
        buf.seek(0)
        self.wf = wave.open("C:/Windows/media/Ring05.wav", 'rb')
        print(self.wf.getparams())
        self.wf = wave.open(buf, 'rb')
        print(self.wf.getparams())

        return sample

    def _cfunc(self, name, result, *args):
        atypes, aflags = [], []
        for arg in args:
            atypes.append(arg[1])
            aflags.append((arg[2], arg[0]) + arg[3:])
        return CFUNCTYPE(result, *atypes)((name, self._fl), tuple(aflags))

    def _initFuncs(self):
        #settings
        self.new_fluid_settings = self._cfunc('new_fluid_settings', c_void_p)

        self.fluid_settings_setstr = self._cfunc('fluid_settings_setstr', c_int,\
                                                ('settings', c_void_p, 1),\
                                                ('name', c_char_p, 1),\
                                                ('str', c_char_p, 1))

        self.fluid_settings_setint = self._cfunc('fluid_settings_setint', c_int,\
                                                ('settings', c_void_p, 1),\
                                                ('name', c_char_p, 1),\
                                                ('val', c_int, 1))

        #new
        self.new_fluid_synth = self._cfunc('new_fluid_synth', c_void_p,\
                                          ('settings', c_void_p, 1))

        self.new_fluid_player = self._cfunc('new_fluid_player',c_void_p,\
                                           ('synth',c_void_p,1))

        self.new_fluid_audio_driver = self._cfunc('new_fluid_audio_driver', c_void_p, \
                                                 ('settings', c_void_p, 1),\
                                                 ('synth', c_void_p, 1))

        self.fluid_synth_sfload = self._cfunc('fluid_synth_sfload', c_int,\
                                             ('synth', c_void_p, 1),\
                                             ('filename', c_char_p, 1),\
                                             ('update_midi_presets', c_int, 1))\

        #player
        self.fluid_player_add = self._cfunc('fluid_player_add',c_void_p,\
                                           ('player',c_void_p,1),\
                                           ('midifile',c_char_p,1))

        self.fluid_player_add_mem = self._cfunc('fluid_player_add_mem',c_void_p,\
                                               ('player',c_void_p,1),\
                                               ('buffer',c_void_p,1),\
                                               ('len',c_uint,1))

        self.fluid_player_play = self._cfunc('fluid_player_play',c_void_p,\
                                            ('player',c_void_p,1))

        self.fluid_player_stop = self._cfunc('fluid_player_stop',c_void_p,\
                                            ('player',c_void_p,1))

        self.fluid_player_join = self._cfunc('fluid_player_join',c_void_p,\
                                            ('player',c_void_p,1))

        #delete
        self.delete_fluid_audio_driver = self._cfunc('delete_fluid_audio_driver', None,\
                                                    ('driver', c_void_p, 1))

        self.delete_fluid_synth = self._cfunc('delete_fluid_synth', None,\
                                             ('synth', c_void_p, 1))

        self.delete_fluid_settings = self._cfunc('delete_fluid_settings', None,\
                                                ('settings', c_void_p, 1))

        self.delete_fluid_player = self._cfunc('delete_fluid_player',c_void_p,\
                                              ('player',c_void_p,1))

        self.fluid_synth_write_s16 = self._cfunc('fluid_synth_write_s16', c_void_p,\
                                                ('synth', c_void_p, 1),\
                                                ('len', c_int, 1),\
                                                ('lbuf', c_void_p, 1),\
                                                ('loff', c_int, 1),\
                                                ('lincr', c_int, 1),\
                                                ('rbuf', c_void_p, 1),\
                                                ('roff', c_int, 1),\
                                                ('rincr', c_int, 1))
