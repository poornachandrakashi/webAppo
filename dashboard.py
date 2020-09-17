from flask import Blueprint, render_template, session
from blogsite.constants import is_logged_in, USERNAME
from blogsite.tables import Articles

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
@is_logged_in
def dashboard_function():

    username = session[USERNAME]

    articles = Articles.query.filter_by(author = username)

    return render_template("dashboard.html", articles = articles )