"""
Assignment: Lesson 08 Activity Class-Based View
Date: 5/26/23
File name: polling/urls.py
Purpose:
- tell Django how to pick an appropriate view to service a request, based on teh path of that request

Date        Developer       Activities
5/15/23     Don D            Update the routing for polling/templates/polling/list.html & ./././detail.html
                             path('polling/', include('polling.urls')),
5/25/23     Don D.           class based views
"""

from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path('', PollListView().as_view(), name="poll_index"),
    path('polls/<int:pk>/', PollDetailView.as_view(), name="poll_detail"),
]
