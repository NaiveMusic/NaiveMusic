import os


class AudioController():
    def __init__(self):
        self.cmd = r'fluidsynth\fluidsynth.exe -ni fluidsynth\GeneralUser_GS.sf2 tmp.mid'

    def play(self):
        os.system(self.cmd)
