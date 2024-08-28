from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('thread/<int:id>/', views.thread_detail, name='thread_detail'),
    path('thread/new/', views.new_thread, name='new_thread'),
    path('post/new/<int:thread_id>/', views.new_post, name='new_post'),
]
