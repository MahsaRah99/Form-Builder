from django.contrib import admin

from .models import Form, Question, Response


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = (
        "question_text",
        "question_type",
        "is_required",
        "place_holder",
        "numeric_constraint",
    )
    show_change_link = True


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title", "description")
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "form", "question_type", "question_text")
    search_fields = ("question_text",)
    list_filter = ("question_type", "is_required")


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "form")
    list_filter = ("question", "form")
