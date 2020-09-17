from flask import Blueprint, request, render_template, session, flash, redirect
from blogsite import db
from blogsite.constants import USERNAME, is_logged_in, IMAGE_UPLOAD_DIR
from blogsite.tables import Articles
from wtforms import Form,StringField,TextAreaField,validators
import os
import time

add_article = Blueprint("add_article", __name__)

@add_article.route("/add_article", methods = ["GET", "POST"])
@is_logged_in
def add_article_function():

    form=ArticleForm(request.form)

    if request.method=='POST' and form.validate():
        title = form.title.data
        body = form.body.data
        image = request.files['img']
        ts = time.gmtime()
        uploadtime = time.strftime("%Y%m%d%H%M%S", ts)
        filename = "image_" + uploadtime + ".jpg"
        newfilename = os.path.join(IMAGE_UPLOAD_DIR,filename)
        # app.logger.info("File to upload: ")
        # app.logger.info(filename)
        image.save(newfilename)

        new_article = Articles(author = session[USERNAME], body = body, title = title, image_name = filename)

        db.session.add(new_article)
        db.session.commit()

        flash('Article Created','Success')

        return redirect('/dashboard')
    return render_template('add_article.html',form=form)

#Article validation
class ArticleForm(Form):
    title = StringField('title', [validators.Length(min=1, max=2000)])
    body = TextAreaField('body', render_kw={'rows':20})

