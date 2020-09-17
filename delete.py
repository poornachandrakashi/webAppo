from flask import Blueprint, redirect, session, flash
from blogsite.constants import is_logged_in, USERNAME, IMAGE_UPLOAD_DIR
from blogsite.tables import Articles
from blogsite import db
import os

delete = Blueprint("delete", __name__)

@delete.route("/delete_article/<string:id>", methods = ["GET"])
@is_logged_in
def delete_function(id):

    article = Articles.query.filter_by(id = id).first()

    if not session[USERNAME] == article.author:
        return redirect("/dashboard")

    os.remove(os.path.join(IMAGE_UPLOAD_DIR, article.image_name))
    print(os.path.join(IMAGE_UPLOAD_DIR, article.image_name))
    db.session.delete(article)

    db.session.commit()

    flash("Article deleted successfully", "success")

    return redirect("/dashboard")
    # return article