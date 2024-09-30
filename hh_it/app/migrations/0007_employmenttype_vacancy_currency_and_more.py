# Generated by Django 5.1.1 on 2024-09-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_company_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmploymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Changed at')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Название занятости')),
            ],
            options={
                'verbose_name': 'Тип занятости',
                'verbose_name_plural': 'Типы занятостей',
            },
        ),
        migrations.AddField(
            model_name='vacancy',
            name='currency',
            field=models.CharField(choices=[('KZT', '₸'), ('RUB', '₽'), ('EUR', '€'), ('USD', '$')], default='KZT', max_length=3, verbose_name='Валюта'),
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='employment_type',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='employment_type',
            field=models.ManyToManyField(blank=True, to='app.employmenttype', verbose_name='Тип занятости'),
        ),
    ]