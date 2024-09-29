from django.db import models
from .abstract import TimestampModel
from django.utils.translation import gettext_lazy as _


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

    class Meta:
        verbose_name_plural = _("Компании")
        verbose_name = _("Компания")

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

    class Meta:
        verbose_name_plural = _("Технологии")
        verbose_name = _("Технология")

    def __str__(self):
        return self.technology_name


class Position(TimestampModel):
    """Позиция"""
    id: int
    name: str = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='Позиция')

    class Meta:
        verbose_name_plural = _("Позиции")
        verbose_name = _("Позиция")

    def __str__(self):
        return self.name
