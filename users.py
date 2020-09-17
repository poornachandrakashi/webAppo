from flask import Blueprint, render_template
from blogsite.tables import Directory

users = Blueprint("users", __name__)

@users.route("/users")
def users_func():

    profiles = Directory.query.all()

    return render_template("fet_profile.html", profiles = profiles)