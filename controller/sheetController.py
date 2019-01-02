import sys
from model.note import Note
from model.file import File
from model.track import Track
from model.const import *
from controller.baseController import BaseController
import pickle


class SheetController(BaseController):
    def __init__(self):
        BaseController.__init__(self)
        self._curTrackID = None
        self._curTrack = None
        self._curPos = 0 # 'curPos' is an assitant parameter to keyboard input.

        self._selectedNoteIDList = []
        self._selectedKey = 0
        self._selectedOn = 0
        self._selectedOff = 0
        self._copiedNoteList = []

    def getCurTrackID(self):
        return self._curTrackID
    
    def getCurTrack(self):
        return self._curTrack

    def switchTrack(self, trackID, track):
        self._curTrackID = trackID
        self._curTrack = track
        self._curPos = 0
        self._selectedNoteIDList = []
        self._selectedKey = 0
        self._selectedOn = 0
        self._selectedOff = 0
        self.notify()

    def addNote(self, key, **options):
        """ Add Note(key,vel,on,off) to curTrack, and put curPos to 'off'
            Suggest using kwarg for default values,
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
        if not self.isOccupied(key,on,off):
            try:
                self._curTrack.addNote(key, vel, on, off)
            except ValueError:
                pass
            else:
                self._curPos = off
            finally:
                pass
        else:
            pass

    def delNote(self, **options):
        """ Delete all notes satisfying that
            1) note.key is in list of keys;
            2) the interval [note.on, note.off) has non-empty intersection with [on,off),
            and put curPos to 'on'

        Keyword Args:
            keys (<list>int): the list of 'key' property. Defaults to KEY_RANGE.
            on (int): the start time of the interval. Defaults to curPos-1
            off (int): the end time of the interval. Defaults to curPos

        """
        keys = options.get('keys', KEY_RANGE)
        on = options.get('on', self._curPos-1)
        off = options.get('off', self._curPos)

        delNoteIDList = self._curTrack.search(on, off,keys)
        for noteID in delNoteIDList:
            self._curTrack.delNote(noteID)        
        self._curPos = on

    def selectNote(self, key, on, off):
        """ Put all notes in range [on,off) into selection
            and set the "origin" of selection to (key,on).
            Meanwhile the state of controller is set to 'SELECTING'
        """
        self._selectedNoteIDList = self._curTrack.search(on, off)
        self._selectedKey = key
        self._selectedOn = on
        self._selectedOff = off
        self._state = STATE.SELECTING
        self._curPos = on
        pass

    def unselectNote(self):
        """ Remove all notes in selection
            and set the state of controller to 'EDITING'
        """
        if self._state is STATE.SELECTING:
            self._selectedNoteIDList = []
            self._selectedKey = 0
            self._selectedOn = 0
            self._state = STATE.EDITING

    def delSelectedNote(self):
        for noteID in self._selectedNoteIDList:
            self._curTrack.delNote(noteID)
        self._curPos = self._selectedOn
        self.unselectNote()

    def copySelectedNote(self):
        """ Save a copy for all selected notes to controller.
            Data is recorded as "relative position" to the origin of the region (selectedKey,selectedOn)
        """
        if self._state is not STATE.SELECTING:
            pass
        else:
            self._copiedNoteList = []
            for noteID in self._selectedNoteIDList:
                note = self._curTrack.getNote(noteID)
                noteInfo = {}
                noteInfo['Key'] = note.key - self._selectedKey
                noteInfo['Velocity'] = note.vel
                noteInfo['On'] = note.on - self._selectedOn
                noteInfo['Off'] = note.off - self._selectedOn
                self._copiedNoteList.append(noteInfo)
    
    def pasteSelectedNote(self, key, on):
        """ Paste all copied notes to a new region originated at (key,on)
        """
        for noteInfo in self._copiedNoteList:
            _key = noteInfo['Key'] + key
            _vel = noteInfo['Vel']
            _on = noteInfo['On'] + on
            _off = noteInfo['Off'] + on
            self.addNote(key=_key, vel=_vel, on=_on, off=_off)
        self._curPos = self._selectedOff
        

    def isOccupied(self, key, on, off):
        if len(self.getNotesInfo(keys=[key],on=on,off=off)) > 0:
            return True
        else:
            return False


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
        noteIDList = self._curTrack.search(on, off,keys)
        for noteID in noteIDList:
            note = self._curTrack.getNote(noteID)
            noteInfo = {}
            noteInfo['Key'] = note.key
            noteInfo['Velocity'] = note.vel
            noteInfo['On'] = note.on
            noteInfo['Off'] = note.off
            noteInfoList.append(noteInfo)
        return noteInfoList