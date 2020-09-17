from flask import Blueprint, session, render_template
from blogsite.constants import is_logged_in, USERNAME
from blogsite.tables import Articles

article = Blueprint("article", __name__)

@article.route("/article/<string:id>")
@is_logged_in
def article_function(id):

    article = Articles.query.filter_by(id = id)

    return render_template('article.html', article=article)

