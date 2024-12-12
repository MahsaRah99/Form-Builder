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
