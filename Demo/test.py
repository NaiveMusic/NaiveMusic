import time
import numpy
import pyaudio
import sys
import os

# os.environ["PATH"] += os.pathsep+r'E:\SoftwareEngineering\NaiveMusic\NaiveMusic\Demo\fluidsynth'
# os.environ["PATH"] += os.pathsep+r'E:\SoftwareEngineering\NaiveMusic\NaiveMusic\Demo\fluidsynth\bin'
# print(os.environ['PATH'])
# exit()
import fluidsynth
# os.system(r'set PATH=E:\SoftwareEngineering\NaiveMusic\NaiveMusic\Demo\fluidsynth;%PATH%')
# os.system(r'set PATH=E:\SoftwareEngineering\NaiveMusic\NaiveMusic\Demo\fluidsynth\bin;%PATH%')

pa = pyaudio.PyAudio()
strm = pa.open(
    format = pyaudio.paInt16,
    channels = 2, 
    rate = 44100, 
    output = True)

s = []

fl = fluidsynth.Synth()

# Initial silence is 1 second
s = numpy.append(s, fl.get_samples(44100 * 1))

sfid = fl.sfload("example.sf2")
fl.program_select(0, sfid, 0, 0)
if sys.argv.__len__()==1:
    a=1
else:
    a=int(sys.argv[1])
fl.noteon(0, a+60, 30)
# fl.noteon(0, 67, 30)
# fl.noteon(0, 76, 30)

# Chord is held for 2 seconds
s = numpy.append(s, fl.get_samples(44100 * 1))

fl.noteoff(0, a+60)
# fl.noteoff(0, 67)
# fl.noteoff(0, 76)

# Decay of chord is held for 1 second
s = numpy.append(s, fl.get_samples(44100 * 1))

fl.delete()

samps = fluidsynth.raw_audio_string(s)

# print len(samps)
# print 'Starting playback'
strm.write(samps)