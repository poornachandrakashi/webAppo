from flask import Blueprint, request, session, render_template, redirect
# from blogsite import bcrypt
from blogsite.tables import Directory

from blogsite.constants import USERNAME
from blogsite.constants import LOGIN_FAIL_INVALID_USER
from blogsite.constants import LOGIN_FAIL_INVALID_CRED
from blogsite.constants import LOGIN_FAIL_PASSWORD_EMPTY

login = Blueprint('login',__name__)

@login.route("/login", methods = [ "GET" ,"POST"])
def login_function():

    if USERNAME in session:
        return redirect("/")

    """
    Constants :
    USERNAME = "username"
    LOGIN_FAIL_PASSWORD_EMPTY = "Password is Empty"
    LOGIN_FAIL_INVALID_USER = "Username does not exist"
    LOGIN_FAIL_INVALID_CRED = "Invalid user credentials"

    """

    if request.method=='POST':
        #Geeting the form field
        username_candidate = request.form.get('username')
        password_candidate=request.form.get('password')

        #Get user by username and password
        user_data = Directory.query.filter_by(username = username_candidate).first()

        if user_data is None:
            return render_template("login.html", error = LOGIN_FAIL_INVALID_USER)

        if password_candidate == "":
            return render_template("login.html", error = LOGIN_FAIL_PASSWORD_EMPTY)

        # result = bcrypt.check_password_hash(user_data.password, password_candidate)
        # print(result)
        print(user_data.password)
        print(password_candidate)


        # if result:
        if user_data.password==password_candidate:
            # Edu add madde
            # session['logged_in'] = True
            session[USERNAME] = user_data.username

            # return redirect("/home")
            return redirect("/")

        else:
            return render_template("login.html", error = LOGIN_FAIL_INVALID_CRED)


    return render_template('login.html')