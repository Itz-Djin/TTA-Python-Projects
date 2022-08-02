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

'''
one-time-use databases can also be created using the line of code below.
It allows the programmer to test code or play around with table structures,
the special name is :memory: for you database to create it in temporary RAM
'''
connection = sqlite3.connect(':memory:')

#to delete the People table we use the DROP TABLE statement: i.e: below
#the SQL command "IF EXISTS" checked if the table exists before trying to drop it, usually a good idea
#helps in avoiding errors that would occur if we happeend to try deleting a table that's
#already been deleted or never existed
c.execute("DROP TABLE IF EXISTS People")

'''
Once done with a db connection, we need to close() the connection.
Just like closing files, this pushes any changes out ot the database and frees up any
resources currently in memory that are no longer needed.
You close the db connection in the same way as you close files. 
'''
connection.close()

'''
When working with db connection, it's also a good idea to use the "with" keyword to simplify your
code (and your llife), similar hto how we have used 'with' to open files.
To run more than one line of SQL code at a time, there are a couple possible options.
A simple option is to use the executescript() method and give it a string that represents a full script;
although lines of SWL code will be seperated by semicolons, it is common to pass multi-line string for readabiltiy.
'''
with sqlite3.connect("test_database.db") as connection:
    #perform any SQL operations using connection here
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)

'''
another way to execute many similar statements by using the executemany() method and supplying
a tuple of tuples where each inner tuple suppplikkes the information for a single command.
For instance, if we have a lot of people's information to insert into our People table, we could
save this information in the following tuple of tuples
'''
peopleValues = (('Ron', 'Obious', 42), 'Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

'''
Then the following comman will insert all of these people at once (after preparing our connection and our People table)
by using the single line.
The question marks act as place-holders for the tuples in peopleValues.
This is called a parameterized statement.
The difference between parameterized and non-parameterized code is very similar to how
we can write out strings by concatenating many parts together versus using the strin format() method to insert
specific piecs into a string after creating it.
'''
c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)

