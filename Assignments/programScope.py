

name = "Python" #Considered global because it's not in any specific block of code

def getName():
    name ="C#" #local to the getName() function, chagnes the previous variable 'name' to C#,
    print("I am coding with {}".format(name))

getName()
