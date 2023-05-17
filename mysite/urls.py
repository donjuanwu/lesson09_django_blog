"""
Assignment: 06
Date: 5/15/23
File name: mysite/urls.py
Purpose:
- file which holds top-level URL configuration for your project, more soon


URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


Date        Developer       Activities
5/15/23     Don D            Update the routing for polling/templates/polling/list.html & ./././detail.html
                             path('polling/', include('polling.urls')),
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blogging.urls')), # general root will pass to blogging.urls
    path('polling/', include('polling.urls')),
    path('admin/', admin.site.urls), # This line routes all of our requests under the admin path to Django's admin module
]
