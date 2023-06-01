"""
Assignment: Lesson 07 Assignment
Date: 5/21/23
File name: blogging/admin.py
Purpose:
- Reversing the relationship between category and post from Lesson 06 assignment.
- Update: only add categories to post


References:
Django Admin Site
- https://docs.djangoproject.com/en/2.1/ref/contrib/admin
1. Discuss how to activate, use and customize Django's admin interface

ModelAdmin
- https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#modeladmin-objects
1. The ModelAdmin class is the representation of a model in the admin interface.
2. Usually, these are stored in a file name admin.py in your application.
3. The ModelAdmin is very flexible. It has several options for dealing with customizing the interface.
    All options are defined on the ModelAdmin subclass

ModelAdmin.inlines
- https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.inlines

ModelAdmin.list_display
- Set list_display to control which fields are displayed on the change list page of the admin
    Example:
    List_display = ('first_name', 'last_name')
ModelAdmin.exclude
-https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.exclude
This attribute, if given, should be a list of fieldnames to exclude from the form

InlineModelAdmin objects
- https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#inlinemodeladmin-objects
The admin interface has the ability to edit models on the same pae as a parent model.
These are called inlines.
    You can edit the books authored by an author on the author page.
    You add inlines to a model by specifying them in a ModelAdmin.inlines



Date        Developer      Activities
5/18/23     Don D.         Continue working on Lesson 06 Django-blog as Lesson 07 activity
5/24/23     Don D.         Edit blogging/admin.py with new classes in order to complete Lesson 07 Activity
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from blogging.models import Post, Category


class PostInline(admin.TabularInline):
    """
    InlineModelAdmin objects
     - https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#inlinemodeladmin-objects

     Django provides two subclasses of InlineModelAdmin and tye are:
     1. TabularInline
     2. StackedInLine
    """

    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    """
    InlineModelAdmin objects
    - https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#inlinemodeladmin-objects
    The admin interface has the ability to edit models on the same pae as a parent model.
    These are called inlines.
    You can edit the books authored by an author on the author page.
    You add inlines to a model by specifying them in a ModelAdmin.inlines
    """

    inlines = [
        PostInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    """
    ModelAdmin.list_display
    - set list_display to control which fields are displayed on the change list page of the admin
    exclude the 'posts' field from the form in your Category admin

    ModelAdmin.exclude
    - https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.exclude
    This attribute, if given, should be a list of field names to exclude from the form
    """

    list_display = (
        "name",
        "description",
    )  # in category display name and description fields
    exclude = ["posts"]  # list out the fields to exclude from the form


# Register your models here. These models will show up in the Django admin/url
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

"""
Below are original code before manipulating the admin interface to exclude post from category and include category for post
"""

# Register your models here. These models will show up in the Django admin/url
# admin.site.register(Post)
# admin.site.register(Category)  # register blogging/model's class Category
