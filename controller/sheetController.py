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
        self._curKey = 0

        self._selectedNoteIDList = []
        self._selectedKey = 0
        self._selectedOn = 0
        self._selectedOff = 0
        self._copiedNoteList = []

    def getCurTrackID(self):
        return self._curTrackID
    
    def getCurTrack(self):
        return self._curTrack

    def getCurPos(self):
        return self._curPos
    
    def getCurKey(self):
        return self._curKey

    def switchTrack(self, trackID, track):
        self._curTrackID = trackID
        self._curTrack = track
        self._curPos = 0
        self._curKey = 0
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
            vel (int): The velocity property of the note. Defaults to DAFUALT_VEL.
            on (int): The start time of the note. Defaults to _curPos.
            off (int): The end time of the note. Dafaults to _curPos+1.

        Pre-Post State:
            EDITING -> EDITING
            PAUSING -> EDITING
        """
        if self._state not in [STATE.EDITING, STATE.PAUSING]:
            return

        vel = options.get('vel', DAFUALT_VEL)
        on = options.get('on', self._curPos)
        off = options.get('off', self._curPos+1)

        if not self.isOccupied(key, self._toTick(on), self._toTick(off)):
            self._curTrack.addNote(key, vel, self._toTick(on), self._toTicks(off))
            self._curPos = off
        else:
            pass

        self._state = STATE.EDITING
        self.notify()

    def delNote(self, **options):
        """ Delete all notes satisfying that
            1) note.key is in list of keys;
            2) the interval [note.on, note.off) has non-empty intersection with [on,off),
            and put curPos to 'on'

        Keyword Args:
            keys (<list>int): the list of 'key' property. Defaults to KEY_RANGE.
            on (int): the start time of the interval. Defaults to curPos-1
            off (int): the end time of the interval. Defaults to curPos

        Pre-Post State:
            EDITING -> EDITING
            PAUSING -> EDITING

        """
        if self._state not in [STATE.EDITING, STATE.PAUSING]:
            return

        keys = options.get('keys', KEY_RANGE)
        on = options.get('on', self._curPos-1)
        off = options.get('off', self._curPos)

        delNoteIDList = self._curTrack.search(keys, self._toTick(on), self._toTick(off))
        for noteID in delNoteIDList:
            self._curTrack.delNote(noteID)        
        self._curPos = on

        self._state = STATE.EDITING
        self.notify()

    def selectNote(self, key, on, off):
        """ Put all notes in range [on,off) into selection
            and set the "origin" of selection to (key,on).

        Pre-Post State:
            EDITING -> SELECTING
            SELECTING -> SELECTING
            PAUSING -> (EDITING ->) SELECTING
        """
        if self._state not in [STATE.EDITING, STATE.SELECTING, STATE.PAUSING]:
            return

        self._selectedNoteIDList = self._curTrack.search(self._toTick(on), self._toTick(off))
        self._selectedKey = key
        self._selectedOn = on
        self._selectedOff = off
        self._curPos = on

        self._state = STATE.SELECTING
        self.notify()

    def unselectNote(self):
        """ Unselect all notes in selection
        
        Pre-Post State:
            SELECTING -> EDITING
        """
        if self._state is not STATE.SELECTING:
            return

        self._selectedNoteIDList = []
        self._selectedKey = 0
        self._selectedOn = 0

        self._state = STATE.EDITING
        self.notify()

    def delSelectedNote(self):
        """ Delete all notes in selection

        Pre-Post State:
            SELECTING -> EDITING
        """
        for noteID in self._selectedNoteIDList:
            self._curTrack.delNote(noteID)
        self._curPos = self._selectedOn

        self.unselectNote()
        self.notify()

    def copySelectedNote(self):
        """ Save a copy for all selected notes to memory.
            Data is recorded as "relative position" to the origin of the region (selectedKey,selectedOn)

        Pre-Post State:
            SELECTING -> SELECTING
        """
        if self._state is not STATE.SELECTING:
            return
    
        self._copiedNoteList = []
        for noteID in self._selectedNoteIDList:
            note = self._curTrack.getNote(noteID)
            noteInfo = {}
            noteInfo['Key'] = note.key - self._selectedKey
            noteInfo['Velocity'] = note.vel
            noteInfo['On'] = self._toSec(note.on) - self._selectedOn
            noteInfo['Off'] = self._toSec(note.off) - self._selectedOn
            self._copiedNoteList.append(noteInfo)

        self._state = STATE.SELECTING
        self.notify()
    
    def pasteSelectedNote(self):
        """ Paste all copied notes to a new region originated at (_curKey, _curPos)

        Pre-Post State:
            EDITING -> EDITING
        """
        if self._state is not STATE.EDITING:
            return

        for noteInfo in self._copiedNoteList:
            _key = noteInfo['Key'] + self._curKey
            _vel = noteInfo['Vel']
            _on = noteInfo['On'] + self._curPos
            _off = noteInfo['Off'] + self._curPos
            self._curTrack.addNote(key=_key, vel=_vel, on=self._toTick(_on), off=self._toTick(_off))
            self._curPos = _off
        
        self._state = STATE.EDITING
        self.notify()

    def isOccupied(self, key, on, off):
        """ Examine if the queried position is already occupied.
        """
        if len(self.getNotesInfo(keys=[key],on=self._toTick(on),off=self._toTick(off))) > 0:
            return True
        else:
            return False


    def setCurPosition(self, curKey, curPos):
        """ Set current (time) position to curPos.
            Set current key to curKey.

        P.S. 
            Should be called right after every click or arrowkeys input.
        """
        self._curPos = curPos
        self._curKey = curKey
        self.notify()

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
            keys (<list>int): the list of 'key' property.
            on (int): the start time of the interval.
            off (int): the end time of the interval.

        Return: a list-dict structure. For example:
                [noteInfo1,noteInfo2,noteInfo3]
            where
                noteInfo1 = {'key':18,'vel':100,'on':13,'off':14},
                noteInfo2 = {'key':19,'vel':100,'on':14,'off':15},
                noteInfo3 = {'key':16,'vel':100,'on':15,'off':16}.

        P.S.
            Notes are not neccessarily contained in the area.
        """
        noteInfoList = []
        noteIDList = self._curTrack.search(on=self._toTick(on), off=self._toTick(off), keys = keys)
        for noteID in noteIDList:
            note = self._curTrack.getNote(noteID)
            noteInfo = {}
            noteInfo['Key'] = note.key
            noteInfo['Velocity'] = note.vel
            noteInfo['On'] = self._toSec(note.on)
            noteInfo['Off'] = self._toSec(note.off)
            noteInfoList.append(noteInfo)
        return noteInfoList

    def getSelectedNotesInfo(self):
        """ Fetches info of all *SELECTED* notes.

        Pre-State:
            SELECTING

        Return: a list-dict structure. For example:
                [noteInfo1,noteInfo2,noteInfo3]
            where
                noteInfo1 = {'key':18,'vel':100,'on':13,'off':14},
                noteInfo2 = {'key':19,'vel':100,'on':14,'off':15},
                noteInfo3 = {'key':16,'vel':100,'on':15,'off':16}.

        P.S.
            Notes are not neccessarily intersected with the area.
        """
        if self._state is not STATE.SELECTING:
            return []

        noteInfoList = []
        noteIDList = self._selectedNoteIDList
        for noteID in noteIDList:
            note = self._curTrack.getNote(noteID)
            noteInfo = {}
            noteInfo['Key'] = note.key
            noteInfo['Velocity'] = note.vel
            noteInfo['On'] = self._toSec(note.on)
            noteInfo['Off'] = self._toSec(note.off)
            noteInfoList.append(noteInfo)
        return noteInfoList

    def _toTick(self, sec):
        return sec * DELTA

    def _toSec(self, tick):
        return round(tick / float(DELTA))