from django.urls import path
from forum import views

urlpatterns = [
    path('', views.ForumHomeView.as_view(), name='home'),
    path('search/', views.ThreadSearchView.as_view(), name="search"),
    path('thread/create/', views.ThreadCreateView.as_view(), name='thread-create'),
    path('thread/<int:pk>/', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('thread/<int:pk>/create-post/', views.PostCreateView.as_view(), name='post-create'),
]

app_name = "forum"