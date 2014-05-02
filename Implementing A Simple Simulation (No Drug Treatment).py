class SimpleVirus(object):
	"""
	Representation of a simple virus (does not model drug effects/resistance).
	"""

	def __init__(self, maxBirthProb, clearProb):
		"""
		Initialize a SimpleVirus instance, saves all parameters as attributes
		of the instance.
		maxBirthProb: Maximum reproduction probability (a float between 0-1)				
		clearProb: Maximum clearance probability (a float between 0-1).
		"""
		# TODO
		self.maxBirthProb = maxBirthProb
		self.clearProb = clearProb

	def doesClear(self):
		"""
		Stochastically determines whether this virus is cleared from the
		patient's body at a time step. 
		
		returns: Using a random number generator (random.random()), this method
		returns True with probability self.clearProb and otherwise returns
		False.
		"""
		# TODO
		if random.random() <= self.clearProb:
			return True
		else:
			return False

	def reproduce(self, popDensity):
		"""
		Stochastically determines whether this virus particle reproduces at a
		time step. Called by the update() method in the SimplePatient and
		Patient classes. The virus particle reproduces with probability
		self.maxBirthProb * (1 - popDensity).
		
		If this virus particle reproduces, then reproduce() creates and returns
		the instance of the offspring SimpleVirus (which has the same
		maxBirthProb and clearProb values as its parent).		 
		
		popDensity: the population density (a float), defined as the current
		virus population divided by the maximum population.		 
		
		returns: a new instance of the SimpleVirus class representing the
		offspring of this virus particle. The child should have the same
		maxBirthProb and clearProb values as this virus. Raises a
		NoChildException if this virus particle does not reproduce.			   
		"""
		# TODO
		if random.random() <= ( self.maxBirthProb * ( 1 - popDensity ) ):
			# print "virus reproduces"
			return SimpleVirus( self.maxBirthProb, self.clearProb )
		else:
			raise NoChildException('In reproduce()')


class Patient(object):
	"""
	Representation of a simplified patient. The patient does not take any drugs
	and his/her virus populations have no drug resistance.
	"""

	def __init__(self, viruses, maxPop):
		"""
		Initialization function, saves the viruses and maxPop parameters as
		attributes.
		
		viruses: the list representing the virus population (a list of
		SimpleVirus instances)
		
		maxPop: the  maximum virus population for this patient (an integer)
		"""
		# TODO
		self.viruses = viruses
		self.maxPop = maxPop

	def getTotalPop(self):
		"""
		Gets the current total virus population. 

		returns: The total virus population (an integer)
		"""
		# TODO		
		return len( self.viruses )

	def update(self):
		"""
		Update the state of the virus population in this patient for a single
		time step. update() should execute the following steps in this order:

		- Determine whether each virus particle survives and updates the list
		  of virus particles accordingly.

		- The current population density is calculated. This population density
		  value is used until the next call to update() 

		- Determine whether each virus particle should reproduce and add
		  offspring virus particles to the list of viruses in this patient.					

		returns: the total virus population at the end of the update (an
		integer)
		"""
		# TODO
		# Determine whether each virus particle survives and updates the 
		# list of virus particles accordingly.
		newViruses = []
		for index, virus in reversed( list( enumerate( self.viruses ) ) ):
			if virus.doesClear():
				# print "Virus clears"
				# pop virus from viruses list
				self.viruses.pop( index )
			else:
				popDensity = self.getTotalPop()/float(self.maxPop)
				try:
					# determine if surving virus reproduces
					# append any offspring to new virus list
					newViruses.append( virus.reproduce( popDensity ) )
				except NoChildException:
					continue
		# print "self.viruses =", self.viruses
		# print "newViruses =",  newViruses
		# add the new viruses to the list of patient viruses
		self.viruses = self.viruses + newViruses
		# print self.viruses

		return self.getTotalPop()