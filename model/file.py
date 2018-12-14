from model.track import Track

class File():
    def __init__(self, bpm):
        self.tracks = {}
        self.curID = 0
        self.bpm = bpm

    def addTrack(self,inst,vel):
        self.tracks[self.curID] = Track(inst, vel)
        trackID = self.curID
        self.curID += 1
        return trackID

    def delTrack(self,trackID):
        poped = self.tracks.pop(trackID)
        del poped