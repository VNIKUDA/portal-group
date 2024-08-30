from django.urls import path
from account import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('<str:username>/edit/', views.ProfileUpdate.as_view(), name='profile-edit'),
]

app_name = "account"