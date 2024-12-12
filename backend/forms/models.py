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
