# Generated by Django 5.1.1 on 2024-09-30 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_employmenttype_vacancy_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.location', verbose_name='Локация'),
            preserve_default=False,
        ),
    ]