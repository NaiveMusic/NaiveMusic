from model.const import *

class BaseController():
	def __init__(self):
		#维护一个状态机
		self._state = STATE.DEFAULT
		#View中对象通过注册加入
		self._observerList = []

	@property
	def state(self):
		return self._state
	
	#每次View新建都需调用
	def register(self, observer):
		self._observerList.append(observer)
		pass

	#model部分更新后会调用
	def notify(self):
		for observer in self._observerList:
			observer.update()
		pass

	def unregister(self, observer):
		if observer in self._observerList:
			self._observerList.pop(observer)
		pass