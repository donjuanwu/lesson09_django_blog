"""
Assignment: 07 Activity
Date: 5/20/23
File name: blogging/urls.py

Notes:
https://canvas.uw.edu/courses/1616579/pages/lesson-07-content?module_item_id=17606304
- In the Starting Django tutorial, you learned about Django urlconfs. We used our project urlconf to hook the Django admin into our project
  and we want to do the same thing for our new app.
- In general, an app that serves any sort of views should contain its own urlconf.
  The project urlconf should mainly include these where possible.

"""

from django.urls import path
from blogging.views import stub_view, list_view, detail_view

# url pattern

urlpatterns = [
    path('', list_view, name="blog_index"),  # url for list page
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),  # kwargs
]
