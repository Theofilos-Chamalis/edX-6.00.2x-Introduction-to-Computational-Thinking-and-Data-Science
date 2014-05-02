# Enter your code for runSimulation in this box.
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.
 
    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.
 
    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    trialsList = []
    
    # Run num_trials amount of tests
    for trial in range(num_trials):
    #### Create room
        room = RectangularRoom(width,height)
        botList = []
    #### Create bots and add them to the botList
        for n in range(num_robots):
            botList.append(robot_type(room,speed))
            #print botList
        #anim = ps7_visualize.RobotVisualization(num_robots, width, height)
        steps = 0
    #### While the room is not cleaned enough: Let all bots have another 'turn'
        while (1.0*room.getNumCleanedTiles()/room.getNumTiles()) <= min_coverage:
            #print room.getNumCleanedTiles()
            #print steps
            for bot in botList:
                #print bot
                #anim.update(room, bots)
                bot.updatePositionAndClean()
            steps += 1
    #### Add test to trialsList
        trialsList.append(steps)
        #anim.done()
    # return mean-value of all values in trialsList
    return float(sum(trialsList)) / len(trialsList)