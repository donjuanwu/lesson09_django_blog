"""
Assignment: Lesson 08 Activity Class-Based View
Date: 5/26/23
File name: polling/views.py
Purpose:
- file which holds views for the polling app

Date        Developer       Activities
5/23/23     Don D.          Class based views
                            - use class inheritance
5/26/23     Don D.          Started lesson 08 activity class-based view
                            Added:
                            - from django.views.generic.list import ListView
                            - from django.views.generic.detail import DetailView
"""

from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# class ListView:
#     """
#     camel case name convention
#     """
#
#     def as_view(self):
#         return self.get
#
#     def get(self, request):
#         model_list_name = self.model.__name__.lower() + '_list'  # poll_list goes into templates/polling/list.html
#         context = {model_list_name: self.model.objects.all()}  # get a table into Django
#         return render(request, self.template_name, context)
#
#     # Below are function based views, give you better control
#     # Create your views here.
#     def list_view(request):
#         context = {'polls': Poll.objects.all()}
#         return render(request, 'polling/list.html', context)
#
#     def detail_view(request, poll_id):
#         try:
#             poll = Poll.objects.get(pk=poll_id)
#         except Poll.DoesNotExist:
#             raise Http404
#
#         if request.method == "POST":
#             if request.POST.get("vote") == "Yes":
#                 poll.score += 1
#             else:
#                 poll.score -= 1
#             poll.save()
#
#         context = {'poll': poll}
#         return render(request, 'polling/detail.html', context)


"""
Begin: Lesson 08 class-based view 
"""


class PollListView(ListView):
    """
    inheritance ListView class
    class-based view
    """

    # specifying model = Poll is a shorthand for saying queryset = Poll.objects.all()
    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):
    """
    class-based view
    """

    # specifying model = Poll is a shorthand for saying queryset = Poll.objects.all()
    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        poll = self.get_object()  # polling_lists
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
        context = {"object": poll}
        return render(request, "polling/detail.html", context)
