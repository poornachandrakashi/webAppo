from flask import Blueprint, render_template
from blogsite.constants import is_logged_in
from blogsite.tables import Directory


profiles = Blueprint("profiles", __name__)

@profiles.route("/profiles/<string:id>")
@is_logged_in
def profiles_function(id):

    info = Directory.query.filter_by(id = id).first()

    return render_template('profiles.html', info=info)