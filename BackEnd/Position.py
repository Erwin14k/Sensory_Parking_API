class Position:
    def __init__(self,id,user,state,alarm,attack):
        self.id = id 
        self.user = user
        self.state = state
        self.alarm=alarm
        self.attack=attack

    def dump(self):
        return {
            self.id: self.state,
        }