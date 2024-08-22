from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.html import format_html
from nested_inline.admin import NestedTabularInline, NestedModelAdmin
from surveys.models import Survey, Question, Option

class OptionInLine(NestedTabularInline):
    model = Option
    extra = 1
    fields = ["value"]

class QuestionInLine(NestedTabularInline):
    model = Question
    extra = 1
    inlines = [OptionInLine]

class SurveyAdmin(NestedModelAdmin):
    list_display = ["title", "complete_survey", "results"]
    inlines = [QuestionInLine]

    def complete_survey(self, obj):
        url = reverse_lazy("surveys:survey-complete", kwargs={"pk": obj.pk})
        return format_html('<a href="{}">Complete this survey</a>', url)
    complete_survey.short_description = "Complete links"

    def results(self, obj):
        url = reverse_lazy("surveys:survey-results", kwargs={"pk": obj.pk})
        return format_html('<a href="{}">See results</a>', url)
    results.short_description = 'Results'

# Register your models here.
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
admin.site.register(Option)