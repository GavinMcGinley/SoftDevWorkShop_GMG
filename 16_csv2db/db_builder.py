#Text Box -- Sadid Ethun, Aaron Contreras, Gavin McGinley
#SoftDev
#K15 -- Database Creation/SQLite -- Populated DB in python using sqlite
#2021-10-21

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="students.db"



db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
c.execute("CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER);")


with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader: # reader is a list of dictionaries with the first row used as the keys
      data.append((row['name'], row['age'], row['id'])) 
        

  # test SQL stmt in sqlite3 shell, save as string
  
c.executemany("INSERT INTO roster (name, age, id) VALUES(?,?,?);", data)


c.execute("CREATE TABLE class (code TEXT, mark INTEGER, id INTEGER);")

with open('courses.csv') as csvfile:
    reader2 = csv.DictReader(csvfile)
    data2 = []
    for row in reader2:
      data2.append((row['code'], row['mark'], row['id']))

c.executemany("INSERT INTO class (code, mark, id) VALUES(?,?,?);", data2)#take in an array of tuples


#==========================================================

db.commit() #save changes
db.close()  #close database



