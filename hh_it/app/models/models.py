from datetime import date

from django.db import models
from .abstract import TimestampModel


class Company(TimestampModel):
    """Компания"""
    id: int
    name: str = models.CharField(
        max_length=255,
        verbose_name='Компания'
    )
    company_description: str = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст компании'
    )
    website: str = models.URLField(
        null=True,
        blank=True,
        verbose_name='Веб-сайт компании'
    )
    location: str = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Локация компании'
    )

    def __str__(self):
        return self.name


class Technology(TimestampModel):
    """Технологии (Python, Docker, React, etc)"""
    id: int
    technology_name: str = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Технология'
    )

    def __str__(self):
        return self.technology_name


class Vacancy(TimestampModel):
    """Вакансия"""
    id: int
    position_name: str = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Позиция')
    salary_start: float = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Зарплата начало')
    salary_end: float = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Зарплата конец')
    required_experience_year_start: int = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Опыт начало')
    required_experience_year_end: int = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Опыт конец')
    position_description: str = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст вакансии'
    )
    company: Company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Компания'
    )
    location: str = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Локация вакансии'
    )
    posted_date: date = models.DateField(
        verbose_name='Дата поста вакансии'
    )
    employment_type: str = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=[
            ('Full-time', 'Full-time'),
            ('Part-time', 'Part-time'),
            ('Contract', 'Contract'),
            ('Freelance', 'Freelance')
        ]
    )
    technology: Technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        verbose_name='Технология'
    )

    def __str__(self):
        return self.position_name