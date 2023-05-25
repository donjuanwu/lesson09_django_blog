"""
Assignment: 06
Date: 5/15/23
File name: views.py
Purpose:
- file which holds views for the polling app

Date        Developer       Activities
5/23/23     Don D.          Class based views
                            - use class inheritance
"""

from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.detail import DetailView

class ListView:
    """
    camel case name convention
    class based view
    """

    def as_view(self):
        return self.get

    def get(self, request):
        model_list_name = self.model.__name__.lower() + '_list'
        context = {model_list_name: self.model.objects.all()}  # get a table into Django
        return render(request, self.template_name, context)


class PollListView(ListView):
    """
    inheritance ListView class
    """
    model = Poll
    template_name = 'polling/list.html'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polling/detail.html'

# Below are function based views, give you better control
# Create your views here.
def list_view(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)
