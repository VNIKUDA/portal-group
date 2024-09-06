from django.views.generic import ListView
from announcements.models import Announcement

class AnnouncementsHomeView(ListView):
    queryset = list(reversed(Announcement.objects.all()))
    context_object_name = "announcements"
    template_name = "announcements/home.html"