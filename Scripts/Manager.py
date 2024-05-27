#ÁllapotManager osztály
class ManagerClass:
    state = ""
    def __init__(self,state):
        self.state = state
    
    def GetState(self):
        return self.state
    
    def SetState(self,state):
        self.state = state