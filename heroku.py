"""
Assignment: lesson09_CI/CD
Date: 6/1/23
File name: heroku.py
purpose:
- deploy to heroku
- supersede mysite/settings.py

Notes:
    1. heroku.py only run when the project is deploy to heroku
    2. heroku by default will not persist data. Need to have a database in order to have persistent data


black usage for heroku (from terminal):
black heroku.py
git add heroku.py
git add Procfile
git commit -m "Getting ready for heroku."
git push origin continuous-deployment

create variables in heroku
heroku config:set DJANGO_SETTINGS_MODULE=mysite.heroku
heroku config:set SECRET_KEY=NnUdYr28vxncCAuYyppNp33H
heroku addons:create heroku-postgresql:hobby-dev
heroku config

git add requirements.txt
git commit -m "Get ready for heroku deployment."
git push origin continuous-deployment

"""

import os
import dj_database_url
from .settings import *

# heroku by default will not persist data. Need to have a database in order to have persistent data
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATES_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

MIDDLEWARE = ("whitenoise.middleware.WhiteNoiseMiddleware", *MIDDLEWARE)
