from django.contrib import admin

from .models import (
    Event,
    Location,
    GrandPrix
)

admin.site.register(Event)
admin.site.register(Location)
admin.site.register(GrandPrix)