"""#Gavin McGinley
#SoftDev
#k06-- Reading csv/weighted randomness
#2021--09--28
#SUMMARY OF DISCUSSION
#We mainly worked together figuring out how to read in CSVs, and conceptualizing how to best do weighted randomness.
#Discoveries
#We mainly just figured out how reading in CSV files works.
#No questions or comments."""
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
            print(x)
            break
weighted()
