"""
Assignment: 07 Activity
Date: 5/15/23
File name: blogging/models.py
Purpose:
- file which holds configuration for your project, more soon


Date        Developer       Activities
5/18/23     Don D.          Continue to use Django-Blog from Lesson 06 as Lesson 07 Activity

"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    URL: https://canvas.uw.edu/courses/1616579/pages/lesson-07-content?module_item_id=17606304
    definition: categorizing post
    """
    # attributes of class Category
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories') # many posts to a table or many
    # tables to a post

    def __str__(self):
        """
        need to add this method in order to pass blogging/tests.py
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Categories' # update category to categories another way to rename category


