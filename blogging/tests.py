"""
Assignment: 07 Activity
Date: 5/20/23
File name: blogging/tests.py
Test usage:
> python manage.py test blogging


Date        Developer       Activities
5/18/23     Don D.          Update tests.py
                            Need to add a fixture into blogging/fixtures
                            - Luis sent out this file

"""

from blogging.models import Post, Category
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import utc
import datetime


# Create your tests here.
class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setup(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:  # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        """only display 5 published posts"""
        resp = self.client.get('/')  # come as part of test case
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        """
        - https://canvas.uw.edu/courses/1616579/pages/lesson-07-content?module_item_id=17606304
        Next, let’s add a view function for the detail view of a post. It will need to get the id of the post to show
        as an argument. Like the list view, it should only show published posts. Unlike the list view, it will need
        to return something if an unpublished post is requested.
        """
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get('/posts/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
