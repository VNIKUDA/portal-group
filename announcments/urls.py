from django.urls import path
from . import views

urlpatterns = [
    path('announcments/', views.portfolio, name='announcments'),
]