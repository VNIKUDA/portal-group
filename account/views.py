from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from account.forms import LoginForm, SignUpForm
from account.models import Profile

User = get_user_model()

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "account/login.html"

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


class ProfileView(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "account/profile.html"

    def get_object(self, queryset):
        username = self.kwargs.get("username")
        user = get_user_model().objects.get(username=username)

        return queryset.get(user=user)