"""
Assignment: Lesson 08 Activity Class-Based View
Date: 5/26/23
File name: polling/models.py
Purpose:
- file which is where we will write our models for the polling app

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
        return self.title
