class RectangularRoom(object):
    def __init__(self, width, height):      
        self.width = width
        self.height = height
        self.tiles = {}    
    def cleanTileAtPosition(self, pos):       
        self.tiles[math.floor(pos.getX()), math.floor(pos.getY())] = 'c'
    def isTileCleaned(self, m, n):       
        return (math.floor(m),math.floor(n)) in self.tiles    
    def getNumTiles(self):       
        return self.width * self.height
    def getNumCleanedTiles(self):        
        return len(self.tiles)
    def getRandomPosition(self):       
        return Position((random.uniform(0.0, self.width)),(random.uniform(0.0, self.height)))  
    def isPositionInRoom(self, pos):        
        return math.floor(pos.getX()) <= self.width -1 and \
               math.floor(pos.getX()) >= 0 and \
               math.floor(pos.getY()) <= self.height -1 and \
               math.floor(pos.getY()) >= 0
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