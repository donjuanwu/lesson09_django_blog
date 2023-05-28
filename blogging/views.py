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


"""
from django.template import loader
from blogging.models import Post, Category
from django.shortcuts import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
def stub_view(request, *args, **kwargs):
    """
    a view:
    - code that builds a page that you can see
    - can be defined as a callable that takes a request and returns a response.
    we'll use the 'stub view' we've created so we can concentrate on the url routing
    """
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs: \n"
        body += "\n".join(["\t%s: %s" % a for a in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")  # return body with mime type


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)  # create an instance from the blogging/models's Post
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html') # get a template from the loader
    context = {'posts': posts} # build a context
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
