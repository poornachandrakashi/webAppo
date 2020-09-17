from flask import Blueprint, render_template
from blogsite.constants import is_logged_in
from blogsite.tables import Articles

articles = Blueprint("articles", __name__)

@articles.route("/articles")
@is_logged_in
def articles_function():
    article = Articles.query.all()

    return render_template("articles.html", article = article )
    # return article