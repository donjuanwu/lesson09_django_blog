"""
Assignment: lesson09_CI/CD
Date: 5/31/23
File name: tests.py
Purpose:
- file which holds tests for the polling app
"""
from blogging.models import Post
from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class PostTestCase(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

        # add this test method to the PostTestCase

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
