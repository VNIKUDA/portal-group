from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"


class SignUpForm(UserCreationForm):
    usable_password = None
    
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None