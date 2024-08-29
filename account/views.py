from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from account.forms import LoginForm,  SignUpForm
from account.models import Profile

User = get_user_model()

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "account/login.html"


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()

        Profile.objects.create(user=user)

        return super().form_valid(form)


class ProfileView(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "account/profile.html"

    def get_object(self):
        username = self.kwargs.get("username")
        user = get_user_model().objects.get(username=username)

        return Profile.objects.get(user=user)
    
class ProfileUpdate(UpdateView):
    model = Profile
    context_object_name = ""
    template_name = "account/profile_edit.html"