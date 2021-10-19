# Text Box -- Sadid Ethun, Aaron Contreras, Gavin McGinley
# SoftDev
# K15 -- Sessions Greetings / Flask Form and Error Handling
# 2021-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

user = 'sethun20'
pwd = 'hello'

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    if (request.args['username'] == user and request.args['password'] == pwd):
        return render_template( 'welcome.html', username=request.args['username'], method=request.method, password=request.args['password']) #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
