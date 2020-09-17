from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#Config
app.config.from_pyfile("config.py")

#Set up sqlalchemy
db = SQLAlchemy(app)

#Bcrypt
bcrypt = Bcrypt(app)

from blogsite.login import login
from blogsite.home import home
from blogsite.register import register
from blogsite.logout import logout
from blogsite.dashboard import dashboard
from blogsite.profile import profile
from blogsite.add_article import add_article
from blogsite.articles import articles
from blogsite.article import article
from blogsite.delete import delete
from blogsite.edit_article import edit_article
from blogsite.users import users
from blogsite.profiles import profiles

app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(register)
app.register_blueprint(logout)
app.register_blueprint(dashboard)
app.register_blueprint(profile)
app.register_blueprint(add_article)
app.register_blueprint(articles)
app.register_blueprint(article)
app.register_blueprint(delete)
app.register_blueprint(edit_article)
app.register_blueprint(users)
app.register_blueprint(profiles)