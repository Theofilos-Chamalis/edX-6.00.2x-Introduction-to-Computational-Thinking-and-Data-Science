# Enter your code for Robot and RandomWalkRobot in this box
# Enter your code for Robot and RandomWalkRobot in this box
class Robot(object):
    """
    Represents a robot cleaning a particular room.
 
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
 
    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
 
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 359)
        self.room = room
        self.speed = speed
        room.cleanTileAtPosition(self.position)
 
    def getRobotPosition(self):
        """
        Return the position of the robot.
 
        returns: a Position object giving the robot's position.
        """
        return self.position
   
    def getRobotDirection(self):
        """
        Return the direction of the robot.
 
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
 
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
 
        position: a Position object.
        """
        self.position = position
 
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
 
        direction: integer representing an angle in degrees
        """
        self.direction = direction
 
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
 
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
 
# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
 
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        if self.room.isPositionInRoom(self.position.getNewPosition(self.direction, self.speed)):
            self.position = self.position.getNewPosition(self.direction, self.speed)
            self.room.cleanTileAtPosition(self.position)
           
        self.direction = random.randint(0, 359)