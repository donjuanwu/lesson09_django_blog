"""
Assignment: lesson09_CI/CD
Date: 6/1/23
File name: mysite/heroku.py
purpose:
- deploy to heroku
- supersede mysite/settings.py

Notes:
    1. heroku.py only run when the project is deploy to heroku
    2. heroku by default will not persist data. Need to have a database in order to have persistent data


black usage for heroku (from terminal):
black mysite/heroku.py
git add mysite/heroku.py
git add Procfile
git commit -m "Getting ready for heroku."
git push origin continuous-deployment

Create environment variables in heroku
1. Create heroku
> heroku create
2. Set environment variable to use mysite.heroku
> heroku config:set DJANGO_SETTINGS_MODULE=mysite.heroku
3. Set secret password
> heroku config:set SECRET_KEY=NnUdYr28vxncCAuYyppNp33H
4. Create database
> heroku addons:create heroku-postgresql:hobby-dev
5. View environment variables
> heroku config
6. Push to heroku
> git push heroku main
7. Create Django superuser
> heroku run python manage.py createsuperuser
8. Open heroku
> heroku open

git add requirements.txt
git commit -m "Get ready for heroku deployment."
git push origin continuous-deployment

app name: lesson09continuous-deployment
heroku git url: https://git.heroku.com/lesson09continuous-deployment.git

git remote rm heroku
git remote add heroku https://git.heroku.com/lesson09continuous-deployment.git
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
