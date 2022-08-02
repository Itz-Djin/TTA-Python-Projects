#imports sqlite3 module
import sqlite3
from sqlite3 import Error


def create_connection():
    '''
        create a databse connection to a databse that resides
        in the memory
    '''

    conn = None;

    try:
        #establishes connection and creates database in RAM
        conn = sqlite3.connect(':memory:')
        #instantiates conn.cursor as c
        c = conn.cursor()

        #creates a tuple of tuples that will define the rows to our table
        fillRoster = (('Jean-Baptiste Zorg', 'Human', 122),('Korben Dallas', 'Meat Popsicle', 100),("Ak'not", 'Mangalore', -5))
        #creates table Roster with TEXT fields of Name, Species and an INT field of IQ
        c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
        #executemany allows us to use our fillRoster variable and use the data from it to fill our rows of the table 
        c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", fillRoster)

        #updates the row containing 'Korben Dalla'
        c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ('Human', 'Korben Dallas', 100))

        #Displays the names and IQs of everyone in the table who is classified as a human
        
        c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
        while True:
            man = c.fetchone()
            if man is None:
                break
            print(man)
        
        #Just a practice to test and come to a conclusion
        '''
        c.execute("SELECT Name, Species, IQ FROM Roster WHERE IQ >= 90")
        while True:
            man = c.fetchone()
            if man is None:
                break
            print(man)
        '''
        
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()






if __name__ == '__main__':
    create_connection()
