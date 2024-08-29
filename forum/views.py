from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from forum.forms import ThreadForm
from forum.models import Thread, Post

class ForumHomeView(ListView):
    model = Thread
    context_object_name = "threads"
    template_name = "forum/home.html"

class ThreadDetailView(DetailView):
    model = Thread
    context_object_name = "thread"
    template_name = "forum/thread_detail.html"

class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadForm
    http_method_names = ["post"]
    
    def get_success_url(self):
        return reverse_lazy("forum:thread-detail", kwargs={"pk": self.kwargs.get("pk")})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.created_by = self.request.user

        return super().form_valid(form)

class PostCreateView(CreateView):
    model = Post
    form_class = ThreadForm
    http_method_names = ["post"]
    
    def get_success_url(self):
        return reverse_lazy("forum:thread-detail", kwargs={"pk": self.kwargs.get("pk")})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.thread = Thread.objects.get(pk=self.kwargs.get("pk"))
        form.instance.created_by = self.request.user

        return super().form_valid(form)
