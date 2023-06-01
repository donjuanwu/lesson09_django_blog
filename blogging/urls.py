"""
Assignment: 08 class-based view
Date: 5/28/23
File name: blogging/urls.py

Notes:
https://canvas.uw.edu/courses/1616579/pages/lesson-07-content?module_item_id=17606304
- In the Starting Django tutorial, you learned about Django urlconfs. We used our project urlconf to hook the Django admin into our project
  and we want to do the same thing for our new app.
- In general, an app that serves any sort of views should contain its own urlconf.
  The project urlconf should mainly include these where possible.

Date        Developer       Activities
5/28/23     Don D.          Refactor urls.py
                            - import Django generic views
                            - refactor urlpatterns to match Django generic url

"""

from django.urls import path
from blogging.views import PostListView, PostListViewDetail

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),  # post front pate
    path("posts/<int:pk>/", PostListViewDetail.as_view(), name="blog_detail"),  # kwargs
]
