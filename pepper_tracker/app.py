"""
Pepper app
"""

from flask import Flask, render_template
from data.plants import plants
app = Flask(__name__)


def calc_germination(seeds, germinated) -> int:
    """_summary_

    Args:
        seeds (_type_): _description_
        germinated (_type_): _description_

    Returns:
        _type_: _description_
    """
    return round((germinated / seeds) * 100, 2) if seeds > 0 else 0

@app.route('/')
def index() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    # Calculate totals for each stage
    totals = {
        "seeds": sum(plant["seeds"] for plant in plants),
        "germinated": sum(plant["germinated"] for plant in plants),
        "seedlings": sum(plant["seedlings"] for plant in plants),
        "hardening": sum(plant["hardening"] for plant in plants),
        "plants": sum(plant["plants"] for plant in plants)
    }
    totals["germination_percentage"] = round((totals["germinated"] / totals["seeds"]) * 100, 2) if totals["seeds"] > 0 else 0

    # Add individual germination percentage to each plant record
    for plant in plants:
        plant["germination_percentage"] = calc_germination(plant["seeds"], plant["germinated"])
    return render_template("index.html", plants=plants, totals=totals)


if __name__ == '__main__':
    app.run(debug=True)
    