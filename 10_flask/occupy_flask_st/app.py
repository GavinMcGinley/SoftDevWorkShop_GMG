"""#Gavin McGinley
#SoftDev
#k10-- trying out flask
#2021--10--04
#SUMMARY OF DISCUSSION
We mainly just tried to get flask to work and pulled the required files from git"""
from flask import Flask
app = Flask(__name__) #create instance of class Flask

def weighted():
    import csv
    import random

    #Reads CSV into program as "reader"
    csv_file=open("occupations.csv")
    reader=csv.reader(csv_file)

    #skips first line
    next(reader)

    #Adds CSV info to dictionary
    wdict={}
    for row in reader:
        wdict[row[0]]=float(row[1])

    #Randomly generates number
    num=random.randint(1,998)
    total=0;

    #Likeliness of passing total is proportional to its percentage
    for x in wdict.keys():
        total=total+(wdict[x]*10)
        if total>=num:
            return(x)
            break

@app.route("/")       #assign fxn to route
def hello_world():
    tmpg="The Cool Dogs: Bobby, Craig, Fish, Ishraq Mahid, Ivan Mijacika, Gavin McGinley"

    q= "Chosen Occupation: " + weighted()

    q= tmpg +"\n"+q
    return q

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()



