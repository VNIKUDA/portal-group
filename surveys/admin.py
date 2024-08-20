from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin
from surveys.models import Survey, Question, Option

class OptionInLine(NestedTabularInline):
    model = Option
    extra = 1
    fields = ["value", "correct"]

class QuestionInLine(NestedStackedInline):
    model = Question
    extra = 1
    inlines = [OptionInLine]

class SurveyAdmin(NestedModelAdmin):
    inlines = [QuestionInLine]

# Register your models here.
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
admin.site.register(Option)