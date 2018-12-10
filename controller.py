from track import Track
from note import Note
from file import File
from const import *
import pickle

## TODO
# ADD BPM,MPB in class File
# ADD search() in class Track
# ADD keyDict in const.py
# del mechanics

# THIS VERSION HAS NOT BEEN TESTED

class Controller():
	def __init__(self):
		self.__file = NULL
		self.__track = NULL
		self.__trackDict = {} #{'viewID':'trackID'}
		self.__cwTrackID = -1
		self.__cwPos = -1
		self.__defaultInst = 0
		self.__defaultVel = 100
		self.__states = 'EMPTY'
	

	# File Manager Part

	def createNewFile():
		self.__file = File()
		self.__states = 'EDITABLE'

	def saveFile():
		pickle.dump(__file, open("test.nm", "wb"))
		
	def loadFile():
		self.__file = pickle.load(open("test.nm", "rb"))
		self.__states = 'EDITABLE'
	
	def delFile():
		del self.__file # file.destruct()? del track?
		self.__track = NULL
		self.__cwPos = -1
		self.__cwTrackID = -1
		self.__trackDict.clear()
		self.__states = 'EMPTY'


	# Track Manager Part

	def setWorkingTrack(viewID):
		self.__cwTrackID = self.__trackDict[viewID]
		self.__track = self.__file.getTrack(self.__cwTrackID)
		self.__cwPos = 0

	def addTrack(viewID, inst=self.__defaultInst, vel=self.__defaultVel):
		# create and switch cwTrack to a new track
		trackID = self.__file.addTrack(inst,vel)
		self.__trackDict[viewID] = trackID
		self.setWorkingTrack(viewID)

	def delTrack(viewID, toViewID):
		# delete track[viewID] and switch cwTrack to track[toViewID]
		if viewID not in self.__trackDict:
			raise ValueError('Track not found')
		self.__file.delTrack(self.__trackDict[viewID])
		del self.__trackDict[viewID]

		if toViewID not in self.__trackDict:
			toViewID = list(self.__trackDict.keys())[0]
		self.setWorkingTrack(toViewID)

	def setWorkingPosition(cwPos):
		# called right after every single click input
		# or called after arrow keys input
		self.__cwPos = cwPos
		
	def addNote(key, vel, on = self.__cwPos, off = self.__cwPos+1):
		# use default value while using keyboard input
		self.__track.addNote(key, vel, on, off)
		self.__cwPos = off

	def selectNote(keys = [], on=self.__cwPos, off=self.__cwPos+1):
		noteList = self.__track.search(key, on, off)
		#...UNFINISHED

	def delNote(keys = [], on=self.__cwPos-1, off=self.__cwPos):
		# use default value while using keyboard input
		noteList = self.__track.search(key, on, off)
		for noteID in noteList:
			self.__track.delNote(noteID)
		#...UNFINISHED


	# Info Part

	def getTrackInfo(viewID = NULL):
		if viewID == NULL:
			track = self.__track
		else
			track = self.__file.getTrack(self.__trackDict[viewID])

		inst, vel = track.getInfo()

		trackInfo = {}
		trackInfo['Instrument'] = inst;
		trackInfo['Velocity'] = vel
		
		return trackInfo

	def getFileInfo():
		#...UNFINISHED
		pass


	# Test Function

	def display():
		# for python 2.7.10
		print '-'*10
		print 'Now playing...'
		for viewID,trackID in self.__trackDict.items():
			trackInfo = self.getTrackInfo(viewID)
			s = 'Track {}, Inst {}:'.format(trackID, INSTRUMENT[trackInfo['Instrument']])
			track = self.__file.getTrack(trackID)
			for noteID,note in track.__notes.items():
				s += ' {}'.format(note.__key)
			print s
		print '-'*10		
		pass

		







