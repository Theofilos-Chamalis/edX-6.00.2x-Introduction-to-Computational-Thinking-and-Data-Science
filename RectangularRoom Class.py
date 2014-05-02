# Enter your code for RectangularRoom in this box
class RectangularRoom(object):
    """
   A RectangularRoom represents a rectangular region containing clean or dirty
   tiles.
 
   A room has a width and a height and contains (width * height) tiles. At any
   particular time, each of these tiles is either clean or dirty.
   """
    def __init__(self, width, height):
        """
       Initializes a rectangular room with the specified width and height.
 
       Initially, no tiles in the room have been cleaned.
 
       width: an integer > 0
       height: an integer > 0
       """
        self.width = width
        self.height = height
        self.clean = []
   
    def cleanTileAtPosition(self, pos):
        """
       Mark the tile under the position POS as cleaned.
 
       Assumes that POS represents a valid position inside this room.
 
       pos: a Position
       """
        x = math.floor(pos.x)
        y = math.floor(pos.y)
        if (x, y) in self.clean:
            return self.clean
        else:
            self.clean.append((x,y))
            return self.clean
       
    def isTileCleaned(self, m, n):
        """
       Return True if the tile (m, n) has been cleaned.
 
       Assumes that (m, n) represents a valid tile inside the room.
 
       m: an integer
       n: an integer
       returns: True if (m, n) is cleaned, False otherwise
       """
        posX = math.floor(m)
        posY = math.floor(n)
        pos = (posX, posY)
 
        if pos in self.clean:
            return True
        else:
            return False
   
    def getNumTiles(self):
        """
       Return the total number of tiles in the room.
 
       returns: an integer
       """
        return self.width * self.height
       
 
    def getNumCleanedTiles(self):
        """
       Return the total number of clean tiles in the room.
 
       returns: an integer
       """
        return len(self.clean)
   
    def getRandomPosition(self):
        """
       Return a random position inside the room.
 
       returns: a Position object.
       """
        randX = random.choice(range(self.width))
        randY = random.choice(range(self.height))
        return Position(randX, randY)
 
    def isPositionInRoom(self, pos):
        """
       Return True if pos is inside the room.
 
       pos: a Position object.
       returns: True if pos is in the room, False otherwise.
       """
        if pos.x < self.width and pos.x >= 0:
            if pos.y < self.height and pos.y >= 0:
                return True
 
        else:
            return False