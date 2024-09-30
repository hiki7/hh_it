from django.utils.translation import gettext_lazy as _
from django.db import models
from .abstract import TimestampModel
from .dict import Technology, Company, Position

EMPLOYMENT_TYPE = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Contract', 'Contract'),
    ('Freelance', 'Freelance')
]

CURRENCY = [
    ('1', '₸'),
    ('2', '₽'),
    ('3', '€'),
    ('4', '$')
]


class Vacancy(TimestampModel):
    """Вакансия"""
    id: int
    position_name: Position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name='Позиция'
    )
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
    employment_type: str = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=EMPLOYMENT_TYPE,
    )
    technology: Technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        verbose_name='Технология'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активная'
    )

    @property
    def get_salary_range(self):
        if self.salary_start and self.salary_end:
            return f"{self.salary_start} - {self.salary_end}"
        elif self.salary_start:
            return f"от {self.salary_start} до вычета налогов"
        return "Уровень дохода не указан"


    class Meta:
        verbose_name_plural = _("[a1] Вакансии")
        verbose_name = _("[a1] Вакансия")

    def __str__(self):
        return self.position_name
