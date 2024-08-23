from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy
from core.mixins import UserIsStaffMixin, UserHasNotCompletedMixin
from surveys.models import Survey, Question, Option

# Create your views here.
class SurveyHomeView(TemplateView):
    template_name = "surveys/home.html"

class SurveyDetailView(DetailView):
    model = Survey
    template_name = "surveys/survey_detail.html"
    context_object_name = "survey"


class SurveyCompleteView(UserHasNotCompletedMixin, DetailView):
    model = Survey
    template_name = "surveys/survey_complete.html"
    context_object_name = "survey"

    def post(self, request, *args, **kwargs):
        survey = self.get_object()
        survey.save_submition(request)

        return redirect("surveys:survey-detail", pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["questions"] = Question.objects.filter(survey=self.get_object())

        return context
    

class SurveyResultsView(UserIsStaffMixin, DetailView):
    model = Survey
    template_name = "surveys/survey_results.html"
    context_object_name = "survey"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["questions"] = Question.objects.filter(survey=self.get_object())

        return context