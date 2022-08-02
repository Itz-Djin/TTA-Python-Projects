#imports the sqlite3 module, allowing use of its classes and methods
import sqlite3

#establishes the connection and sets it to variable 'connection', if there is no "Test_database.db"
#it will be created and the connection will be established
connection = sqlite3.connect("C:/Choose_your_file_path_here_where_you_want/Test_database.db")

'''
communicates across the connection
this line instatiates a cursor object
A cursor is a control structure that enables operations on a database.
Our cursor object 'c' will let us execute commands on our SQL database 'Test_database'
and return the results
'''
c = connection.cursor()

'''
This line creates a new table named People and inserts three new columns into the table:
text for storing each person's FirstName, another text field to store the LastName
and an integer to store Age
'''
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

'''
Inserts data into the new table "People"
A new row with the FirstName of Ron, a LastName of Obvious, and an Age equal to 42.
the following line commits the change we made to the table to say that we really
meant to change the table's contents - otherwise our change wouldn't actually be saved.
'''
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()
