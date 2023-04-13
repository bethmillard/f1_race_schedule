from django.shortcuts import render

from events.models import Event

def welcome(request):
    return render(request, "website/welcome.html",
                  {"events":Event.objects.all()})