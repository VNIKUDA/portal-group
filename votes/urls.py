from django.urls import path
from votes import views

urlpatterns = [
    path("", views.VoteHomeView.as_view(), name="home"),
    path("<int:pk>/", views.VoteDetailView.as_view(), name="vote-detail"),
    path("<int:pk>/complete", views.VoteCompleteView.as_view(), name="vote-complete")
]

app_name = "votes"