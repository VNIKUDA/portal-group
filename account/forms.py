from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"


class SignUpForm(UserCreationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"