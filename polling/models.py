"""
Assignment: 06
Date: 5/15/23
File name: polling/models.py
Purpose:
- file which is where we will write our models for the polling app

Date        Developer       Activities
5/15/23     Don D           Add model
"""

from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
