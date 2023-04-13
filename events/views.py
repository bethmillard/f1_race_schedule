from django.shortcuts import render, get_object_or_404

from .models import Event


def detail(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, "events/detail.html",
                  {"event": event})