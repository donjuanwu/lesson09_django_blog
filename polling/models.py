"""
Assignment: Lesson 08 Activity Class-Based View
Date: 5/26/23
File name: polling/models.py
Purpose:
- file which is where we will write our models for the polling app

Resources:
How To Use the __str__() and __repr__() Methods in Python
- https://www.digitalocean.com/community/tutorials/python-str-repr-functions


Date        Developer       Activities
5/15/23     Don D           Add model
                            Notes:
                                 This new model represented a new table that I wanted stored in my database,
                                 so I had to migrate this new table into the existing database:
                                 1. python manage.py makemigrations
                                 2.
5/26/23     Don D.          Started lesson 08 class-based view
"""

from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        """
        - https://www.digitalocean.com/community/tutorials/python-str-repr-functions
        What is the __str __( self method in Python?
        The __str__() method returns a human-readable, or informal, string representation of an object.
        This method is called by the built-in print() , str() , and format() functions.

        """
        return self.title
