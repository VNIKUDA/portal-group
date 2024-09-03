from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from forum.models import Thread, Post

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ["title"]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["message"]