# Generated by Django 5.1.4 on 2024-12-12 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question_type",
                    models.CharField(
                        choices=[
                            ("SR", "Short responsed"),
                            ("LR", "Long responsed"),
                            ("NR", "Numeric responsed"),
                            ("ER", "Email responsed"),
                        ],
                        max_length=2,
                        verbose_name="Question Type",
                    ),
                ),
                (
                    "question_text",
                    models.CharField(max_length=300, verbose_name="Question text"),
                ),
                (
                    "is_required",
                    models.BooleanField(default=True, verbose_name="Is required"),
                ),
                (
                    "place_holder",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Place holder",
                    ),
                ),
                (
                    "numeric_constraint",
                    models.CharField(
                        blank=True,
                        choices=[("INT", "Integer"), ("FLO", "Float")],
                        max_length=3,
                        null=True,
                        verbose_name="Numeric constraint",
                    ),
                ),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="forms.form"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Response",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "short_response",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("long_response", models.TextField(blank=True, null=True)),
                (
                    "email_response",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("numeric_response", models.FloatField(blank=True, null=True)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responses",
                        to="forms.form",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="q_responses",
                        to="forms.question",
                    ),
                ),
            ],
        ),
    ]
