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

    def __init__(self, data: Mapping[str, Any] | None = ..., files: Mapping[str, File] | None = ..., auto_id: bool | str = ..., prefix: str | None = ..., initial: dict[str, Any] | None = ..., error_class: type[ErrorList] = ..., label_suffix: str | None = ..., empty_permitted: bool = ..., instance: Model | None = ..., use_required_attribute: bool | None = ..., renderer: Any = ...) -> None:
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance, use_required_attribute, renderer)

        self.fields["title"].widget.attrs['class'] = "form-control"


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["message"]

    def __init__(self, data: Mapping[str, Any] | None = ..., files: Mapping[str, File] | None = ..., auto_id: bool | str = ..., prefix: str | None = ..., initial: dict[str, Any] | None = ..., error_class: ErrorList = ..., label_suffix: str | None = ..., empty_permitted: bool = ..., instance: Model | None = ..., use_required_attribute: bool | None = ..., renderer: Any = ...) -> None:
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance, use_required_attribute, renderer)

        self.fields["message"].widget.attrs["class"] = "form-control"