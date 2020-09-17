from flask import Blueprint, request, render_template, session, flash, redirect
from blogsite import db
import datetime
from blogsite.constants import USERNAME, is_logged_in, TIMEZONE_INDIA
from blogsite.tables import Articles
from wtforms import Form,StringField,TextAreaField,validators

edit_article = Blueprint("edit_article", __name__)


@edit_article.route("/edit_article/<string:id>", methods = ["GET", "POST"])
@is_logged_in
def edit_article_function(id):

    author = session[USERNAME]


    form=ArticleForm(request.form)
    articles = Articles.query.filter_by(id=id).first()

    if not articles.author == author:
        return redirect('/dashboard')

    if request.method == "GET":
        form.title.data = articles.title
        form.body.data = articles.body


    if request.method=='POST' and form.validate():

        articles = Articles.query.filter_by(id=id).first()

        articles.title = form.title.data
        articles.body = form.body.data
        articles.create_date = datetime.datetime.now(TIMEZONE_INDIA)

        # .update(dict(email='my_new_email@example.com')))
        print(id)
        print(articles.title)
        print(articles.body)
        print(articles.create_date)

        db.session.commit()

        flash('Article Edited','Success')

        return redirect('/dashboard')
    return render_template('edit_article.html',form=form)

#Article validation
class ArticleForm(Form):
    title = StringField('title', [validators.Length(min=1, max=2000)])
    body = TextAreaField('body', render_kw={'rows':20})

