

# parent class
class Organism:
    # class attributes
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    #class methods
    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Bases: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg








if __name__ == "__main__":
