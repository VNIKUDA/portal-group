from django.views.generic import ListView, DetailView
from events.models import Event

class EventHomeView(ListView):
    model = Event
    context_object_name = "events"
    template_name = "events/home.html"

class EventDetailView(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "events/event_detail.html"
