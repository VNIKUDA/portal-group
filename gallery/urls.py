from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    path('image/<int:id>/', views.image_detail, name='image_detail'),
]

