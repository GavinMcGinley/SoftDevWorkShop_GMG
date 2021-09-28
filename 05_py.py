#Gavin McGinley
#SoftDev
#k05 -- printName program amalgamation
#2021--09--27

#SUMMARY OF DISCUSSION
#The main thing we talked about was organizing data into a dictionary. One of our groupmates read in the names from a
# outside file, so that was a big difference in our initial approaches.
#Discoveries
#Mainly we just had to refresh our knowledge of how python dictionaries work.
#No questions or comments.

import random
#statistically most common names
pd1 = ["Ivan", "Gavin", "Ishraq", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
pd2 = ["James", "Robert", "John", "Donald", "Steven", "Paul", "Andrew",  "Joshua", "Maria", "Nushi", "Mohammed", "Jose", "Muhammad", "Mohamed", "Wei", "Mohammad", "Ahmed", "Yan", "Ali", "Li", "Abdul", "Ana"]
#puts lists into dictionary
KREWES= {'p1': pd1, 'p2':pd2}
#gets period list as argument and runs random student
def printName(x):
    p=str(x)
    p="p"+p
    if p!="p1" and p!="p2":
        print("not a valid softdev period")
    k=randomStudent(KREWES[p])
    print(k)
    
#retrieves random name from period list
def randomStudent(periodList):
    return periodList[random.randint(0,len(periodList)-1)]

printName(1)
