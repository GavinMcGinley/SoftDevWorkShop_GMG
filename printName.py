import random
pd1 = ["Ivan", "Gavin", "Ishraq", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
pd2 = ["James", "Robert", "John", "Donald", "Steven", "Paul", "Andrew",  "Joshua", "Maria", "Nushi", "Mohammed", "Jose", "Muhammad", "Mohamed", "Wei", "Mohammad", "Ahmed", "Yan", "Ali", "Li", "Abdul", "Ana"]

def printName():
    if random.randint(0, 1)==0:
        print(randomStudent(pd1))
    else:
        print(randomStudent(pd2))
    
            
def randomStudent(periodList):
    return periodList[random.randint(0,len(periodList)-1)]

printName()
