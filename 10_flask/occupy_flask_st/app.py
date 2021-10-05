"""
Cool Dogs - Ishraq Mahid & Fish, Ivan Mijacika & Bob, and Gavin McGinley & Craig
SoftDev
k10 -- Flask Greatness -- Exploration of Flask framework -- We explored written code to understand flask and created our own code
2021 - 10 - 4
"""
from flask import Flask
from randomOcc06 import weighted
from randomOcc06 import generateListStr

app = Flask(__name__)  # create instance of class Flask
tnpg = "Cool Dogs - Ishraq Mahid & Fish, Ivan Mijacika & Bob, and Gavin McGinley & Craig"

@app.route("/")  # assign fxn to route

def hello_world():
    #This code does similar to what is done in v3, with the exception of dealing with cases where the file is imported somewhere else
    
    return tnpg + "<br>" + 'The selected occupation is: ' + weighted() + "<br>" + generateListStr()


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

