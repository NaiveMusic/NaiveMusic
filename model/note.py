
class Note():
    def __init__(self, key, vel, on, off):
        self.setAll(key, vel, on, off)

    def getInfo(self):
        '''Return note key, velocity, start time and stop time'''
        return self.__key, self.__vel, self.__on, self.__off

    def setKey(self, key):
        if key not in KEY_RANGE:
            raise ValueError('Key must be int within 0~127')
        self.__key = key

    def setVel(self, vel):
        if vel not in VEL_RANGE:
            raise ValueError('Velocity must be int within 0~127')
        self.__vel = vel

    def setOn(self, on):
        if not isinstance(on, int) or on < 0:
            raise ValueError('Note start time must be int no less than 0')
        self.__on = on

    def setOff(self, off):
        if not isinstance(off, int) or off < 0:
            raise ValueError('Note stop time must be int no less than 0')
        self.__off = off

    def setAll(self, key, vel, on, off):
        if key != None: self.setKey(key)
        if vel != None: self.setVel(vel)
        if on != None: self.setOn(on)
        if off != None: self.setOff(off)
