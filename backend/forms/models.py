from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .enums import NumericConstraints, QuestionTypes
from .validators import validate_response


class Form(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_type = models.CharField(
        _("Question Type"), max_length=2, choices=QuestionTypes
    )
    question_text = models.CharField(_("Question text"), max_length=300)
    is_required = models.BooleanField(_("Is required"), default=True)
    place_holder = models.CharField(
        _("Place holder"), max_length=100, blank=True, null=True
    )
    numeric_constraint = models.CharField(
        _("Numeric constraint"),
        max_length=3,
        choices=NumericConstraints,
        blank=True,
        null=True,
    )

    def clean(self):
        if not self.question_type == "NR" and self.numeric_constraint:
            raise ValidationError("Numeric constraint can't be set for this question.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question_text} ({self.get_question_type_display()})"


class Response(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="q_responses"
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="f_responses")
    short_response = models.CharField(
        _("Short response"), max_length=200, blank=True, null=True
    )
    long_response = models.CharField(
        _("Long response"), max_length=5000, blank=True, null=True
    )
    email_response = models.EmailField(_("Email response"), blank=True, null=True)
    numeric_response = models.FloatField(_("Numeric response"), blank=True, null=True)

    def __str__(self):
        return f"response to {self.question.question_text}"

    def clean(self):
        validate_response(self.__dict__, self.question, self.question.is_required)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
