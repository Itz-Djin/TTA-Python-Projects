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

# create example tuple
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

