"""
Assignment: 08 class-based view
Date: 5/28/23
File name: blogging/views.py
Purpose:
- convert the function-based views in your blogging app into class-based views.
Your work will be very similar to the work we did in the lesson content to create the polling class-based views, except
The blogging detail view doesn't accept POST requests, so there will be no need to create a `post` method in the blogging detail view.

Resources:
Introduction to class-based views
- https://docs.djangoproject.com/en/2.1/topics/class-based-views/intro/

Notes:
https://canvas.uw.edu/courses/1616579/pages/lesson-07-content?module_item_id=17606304
  In the Starting Django tutorial, you learned about Django urlconfs. We used our project urlconf to hook the Django admin into our project
  and we want to do the same thing for our new app. In general, an app that serves any sort of views should contain its own urlconf.
  The project urlconf should mainly include these where possible.

Date        Developer       Activities
5/28/23     Don D.          Remove def stub_view()
5/28/23     Don D.          import class-based views: ListView
                            use queryset to specify list of objects
                            - https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/#viewing-subsets-of-objects
"""

from django.shortcuts import Http404
from blogging.models import Post
from django.views.generic import ListView
from django.views.generic import DetailView


# Create your class-based views here.
class PostListView(ListView):
    """
    Assignment 08 Descriptions:
    - https://canvas.uw.edu/courses/1616579/assignments/8072498?module_item_id=17606313
    front page should continue to display only published posts and it should continue to display posts in reverse-chronological order.
    To accomplish this, you'll be providing a `queryset` class attribute in your list view instead of a `model` class attribute.
    """
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'


class PostListViewDetail(DetailView):
    """
    exclude all post with no published date
    """
    try:
        queryset = Post.objects.exclude(published_date__exact=None)
        template_name = 'blogging/detail.html'
    except Post.DoesNotExist:
        raise Http404
    # model = Post
    # template_name = 'blogging/detail.html'

