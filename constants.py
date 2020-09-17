from flask import session, redirect
from functools import wraps
import pytz

# Timezone for the server
TIMEZONE_INDIA = pytz.timezone("Asia/Calcutta")

# Constants for sessions
USERNAME = "username"

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if USERNAME in session:
            return f(*args, **kwargs)
        else:
            return redirect("/login")
    return wrap

# Constants for Image upload
IMAGE_PROFILE_DIR = 'mysite/blogsite/static/images/profile/'
IMAGE_UPLOAD_DIR = 'mysite/blogsite/static/images/article/'

# Constants for Login error
LOGIN_FAIL_PASSWORD_EMPTY = "Password is Empty"
LOGIN_FAIL_INVALID_USER = "Username does not exist"
LOGIN_FAIL_INVALID_CRED = "Invalid user credentials"

# Constants for Signup error
SIGNUP_FAIL_INVALID_EMAIL = "Email Address is invalid"
SIGNUP_FAIL_EMAIL_EXISTS = "Email is already associated with another account"
SIGNUP_FAIL_USERNAME_EXISTS = "Username is already associated with another account"

#Constants for Flashing
ARTICLE_CREATED="Article create successfully"
ARTICLE_DELETED="Article deleted successfully"
ARTICLE_EDITTED="Article editted successfully"