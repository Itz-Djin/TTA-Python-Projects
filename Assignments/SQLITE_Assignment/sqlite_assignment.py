#imports sqlite3 module giving access to methods and use of sqlite
import sqlite3

#instantiates connection object with connection to database, if db non-existent, it's created in set path
connection = sqlite3.connect("F:/The Tech Academy/TTA-Python-Projects/Assignments/SQLITE_Assignment/test_database.db")

#instantiates a cursor object, allowing operations on our db
c = connection.cursor()

c.execute("DROP TABLE IF EXISTS People")

#Creates table with 3 columns: text to store FirstName, LastName, and a integer to store Age
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

#Inserts data into new table
#Inserted a new row, with FirstName of Ron, LastNmae of Obious, and an Age equal to 42
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

#commits the changes made to the table verifying that we really meant this change to table's contents
connection.commit()

#creates a one-time-use database while testing code/playing around with table structures
#use special name :memory: for your database to create it in temporary RAM
connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")


#closes connection to database
connection.close()


