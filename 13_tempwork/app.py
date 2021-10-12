# The Fish Ducks: Lia Nelson, Tami Takada, Gavin McGinley
#SoftDev
#k13 -- Using templates with flask to generate easily customizable web pages
#2021-10-11

from flask import Flask, render_template
import csv
import random

#reads froms csv into a dictionary, and generates a dictionary including an "other" category, calculated from the csv data
def read_occupations(filename: str) -> dict:
    occupations = {}
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)

        next(reader)

        for index, row in enumerate(reader):
            job_class = row[0]
            percentage = row[1]
            occupations[job_class] = float(percentage)

    total_percentage = occupations["Total"]
    occupations["Other"] = round(100 - total_percentage,1)
    del occupations["Total"]

    return occupations

#randomly picks a key and its data from a dictionary, with the percentages of the csv serving as weights for weighted randomization
def choose_from_dict(occupations: dict) -> str:
    job_classes = list(occupations.keys())
    percentages = list(occupations.values())

    choice = random.choices(job_classes, weights=percentages)[0]
    return choice


app = Flask(__name__)

#defines tablified webpage route, and feeds python data into template
@app.route("/occupyflaskst")
def get_occupations_page():
    collection = read_occupations("data/occupations.csv")
    tnpg="The Fish Ducks: Lia Nelson, Tami Takada, Gavin McGinley"
    return render_template(
        "tablified.html",
        header="Random Occupation",
        title="Random Occupation Generator",
        tnpg=tnpg,
        collection=collection,
        randomoc=choose_from_dict(collection)
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
