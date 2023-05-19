"""
Assignment: 07 Activity
Date: 5/15/23
File name: blogging/admin.py
Purpose:
- to register models
Date        Developer      Activities
5/18/23     Don D.         Continue working on Lesson 06 Django-blog as Lesson 07 activity
"""

from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category) # register bloggin/model's class Category
