

mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black', 'orange']

def color_function(name):
    lst = []
    for i in color_list:
        msg = '{0} {1} {2}'.format(name, mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name!')
        elif name == 'Sally':
            print('Sally, you may not use this software.')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


get_name()

#practice function

def challengeFunction():
    if 3 > 2 or 8 < 5:
        print('Hello from a function!')
    else:
        print("didn't work!")

challengeFunction()

#practicing parameters

def nameFunction(fname, lname,):
    print(fname + ' ' + lname + ' likes fruit')

nameFunction('Joe', 'Buirgess',)

#practicing parameters w/ '*'
def fruitsFunction(*fruits):
    print('My favorite fruit is ' + fruits[1])

fruitsFunction('apple', 'orange', 'banana', 'peach')


#lambda function example

def multiply(i):
    return i * i;

y = lambda x: x * x * x

print(y(4))
print(multiply(3))

def getSum(num1, num2):
    answer = num1 + num2
    print('The answer is {}.'.format(answer))

myAdd = getSum

