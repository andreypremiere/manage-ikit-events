from django.contrib import admin
from .models import ListUniversity, Events


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_of_event', 'time_of_event')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'organizer')

admin.site.register(Events, EventsAdmin)