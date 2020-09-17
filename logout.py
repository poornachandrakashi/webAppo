from flask import Blueprint, session, redirect
from blogsite.constants import USERNAME

logout = Blueprint('logout', __name__)

@logout.route("/logout")
def logout_function():

    if USERNAME in session:
        session.clear()

    return redirect("/")