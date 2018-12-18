import os
import subprocess
from ctypes import *
from ctypes.util import find_library


class AudioController():
    def __init__(self):
        os.chdir('./fluidsynth')
        if os.sys.platform.startswith('win'):
            lib = find_library('libfluidsynth-2.dll')
        elif os.sys.platform.startswith('linux'):
            raise NotImplementedError('TODO for tomorrow')
        elif os.sys.platform.startswith('darwin'):
            raise NotImplementedError('TODO for wu tong xue')
        if lib is None:
            raise ImportError("Couldn't find the FluidSynth library.")
        self._fl = CDLL(lib)
        self._defFuncs()
        self.settings = self.new_fluid_settings()
        self.synth = self.new_fluid_synth(self.settings)
        self.adriver = self.new_fluid_audio_driver(self.settings, self.synth)
        self.fluid_synth_sfload(self.synth, b"GeneralUser_GS.sf2", 1)
        os.chdir('..')

    def __del__(self):
        self.delete_fluid_audio_driver(self.adriver)
        self.delete_fluid_synth(self.synth)
        self.delete_fluid_settings(self.settings)

    def _play(self):
        self.player = self.new_fluid_player(self.synth)
        self.fluid_player_add(self.player, b"fluidsynth\\tmp.mid")
        self.fluid_player_play(self.player)
        self.fluid_player_join(self.player)
        self.delete_fluid_player(self.player)

    def _defFuncs(self):
        def cfunc(name, result, *args):
            atypes, aflags = [], []
            for arg in args:
                atypes.append(arg[1])
                aflags.append((arg[2], arg[0]) + arg[3:])
            return CFUNCTYPE(result, *atypes)((name, self._fl), tuple(aflags))

        #settings
        self.new_fluid_settings = cfunc('new_fluid_settings', c_void_p)

        self.fluid_settings_setstr = cfunc('fluid_settings_setstr', c_int,\
                                    ('settings', c_void_p, 1),\
                                    ('name', c_char_p, 1),\
                                    ('str', c_char_p, 1))

        self.fluid_settings_setint = cfunc('fluid_settings_setint', c_int,\
                                    ('settings', c_void_p, 1),\
                                    ('name', c_char_p, 1),\
                                    ('val', c_int, 1))

        #new
        self.new_fluid_synth = cfunc('new_fluid_synth', c_void_p,\
                                ('settings', c_void_p, 1))

        self.new_fluid_player = cfunc('new_fluid_player',c_void_p,\
                                ('synth',c_void_p,1))

        self.new_fluid_audio_driver = cfunc('new_fluid_audio_driver', c_void_p, \
                                        ('settings', c_void_p, 1),\
                                        ('synth', c_void_p, 1))

        self.fluid_synth_sfload = cfunc('fluid_synth_sfload', c_int,\
                                ('synth', c_void_p, 1),\
                                ('filename', c_char_p, 1),\
                                ('update_midi_presets', c_int, 1))\

        #player
        self.fluid_player_add = cfunc('fluid_player_add',c_void_p,\
                                ('player',c_void_p,1),\
                                ('midifile',c_char_p,1))

        self.fluid_player_play = cfunc('fluid_player_play',c_void_p,\
                                ('player',c_void_p,1))

        self.fluid_player_join = cfunc('fluid_player_join',c_void_p,\
                                ('player',c_void_p,1))

        #delete
        self.delete_fluid_audio_driver = cfunc('delete_fluid_audio_driver', None,\
                                        ('driver', c_void_p, 1))

        self.delete_fluid_synth = cfunc('delete_fluid_synth', None,\
                                ('synth', c_void_p, 1))

        self.delete_fluid_settings = cfunc('delete_fluid_settings', None,\
                                    ('settings', c_void_p, 1))

        self.delete_fluid_player = cfunc('delete_fluid_player',c_void_p,\
                                ('player',c_void_p,1))
