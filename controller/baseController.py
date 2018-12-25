from model.const import *

class baseController():
	def __init__(self):
		self._state = None
		self._observerList = []

	@property
	def state(self):
		return self._state
	
	def register(self, observer):
		self._observerList.append(observer)
		pass

	def notify(self):
		for observer in self._observerList:
			observer.update()
		pass

	def unregister(self, observer):
		if observer in self._observerList:
			self._observerList.pop(observer)
		pass