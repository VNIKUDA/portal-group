from django.urls import path
from . import views

urlpatterns = [
    path('eventsss/', views.announcement_list, name='eventsss_list'),
]