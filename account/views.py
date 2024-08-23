from django.shortcuts import render
from django.contrib.auth import views as auth_views
from account.forms import LoginForm

# Create your views here.
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "account/login.html"