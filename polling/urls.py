
"""
Assignment: 06
Date: 5/15/23
File name: polling/urls.py
Purpose:
- tell Django how to pick an appropriate view to service a request, based on teh path of that request

Date        Developer       Activities
5/15/23     Don D            Update the routing for polling/templates/polling/list.html & ./././detail.html
                             path('polling/', include('polling.urls')),
"""

from django.urls import path
from polling.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="poll_index"),
    path('polls/<int:poll_id>/', detail_view, name="poll_detail"),
]
