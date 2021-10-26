#a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("discobandit.db") 

c = db.cursor() #facilitate db ops

#c.execute("CREATE TABLE roster(name TEXT,userid INTEGER);")
c.execute("INSERT INTO roster VALUES( 'tim',7);")
c.execute("INSERT INTO roster VALUES( 'jim',8);")
c.execute("SELECT * FROM roster;")
db.commit() #save changes
db.close()
