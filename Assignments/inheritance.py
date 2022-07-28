#Created Electronics class
class Electronics:
    powered = ''
    model_number = 0
    components = ''
    bluetooth = True
#Created Screens subclass of Electronices with 2 specific attributes
class Screens(Electronics):
    size = 0
    shape = ''
#Created Speakers subclass of Electronics with 2 specific attributes
class Speakers(Electronics):
    decibals = 0
    variant = ''
    