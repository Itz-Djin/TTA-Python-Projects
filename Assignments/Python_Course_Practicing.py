# Python Course Practicing

# Args(Short for "arguments") is a special syntax in Python written out as *args. 
# Used to pass in an undefined number of arguments to a function. 
# The * represents any n umber of arguments in tuple form. 
# Args allows you to add on to your current parameters even if you didn't have any defined

# Example
def myFun(*args):
    for arg in args:
        print(arg)

myFun('This is an example of args', 'string', 'and then an integer', 5, 'You can add', 'as many arguments', 'up to the max limit')


# Kwargs (short for "keyword arguments") is also a special syntax, just like *args
# Written as **kwargs where the asterisks ** represent a key value pair
# Also used to pass in any number of undefined arguments into a function
# Acts as a dictionary, mapping out the value to its corresponding variable key
# The use of **args is another way of writing kwargs

# Example
def myKwargs(**kwargs):
    print("kwargs", kwargs)

myKwargs(first = '1', second = '2', third = '3')