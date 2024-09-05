from django.urls import path
from announcements import views

urlpatterns = [
    path('', views.AnnouncementsHome.as_view(), name='home'),
]

app_name = "announcements"