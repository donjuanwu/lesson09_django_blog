"""
Date: 5/16/23
File name: blogging/views.py
"""

from django.shortcuts import render
from blogging.models import Post
from django.shortcuts import HttpResponse
from django.template import loader

# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs: \n"
        body += "\n".join(["\t%s: %s" % a for a in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    published = Post.objects.exclude(published_date_exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html')
    context = {'post': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")
