import sqlite3

with sqlite3.connect("test_database.db") as connection:
    #perform any SQL operations using connection here
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)

#tuple of tuples, the inner tuples supplies the information for a single comman in the Db    
peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

#inserts tuples values into the Db
c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
