from django.db import models
from django.utils.translation import gettext_lazy as _


class QuestionTypes(models.TextChoices):
    SHORT_RESPONSED = "SR", _("Short responsed")
    LONG_RESPONSED = "LR", _("Long responsed")
    NUMERIC_RESPONSED = "NR", _("Numeric responsed")
    EMAIL_RESPONSED = "ER", _("Email responsed")


class NumericConstraints(models.TextChoices):
    INTEGER = "INT", _("Integer")
    FLOAT = "FLO", _("Float")
