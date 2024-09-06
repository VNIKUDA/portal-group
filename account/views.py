from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth import views as auth_views
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from account.forms import LoginForm,  SignUpForm
from account.models import Profile
from account.mixins import UserIsOwner

User = get_user_model()

@method_decorator(login_not_required, name="dispatch")
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "account/login.html"


@method_decorator(login_not_required, name="dispatch")
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


class ProfileUpdate(UserIsOwner, UpdateView):
    model = Profile
    fields = ["avatar", "bio"]
    context_object_name = "profile"
    template_name = "account/profile_edit.html"

    def get_object(self):
        username = self.kwargs.get("username")
        user = get_user_model().objects.get(username=username)

        return Profile.objects.get(user=user)
    
    def get_success_url(self) -> str:
        return reverse_lazy("account:profile", kwargs={"username": self.get_object().user.username})