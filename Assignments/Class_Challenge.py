#Class Challenge
class Computer:
    def __init__(self, GPU, CPU, M2Drive):
        self.GPU = GPU
        self.CPU = CPU
        self.M2Drive = M2Drive

    def myfunc(self):
        print("The GPU is a " + self.GPU)

computer1 = Computer("1660TI", "Ryzen", "970 EVO")

computer1.myfunc()

#Inheritance Challenge
class smallComputer(Computer):
    pass

microPuter = smallComputer("MiniTI", "MiniRyzen", "Mini EVO")
microPuter.myfunc()