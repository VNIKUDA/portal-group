from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from forum.forms import ThreadForm, PostForm
from forum.models import Thread, Post

class ForumHomeView(ListView):
    model = Thread
    context_object_name = "threads"
    template_name = "forum/home.html"


class ThreadSearchView(ListView):
    model = Thread
    context_object_name = "threads"
    template_name = "forum/thread_search.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("query")

        matched_query = queryset.filter(title__contains=search_query)

        return matched_query

class ThreadDetailView(DetailView):
    model = Thread
    context_object_name = "thread"
    template_name = "forum/thread_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['post_form'] = PostForm()

        return context

class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadForm
    
    def get_success_url(self):
        return reverse_lazy("forum:thread-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.created_by = self.request.user
        self.object = form.instance

        return super().form_valid(form)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    http_method_names = ["post"]
    
    def get_success_url(self):
        return reverse_lazy("forum:thread-detail", kwargs={"pk": self.kwargs.get("pk")})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.thread = Thread.objects.get(pk=self.kwargs.get("pk"))
        form.instance.created_by = self.request.user

        return super().form_valid(form)
