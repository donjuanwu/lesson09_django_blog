"""
Assignment: 06
Date: 5/15/23
File name: admin.py
Purpose:
- file that you'll use to register polling models in the Django admin, more soon

Notes:
    Log into Django Adminstration
    > python manage.py runserver
    username: doncd
    pw: leyla2004

Date        Developer       Activities
5/15/23     Don D.          Register the Poll model in Django admin

"""

from django.contrib import admin
from polling.models import Poll

# Register your models here.
admin.site.register(Poll)