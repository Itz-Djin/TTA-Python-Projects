import sqlite3
# setup variables for connection and cursor on sqlite3
# also creates the database filelist
conn = sqlite3.connect('filelist.db')
cur = conn.cursor()
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
for file in fileList:
    if file.endswith('.txt'):
# specifies while connected to specific db, to create table tbl_txtFiles if it non-existent and creates the primary key as well as columns utilizing string data type
        with conn:
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    File_Title TEXT, \
                    Extension TEXT \
                    )")
            cur.execute("INSERT INTO tbl_txtFiles(File_Title, Extension) VALUES (?, ?)" \
                        ("Hello", ".txt"))
            cur.execute("INSERT INTO tbl_txtFiles(File_Title, Extension) VALUES (?, ?)" \
                        ("World", ".txt"))
            conn.commit()
        conn.close()

print(file)



