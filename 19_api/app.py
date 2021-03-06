# TNPG: Shyne Choi, Gavin McGinley
# SoftDev
# K19 -- A RESTful Journey Skyward / Rest APIs & Flask
# 2021-11-23
# time spent: .7

import requests
import json
#put your key here
key=""


from flask import Flask, render_template   #facilitate jinja templating

from flask import Flask
app = Flask(__name__)

@app.route("/")
def NASA_key():
    response = requests.get(key)
    data = json.loads(response.content) #more usable dict
    #then return the template with image and explanation
    return render_template("main.html", pic=data["url"], explanation=data["explanation"]);

if __name__ == "__main__":
    app.debug = True        # enable auto-reload upon code change
    app.run()
