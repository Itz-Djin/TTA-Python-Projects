#Encapsulation Challenge
class Test:
    def __init__(self):
        self.foo = 11
        #protected variable
        self._bar = 23
        #private variable
        self.__baz = 42

    def getPrivate(self):
        print(self.__baz)

    def setPrivate(self, private):
        self.__baz = private

    
#instantiates the class as t variable
t = Test()
#creating object using _bar
bar = t._bar
#below prints the same value by different means. the first is instatiating the variable as an object, the second uses the class to access the protected variable
print(bar)
print(t._bar)

# as shown above it is easy to access a protected variable, there is a few more steps to access the private variable
#allows us to access our private variable by defined function
t.getPrivate()
#changes the private variable to a new value
t.setPrivate(9)
#obtains new value of private variable
t.getPrivate()
'''
this wont retrieve the private variable, instead it states there is no variable assigned. 
in order to access the private variable, look at above steps.
t.__baz
'''

