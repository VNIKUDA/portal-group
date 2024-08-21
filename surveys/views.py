from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from surveys.mixins import UserIsStaffMixin # type: ignore
from surveys.models import Survey, Question, Option

# Create your views here.
class SurveyDetailView(DetailView):
    model = Survey
    context_object_name = "survey"
    template_name = "surveys/survey_detail.html"


class SurveyCompleteView(TemplateView):
    template_name = "surveys/survey_complete.html"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        survey = self.get_object()

        if self.request.user in survey.get_users_that_completed():
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        survey = self.get_object()
        survey.save_submition(self.request)

        return redirect("surveys:survey-detail", pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        survey = self.get_object()

        context["survey"] = survey
        context["questions"] = Question.objects.filter(survey=survey)

        return context
    
    def get_object(self):
        return Survey.objects.get(pk=self.kwargs.get("pk"))
    

class SurveyResultsView(UserIsStaffMixin, TemplateView):
    template_name = "surveys/survey_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        survey = self.get_object()

        context["survey"] = survey
        context["questions"] = Question.objects.filter(survey=survey)

        return context


    def get_object(self):
        return Survey.objects.get(pk=self.kwargs.get("pk"))