"""
Date: 5/16/23
File name: blogging/urls.py
"""

from django.urls import path
from blogging.views import stub_view

# url pattern
urlpatterns = [path('', stub_view, name="blog_index"),
               path('posts/<int:post_id>/', stub_view, name="blog_detail"),]