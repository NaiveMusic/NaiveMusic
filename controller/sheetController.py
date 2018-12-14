import sys
from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
import pickle


#TODO: split some MainController function to here
# note相关操作
class SheetController():
    def __init__(self):
        self._curTrackID = None
        self._curTrack = None

    @property
    def curTrackID(self):
        return self._curTrackID

    @property
    def curTrack(self):
        return self._curTrack
    
    def addNote(self):
        pass



    