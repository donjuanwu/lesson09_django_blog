"""
Assignment: Lesson 07 Assignment
Date: 5/21/23
File name: blogging/admin.py
Purpose:
- to register models


Notes:
    class ModelAdmin
    - The ModelAdmin class is the representation of a model in the admin interface. Usually, these are stored in
    a file name admin.py in your application.
    - https://docs.djangoproject.com/en/2.1/ref/contrib/admin/



Date        Developer      Activities
5/18/23     Don D.         Continue working on Lesson 06 Django-blog as Lesson 07 activity
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from blogging.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    """
    add this class to represent in admin interface
    - https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#modeladmin-objects
    """
    # title = models.CharField(max_length=128)
    # text = models.TextField(blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_date = models.DateTimeField(auto_now=True)
    # modified_date = models.DateTimeField(auto_now=True)
    # published_date = models.DateTimeField(blank=True, null=True)
    # categories = models.ManyToManyField(Category, blank=True, related_name='categories')
    fields = ('title', 'text', 'author', 'created_date', 'modified_date', 'published_date', 'categories')


# Register your models here. These models will show up in the Django admin/url
# admin.site.register(Post)
admin.site.register(Category)  # register blogging/model's class Category

# added to represent in admin interface
admin.site.register(Post, PostAdmin)  # added to
# admin.site.register(Category, PostAdmin)  # added to
