from track import Track
from note import Note
from file import File
from const import *

## TODO
# ADD BPM,MPB in class File
# ADD search() in class Track
# ADD keyDict in const.py
# COMPLETE demo 2.0 using MVC


class Controller():
	def __init__(self):
		self.__file = NULL
		self.__track = NULL
		self.__trackDict = {'viewID':'trackID'}
		self.__cwTrackID = 0
		self.__cwPos = 0
		self.__defaultInst = 0
		self.__defaultVel = 100
		self.__states = 'DEFAULT'
	
	def createNewFile():
		
	def saveFile():
	
	def loadFile():
	
	def delFile():



	def setWorkingTrack(viewID):
		self.__cwTrackID = self.__trackDict[viewID]
		self.__track = self.__file.getTrack(self.__cwTrackID)
		self.__cwPos = 0

	def addTrack(viewID, inst=self.__defaultInst, vel=self.__defaultVel):
		trackID = __file.addTrack(inst,vel) ##
		self.__trackDict[viewID] = trackID
		self.setWorkingTrack(viewID)

	def delTrack(viewID, toViewID):
		self.__file.delTrack(self.__trackDict[viewID])
		del self.__trackDict[viewID]
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
		#...

	def delNote(keys = [], on=self.__cwPos-1, off=self.__cwPos):
		# use default value while using keyboard input
		noteList = self.__track.search(key, on, off)
		for noteID in noteList:
			self.__track.delNote(noteID)

	def function():
		pass







