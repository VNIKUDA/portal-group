from django.contrib import admin
from .models import Announcments

@admin.register(Announcments)
class AnnouncmentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')