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


# Child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    # Method of Human class
    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg


# another child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on its target!"
        return msg

# another child class instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0 
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and mulitply into two seperate organisms!"
        return msg


if __name__ == "__main__":
    #Instantiate the "Human()" object
    human = Human()
    print(human.information())
    print(human.ingenuity())

    #Instantiate the "Dog()" object
    dog = Dog()
    print(dog.information())
    print(dog.bite())

    #Instantiate the "Bacterium()" object
    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())

