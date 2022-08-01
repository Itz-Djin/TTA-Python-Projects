#Encapsulation Challenge
class Test:
    def __init__(self):
        self.foo = 11
        #protected variable
        self._bar = 23
        #private variable
        self.__baz = 42

    

t = Test()
#creating object using _bar
bar = t._bar
#below prints the same value by different means. the first is instatiating the variable as an object, the second uses the class to access the protected variable
print(bar)
print(t._bar)


