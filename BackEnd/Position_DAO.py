from Position import Position
import json 
import serial
import time
import re

class Position_DAO:
    def __init__(self):
        self.positions = []
        self.occupied = 0
        self.free = 32
        self.reserverd=0
        self.can_open=True

    #Function to create a new parking position
    def new_position(self,id,user,state,alarm,attack):
        self.positions.append(Position(id,user,state,alarm,attack))
        return True
    
    def set_parking_free_by_reserved(self,id,user):
        for position in self.positions:
            if position.user==user:
                position.user=-1
                position.state="free"
                self.reserverd-=1
                self.free+=1
                print("Parqueo Reservado por el usuario "+str(user)+" Libre nuevamente. ")
                return True

    #Set free the position, but verify if the user has the alarm active.
    def set_parking_free(self,id,user):
        for position in self.positions:
            if position.user==user:
                if position.alarm=="on":
                    position.attack="on"
                    self.can_open=False
                else:
                    position.state="free"
                    self.occupied-=1
                    self.free+=1
                    position.user=-1
                    position.attack="off"



    
    def set_parking_reserved(self,id,user):
        for position in self.positions:
            if position.id==id:
                if position.state=="free":
                    position.user=user
                    position.state="reserved"
                    self.reserverd+=1
                    self.free-=1
                    print("Parqueo "+str(id)+" reservado por el usuario: "+str(user))
                    return True
                else:
                    return False
    
    def set_parking_occupied(self,id,user):
        for position in self.positions:
            if position.id==id:
                position.user=user
                self.occupied+=1
                self.free-=1
                print("Parqueo "+str(id)+" ocupado por el usuario: "+str(user))
                return True

    def verify_parking_change_in_proteus(self,id):
        for position in self.positions:
            if position.id==id:
                if position.state=="free":
                    position.state="occupied"
                    self.occupied+=1
                    self.free-=1
                    print("Parqueo "+str(id)+" ocupado ")
                    return True

                


    def set_parking_occupied_by_reserved(self,id,user):
        for position in self.positions:
            if position.user==user:
                if position.state=="reserved" and position.user==user:
                    position.state="occupied"
                    self.occupied+=1
                    self.reserverd-=1
                    print("Parqueo reservado "+str(position.id)+" ocupado por el usuario: "+str(user))
                    return True
                else:
                    return False
    
    def return_parking_stats(self):
        return {"occupied":self.occupied,
                "reserved":self.reserverd,
                "free":self.free,
                }
    def return_alarm_analytics(self,user):
        for position in self.positions:
            if position.user==user:
                return {"parking":position.id,
                    "alarm":position.alarm,
                    "attack":position.attack,
                    }
        return{
            "error":"true",
        }
    
    def turn_off_the_alarm(self,user):
        for position in self.positions:
            if position.user==user:
                position.alarm="off"
                return True
    
    def turn_on_the_alarm(self,user):
        for position in self.positions:
            if position.user==user:
                position.alarm="on"
                return True

    def return_level_one(self):
        return json.dumps([Position.dump() for Position in self.positions if Position.id <=16]) 
    def return_level_two(self):
        return json.dumps([Position.dump() for Position in self.positions if Position.id >=17]) 

    def return_all_reserveds(self):
        final_list=[]
        for position in self.positions:
            if position.state=="reserved":
                final_list.append(position.id)
        return final_list
                



