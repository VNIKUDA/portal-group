from django.urls import path
from account.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
]

app_name = "account"