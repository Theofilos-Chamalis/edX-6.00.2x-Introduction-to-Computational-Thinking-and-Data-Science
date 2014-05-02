# Enter your code for Robot (from the previous problem)
#  and StandardRobot in this box
class Robot(object):   
    def __init__(self, room, speed):        
        self.room = room
        self.speed = speed       
        self.direction =  random.randint(0,359) 
        self.position = room.getRandomPosition()
        self.room.cleanTileAtPosition(self.position) 
    def getRobotPosition(self):        
        return self.position    
    def getRobotDirection(self):        
        return self.direction
    def setRobotPosition(self, position):        
        self.position = position
    def setRobotDirection(self, direction):       
        self.direction = direction
    def updatePositionAndClean(self):        
        raise NotImplementedError # don't change this!
class StandardRobot(Robot):    
    def updatePositionAndClean(self):        
        pos = self.getRobotPosition()       
        newpos = pos.getNewPosition(self.getRobotDirection(), self.speed)
        if self.room.isPositionInRoom(newpos): 
            self.setRobotPosition(newpos)
            if not self.room.isTileCleaned(math.floor(newpos.getX()),math.floor(newpos.getY())):
                self.room.cleanTileAtPosition(newpos)                
        else:          
            self.setRobotDirection(random.randint(0,359))