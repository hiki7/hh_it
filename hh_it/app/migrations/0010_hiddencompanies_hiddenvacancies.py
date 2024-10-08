# Generated by Django 5.1.1 on 2024-10-08 15:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_remove_vacancy_technology_vacancy_technology"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HiddenCompanies",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "changed_at",
                    models.DateTimeField(auto_now=True, verbose_name="Changed at"),
                ),
                (
                    "company_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.company"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Айди пользователя",
                    ),
                ),
            ],
            options={
                "verbose_name": "[a1] Скрытая компания",
                "verbose_name_plural": "[a1] Скрытые компании",
            },
        ),
        migrations.CreateModel(
            name="HiddenVacancies",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "changed_at",
                    models.DateTimeField(auto_now=True, verbose_name="Changed at"),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Айди пользователя",
                    ),
                ),
                (
                    "vacancy_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.vacancy"
                    ),
                ),
            ],
            options={
                "verbose_name": "[a1] Скрытая вакансия",
                "verbose_name_plural": "[a1] Скрытые вакансии",
            },
        ),
    ]