# Polymorphism Challenge
# Created parent class person
class Employee:
    # Set a variable with a data type float
    raise_amt = 1.04
    # Used init method to initialize any instance of a Person
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
    # Created a method that will retrun the fullname of an instance of the class 'Person'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Created a method that will multipy the set float of the raise_amt variable to a Persons(s) pay
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    # Simple method we'll polymorph in child classes
    def action(self):
        print('All the employees work in building A')

# Created child class Developer
class Developer(Employee):
    raise_amt = 1.10
    # Initializes developers 
    def __init__(self, first, last, pay, prog_lang, monitors):
        #Grants access to parent methods/attributes and initiliazes here
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        self.monitors = monitors

    # Polymphorism on parent class method
    def action(self):
        print('Developers work in section 1 of building A')

#Created child class Manager
class Manager(Employee):
    #Initializes Manager objects with set attributes
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Creates a list of employees the manager oversees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # Allows manager to add/remove employees from list
    def add_emp(self,emp):
        if emp not in self.employees:
            #appends employee to the list if not already in the list
            self.employees.append(emp)

    # Allows manager to add/remove employees from list
    def remove_emp(self, emp):
        if emp in self.employees:
            #Removes employee to the list if not already in the list
            self.employees.append(emp)

    # Prints out list of employees that manager supervises
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    # Polymphorism on parent class method
    def action(self):
        print('Managers work in section 2 of building A')

# Instantiated 2 Developer Objects
dev_1 = Developer('Matt', 'Ziggler', 50000, 'Python', 1)
dev_2 = Developer('Sheila', 'Heinz', 60000, 'JavaScript', 3)

mgr_1 = Manager('Joe', 'Smith', 90000, [dev_1])

#print(issubclass(Manager, Employee))

#print(mgr_1.email)
#mgr_1.print_emps()

#print(dev_1.email)
#print(dev_1.monitors)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)