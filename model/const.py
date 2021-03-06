from enum import Enum
import re

MAX_TRACK_NUM = 16

# for note and track
DEFAULT_VEL = 100

# for track
DEFAULT_INST = 0

# for file
DEFAULT_BPM = 120
KEY_TOP = 108

# TICKS_PER_BEAT
DELTA = 120

KEY_RANGE = range(0, 128)

VEL_RANGE = range(0, 128)

STATE = Enum('STATE', ('DEFAULT', 'PLAYING', 'PAUSING', 'EDITING', 'SELECTING'))

INSTRUMENT = {
    0: 'Stereo Grand',
    1: 'Bright Grand',
    0: 'Stereo Grand',
    1: 'Bright Grand',
    2: 'Electric Grand',
    3: 'Honky-Tonk',
    4: 'Tine Electric Piano',
    5: 'FM Electric Piano',
    6: 'Harpsichord',
    7: 'Clavinet',
    8: 'Celeste',
    9: 'Glockenspiel',
    10: 'Music Box',
    11: 'Vibraphone',
    12: 'Marimba',
    13: 'Xylophone',
    14: 'Tubular Bells',
    15: 'Dulcimer',
    16: 'Tonewheel Organ',
    17: 'Percussive Organ',
    18: 'Rock Organ',
    19: 'Pipe Organ',
    20: 'Reed Organ',
    21: 'Accordian',
    22: 'Harmonica',
    23: 'Bandoneon',
    24: 'Nylon Guitar',
    25: 'Steel Guitar',
    26: 'Jazz Guitar',
    27: 'Clean Guitar',
    28: 'Muted Guitar',
    29: 'Overdrive Guitar',
    30: 'Distortion Guitar',
    31: 'Guitar Harmonics',
    32: 'Acoustic Bass',
    33: 'Finger Bass',
    34: 'Pick Bass',
    35: 'Fretless Bass',
    36: 'Slap Bass 1:',
    37: 'Slap Bass 2:',
    38: 'Synth Bass 1:',
    39: 'Synth Bass 2:',
    40: 'Violin',
    41: 'Viola',
    42: 'Cello',
    43: 'Double Bass',
    44: 'Stereo Strings Trem',
    45: 'Pizzicato Strings',
    46: 'Orchestral Harp',
    47: 'Timpani',
    48: 'Stereo Strings Fast',
    49: 'Stereo Strings Slow',
    50: 'Synth Strings 1:',
    51: 'Synth Strings 2:',
    52: 'Concert Choir',
    53: 'Voice Oohs',
    54: 'Synth Voice',
    55: 'Orchestra Hit',
    56: 'Trumpet',
    57: 'Trombone',
    58: 'Tuba',
    59: 'Muted Trumpet',
    60: 'French Horns',
    61: 'Brass Section',
    62: 'Synth Brass 1:',
    63: 'Synth Brass 2:',
    64: 'Soprano Sax',
    65: 'Alto Sax',
    66: 'Tenor Sax',
    67: 'Baritone Sax',
    68: 'Oboe',
    69: 'English Horn',
    70: 'Bassoon',
    71: 'Clarinet',
    72: 'Piccolo',
    73: 'Flute',
    74: 'Recorder',
    75: 'Pan Flute',
    76: 'Bottle Blow',
    77: 'Shakuhachi',
    78: 'Irish Tin Whistle',
    79: 'Ocarina',
    80: 'Square Lead',
    81: 'Saw Lead',
    82: 'Synth Calliope',
    83: 'Chiffer Lead',
    84: 'Charang',
    85: 'Solo Vox',
    86: '5:th Saw Wave',
    87: 'Bass & Lead',
    88: 'Fantasia',
    89: 'Warm Pad',
    90: 'Polysynth',
    91: 'Space Voice',
    92: 'Bowed Glass',
    93: 'Metal Pad',
    94: 'Halo Pad',
    95: 'Sweep Pad',
    96: 'Ice Rain',
    97: 'Soundtrack',
    98: 'Crystal',
    99: 'Atmosphere',
    100: 'Brightness',
    101: 'Goblin',
    102: 'Echo Drops',
    103: 'Star Theme',
    104: 'Sitar',
    105: 'Banjo',
    106: 'Shamisen',
    107: 'Koto',
    108: 'Kalimba',
    109: 'Bagpipes',
    110: 'Fiddle',
    111: 'Shenai',
    112: 'Tinker Bell',
    113: 'Agogo',
    114: 'Steel Drums',
    115: 'Wood Block',
    116: 'Taiko Drum',
    117: 'Melodic Tom',
    118: 'Synth Drum',
    119: 'Reverse Cymbal',
    120: 'Fret Noise',
    121: 'Breath Noise',
    122: 'Seashore',
    123: 'Birds',
    124: 'Telephone 1:',
    125: 'Helicopter',
    126: 'Applause',
    127: 'Gun Shot',
}

def style(instName, state=True):
    p1 = r"Piano"
    p2 = r"Grand"
    p3 = r"Bass"
    p4 = r"Guitar"
    p5 = r"Drum"
    p6 = r"Organ"
    if state:
        border_color = "beige"
    else:
        border_color = "black"

    if re.search(p1, instName) or re.search(p2, instName) or re.search(p6, instName) :
        style = """
            .QPushButton {
                width: 20px;
                height: 20px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: %s;
                padding: 15px;
                background-color: rgb(204, 255, 229);
                image: url('view/Icons/instrument/piano.svg');
            
            }""" % (border_color)
        color = "rgb(204, 255, 229)"
    elif re.search(p3, instName):
        style = """
            .QPushButton {
                width: 20px;
                height: 20px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: %s;
                padding: 15px;
                background-color: rgb(255, 204, 204);
                image: url('view/Icons/instrument/bass.svg');
            
            }""" % (border_color)
        color = "rgb(255, 204, 204)"
    elif re.search(p4, instName):
        style = """
            .QPushButton {
                width: 20px;
                height: 20px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: %s;
                padding: 15px;
                background-color: rgb(102, 178, 255);
                image: url('view/Icons/instrument/guitar.svg');
            
            }""" % (border_color)
        color = "rgb(102, 178, 255)"
    elif re.search(p5, instName):
        style = """
            .QPushButton {
                width: 20px;
                height: 20px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: %s;
                padding: 15px;
                background-color: rgb(160, 160, 160);
                image: url('view/Icons/instrument/drum.svg');
            
            }""" % (border_color)
        color = "rgb(160, 160, 160)"
    else:
        style = """
            .QPushButton {
                width: 20px;
                height: 20px;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: %s;
                padding: 15px;
                background-color: rgb(255, 255, 111);
                image: url('view/Icons/instrument/default.svg');
                
            } """ % (border_color)

        color = "rgb(255, 255, 111)"

    return style, color

            

