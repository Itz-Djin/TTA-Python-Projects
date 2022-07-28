# Python Course Practicing

# Args(Short for "arguments") is a special syntax in Python written out as *args. 
# Used to pass in an undefined number of arguments to a function. 
# The * represents any n umber of arguments in tuple form. 
# Args allows you to add on to your current parameters even if you didn't have any defined

# Example
def myFun(*args):
    for arg in args:
        print(arg)

myFun('This is an example of args', 'string', 'and then an integer', 5)