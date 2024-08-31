from django.shortcuts import render
from .models import Announcement

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'eventsss/eventsss_list.html', {'eventsss': announcements})