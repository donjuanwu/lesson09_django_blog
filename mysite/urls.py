"""
Assignment: Lesson 09 Assignment
Date: 6/3/23
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


Notes:
https://canvas.uw.edu/courses/1616579/pages/lesson-07-content?module_item_id=17606304
  In the Starting Django tutorial, you learned about Django urlconfs. We used our project urlconf to hook the Django admin into our project
  and we want to do the same thing for our new app. In general, an app that serves any sort of views should contain its own urlconf.
  The project urlconf should mainly include these where possible.


Date        Developer       Activities
6/3/23      Don D.          Add  path('accounts/', include('allauth.urls'))
6/4/23                      Replace path("", include("blogging.urls")),  # blogging/urls
                                to path("blogging/", include("blogging.urls")),
                            Add path("", Home.as_view(), name="home")


"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from .views import Home

"""
- https://canvas.uw.edu/courses/1616579/pages/lesson-07-content?module_item_id=17606304
In order for our new urls to load, we’ll need to include them in our project urlconf. 
Open urls.py from the mysite project package and add this:

Hooking AdminSite instances into your URLconf
- https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#hooking-adminsite-to-urlconf
Example: 
urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
urlpatterns = [
    path("blogging/", include("blogging.urls")),  # blogging/urls
    path("polling/", include("polling.urls")),  # polling/urls
    path(
        "admin/", admin.site.urls
    ),  # This line routes all of our requests under the admin path to Django's admin
    # module
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("accounts/", include("allauth.urls")),
    path("", Home.as_view(), name="home"),  # new
]
