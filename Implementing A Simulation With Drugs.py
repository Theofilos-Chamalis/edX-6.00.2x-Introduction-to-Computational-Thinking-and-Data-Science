# Enter your definition for the ResistantVirus class in this box.
# You'll enter your code for TreatedPatient on the next page.
class ResistantVirus(SimpleVirus):  
 
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.mutProb = mutProb
        self.resistances = resistances
 
    def isResistantTo(self, drug):
        return self.resistances.get(drug, False)
 
    def reproduce(self, popDensity, activeDrugs):
        if (all(self.isResistantTo(d) for d in activeDrugs) and
            random.random() <= self.getMaxBirthProb() * (1 - popDensity)):
            resistances = {k:v if random.random() > self.mutProb else not v
                           for k, v in self.resistances.items()}
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), 
                                  resistances, self.mutProb)
        raise NoChildException