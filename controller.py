from track import Track
from note import Note
from file import File
from const import *
import pickle

## TODO
# ADD BPM,MPB in class File
# ADD search() in class Track
# ADD keyDict in const.py

## I DONT KNOW
# del mechanics
# multiple missing value input

class Controller():
	def __init__(self):
		self.__file = None
		self.__track = None
		self.__trackDict = {} #{'viewID':'trackID'}
		self.__cwTrackID = -1
		self.__cwViewID = -1
		self.__cwPos = -1
		self.__defaultInst = 0
		self.__defaultVel = 100
		self.__states = 'EMPTY'
		self.__switcher = {'EDITABLE':self.display1,'EMPTY':self.display2}
	

	# File Manager Part

	def createNewFile(self):
		self.__file = File()
		self.__states = 'EDITABLE'
		self.log('Create new file')

	def saveFile(self):
		pickle.dump(__file, open("test.nm", "wb"))
		self.log('Save file to test.nm')
		
	def loadFile(self):
		self.__file = pickle.load(open("test.nm", "rb"))
		self.__states = 'EDITABLE'
		self.log('Load file from test.nm')
	
	def delFile(self):
		del self.__file # file.destruct()? del track?
		self.clearConfig()
		self.__states = 'EMPTY'
		self.log('Delete file')

	def getState(self):
		state = self.__states
		return state

	# Track Manager Part

	def setWorkingTrack(self, viewID):
		if viewID not in self.__trackDict:
			raise ValueError('Track not found')
		self.__cwViewID = viewID
		self.__cwTrackID = self.__trackDict[viewID]
		self.__track = self.__file.getTrack(self.__cwTrackID)
		self.__cwPos = 0
		self.log('Set Working Track to Track {}'.format(self.__cwTrackID))

	def getWorkingTrack(self):
		cwViewID = self.__cwViewID
		return	cwViewID

	def addTrack(self, viewID, **options):
		# create and switch cwTrack to a new track
		# attach viewID with the new track
		inst = options.get('inst', self.__defaultInst)
		vel = options.get('vel', self.__defaultVel)

		trackID = self.__file.addTrack(inst,vel)
		self.__trackDict[viewID] = trackID
		self.setWorkingTrack(viewID)
		self.log('Add Track {} attached with View {}'.format(self.__cwTrackID,self.__cwViewID))

	def delTrack(self, viewID, **options):
		# delete track[viewID] and switch cwTrack to track[toViewID]
		# unattach viewID with the deleted track
		if viewID not in self.__trackDict:
			raise ValueError('Track not found')
		delTrackID = self.__trackDict[viewID]
		self.__file.delTrack(delTrackID)
		del self.__trackDict[viewID]
		
		self.log('Delete Track {}'.format(delTrackID))

		if len(self.__trackDict) == 0:
			self.clearConfig()
			return
		toViewID = options.get('toViewID', list(self.__trackDict.keys())[0])
		self.setWorkingTrack(toViewID)

	def setWorkingPosition(self, cwPos):
		# called right after every single click input
		# or called after arrow keys input
		self.__cwPos = cwPos
		self.log('Set Working Position to {}'.format(cwPos))
		
	def addNote(self, key, **options):
		# use default value while using keyboard input
		vel = options.get('vel', self.__defaultVel)
		on = options.get('on', self.__cwPos)
		off = options.get('off', self.__cwPos+1)
		self.__track.addNote(key, vel, on, off)
		self.__cwPos = off
		self.log('Add Node key={}, on={}, off={} to Track {}'.format(key,on,off,self.__cwTrackID))

	def selectNote(self):
		#...UNFINISHED
		pass

	def delNote(self):
		# ...UNFINISHED
		# use default value while using keyboard input
		noteList = self.__track.search(key, on, off)
		for noteID in noteList:
			self.__track.delNote(noteID)
		pass


	# Info Part

	def getTrackInfo(self, viewID):
		
		track = self.__file.getTrack(self.__trackDict[viewID])

		inst, vel = track.getInfo()

		trackInfo = {}
		trackInfo['Instrument'] = inst;
		trackInfo['Velocity'] = vel
		
		return trackInfo

	def getFileInfo(self):
		#...UNFINISHED
		pass


	# Protected

	def clearConfig(self):
		self.__track = None
		self.__cwPos = -1
		self.__cwViewID = -1
		self.__cwTrackID = -1
		self.__trackDict.clear()
		pass


	# Test Function

	def display1(self):
		# state = EDITABLE
		# for python 2.7.10
		print
		print '-'*5 + 'INFO' + '-'*5
		print '* Now playing Track {} *'.format(self.__cwTrackID)
		for viewID,trackID in self.__trackDict.items():
			trackInfo = self.getTrackInfo(viewID)
			s = 'Track {}, Inst {}:'.format(trackID, INSTRUMENT[trackInfo['Instrument']])
			track = self.__file.getTrack(trackID)
			for noteID in track.getNoteIDList():
				key, vel, on, off = track.getNote(noteID).getInfo()
				s += ' {}'.format(key)
			print s
		print '-'*14		

	def display2(self):
		# state = EMPTY
		# for python 2.7.10
		print
		print '-'*5 + 'INFO' +'-'*5
		print 'Oops! No file found.'
		print '-'*14

	def display(self):
		self.__switcher[self.__states]()

	def log(self, s):
		print
		s = '! Action: '+s
		print s

		




