import os
import subprocess
import ctypes

class AudioController():
    def __init__(self):
        if os.sys.platform.startswith('win'):
            self.player = subprocess.Popen(['fluidsynth\\player.exe'], stdin=subprocess.PIPE, bufsize=0)
        elif os.sys.platform.startswith('linux'):
            pass
        elif os.sys.platform.startswith('darwin'):
            pass


    def _play(self):
        if os.sys.platform.startswith('win'):
            self.player.stdin.write(bytes('a', encoding='utf8'))
        elif os.sys.platform.startswith('linux'):
            os.system('fluidsynth -a pulseaudio -ni fluidsynth/GeneralUser_GS.sf2 fluidsynth/tmp.mid')
        elif os.sys.platform.startswith('darwin'):
            pass

        