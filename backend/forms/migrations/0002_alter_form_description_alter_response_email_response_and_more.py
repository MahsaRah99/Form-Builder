# Generated by Django 5.1.4 on 2024-12-12 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="response",
            name="email_response",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Email response"
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="f_responses",
                to="forms.form",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="long_response",
            field=models.CharField(
                blank=True, max_length=5000, null=True, verbose_name="Long response"
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="numeric_response",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Numeric response"
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="short_response",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Short response"
            ),
        ),
    ]
