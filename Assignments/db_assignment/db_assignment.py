import sqlite3
# setup variables for connection and cursor on sqlite3
# also creates the database filelist
conn = sqlite3.connect('filelist.db')
cur = conn.cursor()

# specifies while connected to specific db, to create table tbl_txtFiles if it non-existent and creates the primary key as well as columns utilizing string data type
with conn:
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            File_Title TEXT, \
            Extension TEXT \
            )")
    conn.commit()
conn.close()

# list of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#iterates through the list of file names
for file in fileList:
    #if the file name ense with ".txt" then...
    if file.endswith('.txt'):
        #re-establishes 'conn' conecction to the database
        conn = sqlite3.connect('filelist.db')

        #opens connection to database and says what to do with said connection
        with conn:
            #executes the SQL statement to insert the 'file' variable into the table
            cur.execute("INSERT INTO tbl_txtFiles(File_Title) VALUES (?)" \
                (file,))

            #Displays the name of the file
            print(file)
            #commits changes to database
            conn.commit()
        #closes the connection to the database
        conn.close()

    