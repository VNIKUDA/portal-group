from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from core.mixins import UserHasNotCompletedMixin
from votes.models import Vote

# Create your views here.
class VoteHomeView(TemplateView):
    template_name = "votes/home.html"


class VoteDetailView(DetailView):
    model = Vote
    template_name = "votes/vote_detail.html"
    context_object_name = "vote"


class VoteCompleteView(UserHasNotCompletedMixin, DetailView):
    model = Vote
    template_name = "votes/vote_complete.html"
    context_object_name = "vote"

    def post(self, request, *args, **kwargs):
        vote = self.get_object()

        vote.save_submission(request)          

        return redirect("votes:vote-detail", pk=vote.pk)