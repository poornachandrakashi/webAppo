from flask import Blueprint, session, render_template
from blogsite.constants import is_logged_in, USERNAME
from blogsite.tables import Directory

profile = Blueprint("profile", __name__)

@profile.route("/profile")
@is_logged_in
def profile_function():

    user_data = Directory.query.filter_by(username = session[USERNAME]).first()

    print(user_data.profile_image)

    return render_template("profile.html", user_data = user_data)