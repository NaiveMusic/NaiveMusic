import sys
from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
import pickle

#TODO: split some MainController function to here
class SheetController():
    def __init__(self):
        self.curTrack = None

