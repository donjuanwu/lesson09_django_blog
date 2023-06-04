"""
Assignment: lesson09 assignment
Date: 6/4/23
File name: mysite/views.py
purpose:
- views for user to get authorization from Github

Notes:
    By default Django will look within an app for the templates folder but to keep
     things simple we can create a project-level templates folder and tell Django to look there, rather than in an app.

Resources:
Homepage - https://learndjango.com/tutorials/django-allauth-tutorial

Date        Developer       Activities
6/4/23      Don D.          Created views

"""


from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"