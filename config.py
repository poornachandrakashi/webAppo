import os

#sqlalchemy stuff
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS=False

#secret
SECRET_KEY = os.getenv("SECRET_KEY")
