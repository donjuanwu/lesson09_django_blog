#!/usr/bin/env python
import os
import sys

"""
Assignment: lesson09_CI/CD
Date: 5/31/23
File name: manage.py
Purpose:
- a management control script
- Django's command-line utility for administrative tasks

How it works:
The `django-admin` command that we used to create the project has sub-commands that allow you to:
- creating a new project or app
- running the development server
- executing tests
- entering a python interpreter
- entering a database shell session with your database
- much much more (run django-admin without an argument)

The `manage.py` script wraps this functionality in the context of your project: it communicates your project settings 
to `django-admin`.

The environment variable DJANGO_SETTINGS_MODULE is how the manage.py script knows about your project’s environment. 
Specifically, it knows that our project is named mysite. This is why you shouldn’t rename the mysite project package.

Notes:
After forking project must do the following
1. create database
> from terminal: python manage.py migrate
2. create super user
> from terminal: python manage.py createsuperuser
                 doncd
                 leyla2004
                 
black usage:
> pip install black
run autoformatter on blogging mysite and polling
> black --check blogging mysite polling

Django allauth-tutorial:  https://learndjango.com/tutorials/django-allauth-tutorial




Date        Developer           Activities
5/31/23     Don D.              Clone lesson08 assignment main branch and called it lesson09_django_blog
                                Need to recreate superuser on pycharm terminal
                                > python manage.py createsuperuser
                                name: doncd
                                pw: leyla2004
6/3/23      Don D.              Add addon #1: Social Signin/Login withGub
                                Heroku:
                                    Client ID: 40a9585681212df1a57a
                                    Secrets 7ec520b12f836f7df17bf16445a28d67c66d0957
6/4/23      Don D.              Local Test
                                    Client ID: 660649bc1e2b093d12f3
                                    Secrets: 05d26f04db10b8689c6bb2037d67184dec8b754c


"""


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
