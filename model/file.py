from .track import Track
from .const import *


class File():
    def __init__(self, bpm):
        self.tracks = {}
        self.curID = 0
        self.bpm = bpm
