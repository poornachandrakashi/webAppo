from flask import Blueprint, flash, request, render_template, redirect
import os
import re
from blogsite import db
# from blogsite import bcrypt
from blogsite.tables import Directory
from blogsite.constants import SIGNUP_FAIL_INVALID_EMAIL
from blogsite.constants import SIGNUP_FAIL_EMAIL_EXISTS
from blogsite.constants import SIGNUP_FAIL_USERNAME_EXISTS
from blogsite.constants import IMAGE_PROFILE_DIR

register = Blueprint("register", __name__)

"""
CONSTANTS :

IMAGE_PROFILE_DIR = 'mysite/blogsite/static/images/profile/'

"""

@register.route("/register", methods = ["GET", "POST"])
def register_fun():
    if request.method=='POST':

        # Get values inserted by User
        name=request.form.get('name')
        family=request.form.get('fname')
        email=request.form.get('email')
        username=request.form.get('username')
        password=request.form.get('password')
        dob=request.form.get('dob')
        GENDER=request.form.get('gender')
        PROFESSION=request.form.get('profession')
        father=request.form.get('father')
        mother=request.form.get('mother')
        gotra=request.form.get('gotra')
        marraige=request.form.get('marraige')
        children=request.form.get('children')
        phone=request.form.get('phone')
        address=request.form.get('address')

        if not check_email_valid(email):
            return render_template("registration.html", error = SIGNUP_FAIL_INVALID_EMAIL)

        if not does_user_exist(email):
            return render_template("registration.html", error = SIGNUP_FAIL_EMAIL_EXISTS)

        if not does_user_exist(username):
            return render_template("registration.html", error = SIGNUP_FAIL_USERNAME_EXISTS)

        # Fetch and store image
        image = request.files['img']
        filename = username + ".jpg"
        newfilename = os.path.join(IMAGE_PROFILE_DIR, filename)
        image.save(newfilename)

        print(password)
        # hash_pw = bcrypt.generate_password_hash(password).decode('UTF-8')
        # print(hash_pw)
        new_user = Directory(username=username, password=password, dob = dob, family = family, GENDER = GENDER, PROFESSION = PROFESSION, email=email, phone=phone, children = children, marraige = marraige, gotra = gotra, name=name, address = address, father = father, mother = mother, profile_image = filename)

        db.session.add(new_user)
        db.session.commit()

        flash("Successfully registered","success")

        # return form.email.data
        return redirect('/login')
    return render_template('registration.html')

def check_email_valid(email):
    s = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    if s.match(email):
        return True
    else:
        return False

def check_phone_valid(phone):
    s = re.compile("^[+]?[0-9]{10,13}$")
    if s.match(phone):
        return True
    else:
        return False


def does_user_exist(email=None, username=None):
    if email is not None:
        # Email is given
        data = Directory.query.filter_by(email = email).first()
        return data is None

    if username is not None:
        # Username is given
        data = Directory.query.filter_by(username = username).first()
        return data is None
