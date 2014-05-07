from random import *


#from pylab import *


# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    for _ in range(CURRENTRABBITPOP):
		new_rabbit_prob = 1.0 - (CURRENTRABBITPOP/float(MAXRABBITPOP))
		if new_rabbit_prob > random():
			if CURRENTRABBITPOP < MAXRABBITPOP:
				CURRENTRABBITPOP += 1


            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    for _ in range(CURRENTFOXPOP):
		eat_prob = CURRENTRABBITPOP/float(MAXRABBITPOP)
		if eat_prob > random():
			if CURRENTRABBITPOP > 10:
				CURRENTRABBITPOP -= 1

			if 1/3.0 > random():
				CURRENTFOXPOP += 1
		else:
			if 0.1 > random():
				CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_pops = [0]*numSteps
    fox_pops = [0]*numSteps

    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()

        rabbit_pops[i] = CURRENTRABBITPOP
        fox_pops[i] = CURRENTFOXPOP        

    return rabbit_pops, fox_pops



#r_pop, f_pop = runSimulation(200)

#plot(range(200), r_pop)
#plot(range(200), f_pop)
#title('Forrest animals')
#legend( ("Rabbits", "Foxes") )
#xlabel('Time')
#ylabel('Population')
#show()


#coeff = polyfit(range(len(r_pop)), r_pop, 2)
#plot(polyval(coeff, range(len(r_pop))))

#coeff = polyfit(range(len(f_pop)), f_pop, 2)
#plot(polyval(coeff, range(len(f_pop))))

#show()