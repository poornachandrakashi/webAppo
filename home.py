from flask import Blueprint, render_template
from blogsite.tables import Articles

home = Blueprint("home", __name__)

@home.route("/", methods = ["GET"])
def homepage():
    # article = Articles.query.all()
    return render_template('home.html')