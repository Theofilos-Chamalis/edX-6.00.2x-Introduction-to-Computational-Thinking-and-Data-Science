# Enter your definitions for the ResistantVirus and TreatedPatient classes in this box.
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
        
        
# Problem 4: b) TreatedPatient
class TreatedPatient(Patient):
    
    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.drugs =[]
 
    def addPrescription(self, newDrug):
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)
 
    def getPrescriptions(self):
        return self.drugs
 
    def getResistPop(self, drugResist):
        return len([v for v in self.viruses if all(v.isResistantTo(d) 
                                                   for d in drugResist)])
 
    def update(self):
        self.viruses = [v for v in self.viruses if not v.doesClear()]
        popDensity = len(self.viruses) / float(self.maxPop)
        for v in self.viruses[:]:
            try:
                self.viruses.append(v.reproduce(popDensity,
                                                self.getPrescriptions()))
            except NoChildException:
                pass
        return len(self.viruses)