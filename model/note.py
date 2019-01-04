from model.const import *


class Note():
    def __init__(self, key, vel, on, off):
        self.setAll(key, vel, on, off)

    @property
    def on(self):
        return self._on

    @property
    def off(self):
        return self._off

    @property
    def key(self):
        return self._key

    @property
    def vel(self):
        return self._vel

    def getInfo(self):
        '''Return note key, velocity, start time and stop time'''
        return self._key, self._vel, self._on, self._off

    def setKey(self, key):
        if key not in KEY_RANGE:
            raise ValueError('Key must be int within 0~127')
        self._key = key

    def setVel(self, vel):
        if vel not in VEL_RANGE:
            raise ValueError('Velocity must be int within 0~127')
        self._vel = vel

    def setOn(self, on):
        if not isinstance(on, int) or on < 0:
            raise ValueError('Note start time must be int no less than 0')
        self._on = on

    def setOff(self, off):
        if not isinstance(off, int) or off < 0:
            raise ValueError('Note stop time must be int no less than 0')
        self._off = off

    def setAll(self, key, vel, on, off):
        if key != None: self.setKey(key)
        if vel != None: self.setVel(vel)
        if on != None: self.setOn(on)
        if off != None: self.setOff(off)
