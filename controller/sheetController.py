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
        self._curPos = 0 # 'curPos' is an assitant parameter to keyboard input.

    def getCurTrackID(self):
        return self._curTrackID
    

    def addNote(self, key, **options):
        """ Add Note(key,vel,on,off) to curTrack.
            Suggest using missing key for default values,
            specifically when in keyboard input.

        Args:
            key (int): The 'key' property of the note

        Keyword Args:
            vel (int): The velocity property of the note. Defaults to curTrack.defaultVel.
            on (int): The start time of the note. Defaults to _curPos.
            off (int): The end time of the note. Dafaults to _curPos+1.

        """
        vel = options.get('vel', self._curTrack.vel)
        on = options.get('on', self._curPos)
        off = options.get('off', self._curPos+1)
        self._curTrack.addNote(key, vel, on, off)
        self._curPos = off


    def selectNote(self, on, off, keys=KEY_RANGE):
        #...UNFINISHED
        pass


    def delNote(self, **options):
        """ Delete all notes satisfying that
            1) note.key is in list of keys;
            2) the interval [note.on, note.off) has non-empty intersection with [on,off).

        Keyword Args:
            keys (<list>int): the list of 'key' property. Defaults to KEY_RANGE.
            on (int): the start time of the interval. Defaults to curPos-1
            off (int): the end time of the interval. Defaults to curPos

        """
        keys = options.get('keys', KEY_RANGE)
        on = options.get('on', self._curPos-1)
        off = options.get('off', self._curPos)

        delNoteIDList = self._curTrack.search(keys, on, off)
        for noteID in delNoteIDList:
            self._curTrack.delNote(noteID)        
        self._curPos = on

    def setCurPosition(self, curPos):
        """ Set current (time) position to a new one.

        P.S. 
            Should be called right after every click or arrowkeys input.
        """
        self._curPos = curPos

    def getTrackInfo(self):
        """ Fetches info of curTrack.

        Return: a dict structure. For example:
            {'Instrument': 69,
             'Velocity': 100}
        """
        trackInfo = {}
        trackInfo['Instrument'] = self._curTrack.inst
        trackInfo['Velocity'] = self._curTrack.vel
        return trackInfo


    def getNotesInfo(self, keys, on, off):
        """ Fetches info of all notes satisfying that
            1) note.key is in list of keys;
            2) the interval [note.on, note.off) has non-empty intersection with [on,off).
        
        Keyword Args:
            keys (<list>int): the list of 'key' property. Defaults to KEY_RANGE.
            on (int): the start time of the interval. Defaults to curPos-1
            off (int): the end time of the interval. Defaults to curPos

        Return: a list-dict structure. For example:
                [noteInfo1,noteInfo2,noteInfo3]
            where
                noteInfo1 = {'key':18,'vel':100,'on':13,'off':14},
                noteInfo2 = {'key':19,'vel':100,'on':14,'off':15},
                noteInfo3 = {'key':16,'vel':100,'on':15,'off':16},
        """
        noteInfoList = []
        noteIDList = self._curTrack.search(keys, on, off)
        for noteID in noteIDList:
            note = self._curTrack.getNote(noteID)
            noteInfo = {}
            noteInfo['Key'] = note.key
            noteInfo['Velocity'] = note.vel
            noteInfo['On'] = note.on
            noteInfo['Off'] = note.off
            noteInfoList.append(noteInfo)
        return noteInfoList