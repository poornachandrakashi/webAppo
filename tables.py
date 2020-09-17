from blogsite import db,app
from blogsite.constants import TIMEZONE_INDIA
import datetime

class Directory(db.Model):
    __tablename__ = "directory"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    family = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    GENDER = db.Column(db.String)
    PROFESSION = db.Column(db.String)
    father = db.Column(db.String)
    mother = db.Column(db.String)
    gotra = db.Column(db.String)
    marraige = db.Column(db.String)
    children = db.Column(db.Integer)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    dob = db.Column(db.Date)
    profile_image = db.Column(db.String)


"""
desc directory;

id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| name       | varchar(100) | YES  |     | NULL    |                |
| family     | varchar(100) | YES  |     | NULL    |                |
| email      | varchar(100) | YES  |     | NULL    |                |
| username   | varchar(30)  | YES  |     | NULL    |                |
| password   | varchar(50)  | YES  |     | NULL    |                |
| GENDER     | varchar(10)  | YES  |     | NULL    |                |
| PROFESSION | varchar(20)  | YES  |     | NULL    |                |
| father     | varchar(100) | YES  |     | NULL    |                |
| mother     | varchar(100) | YES  |     | NULL    |                |
| gotra      | varchar(50)  | YES  |     | NULL    |                |
| marraige   | varchar(30)  | YES  |     | NULL    |                |
| children   | int(100)     | YES  |     | NULL    |                |
| phone      | varchar(30)  | YES  |     | NULL    |                |
| address    | varchar(400) | YES  |     | NULL    |                |
| dob        | date         | YES  |     | NULL    |                |
"""

class Articles(db.Model):
    __tablename__="articles"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    body = db.Column(db.String)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now(TIMEZONE_INDIA))
    image_name = db.Column(db.String)

db.init_app(app)

"""
mysql> desc articles;
+-------------+--------------+------+-----+-------------------+----------------+
| Field       | Type         | Null | Key | Default           | Extra          |
+-------------+--------------+------+-----+-------------------+----------------+
| id          | int(11)      | NO   | PRI | NULL              | auto_increment |
| title       | varchar(100) | YES  |     | NULL              |                |
| author      | varchar(50)  | YES  |     | NULL              |                |
| body        | text         | YES  |     | NULL              |                |
| create_date | timestamp    | YES  |     | CURRENT_TIMESTAMP |                |
| image_name  | varchar(50)  | YES  |     | NULL              |                |
+-------------+--------------+------+-----+-------------------+----------------+
6 rows in set (0.00 sec)
"""
