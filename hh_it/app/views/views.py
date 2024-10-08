from rest_framework import permissions, viewsets
from drf_spectacular.utils import extend_schema
from ..models import Vacancy
from ..models.models import HiddenVacancies, HiddenCompanies
from ..serializers import (
    VacancySerializer,
    HiddenVacanciesSerializer,
    HiddenCompaniesSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=["Vacancy"])
class VacancyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vacancies to be viewed or edited.
    """

    queryset = Vacancy.objects.all().order_by("-created_at")
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["position_name__name", "is_active"]

    def get_queryset(self):
        user = self.request.user

        hidden_vacancies = HiddenVacancies.objects.filter(user_id=user).values_list(
            "vacancy_id"
        )
        hidden_companies = HiddenCompanies.objects.filter(user_id=user).values_list(
            "company_id"
        )

        return Vacancy.objects.exclude(id__in=hidden_vacancies).exclude(
            company_id__in=hidden_companies
        )


@extend_schema(tags=["Hidden Vacancies"])
class HiddenVacanciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hidden vacancies to be viewed or edited.
    """

    queryset = HiddenVacancies.objects.all().order_by("-created_at")
    serializer_class = HiddenVacanciesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user_id", "vacancy_id"]


@extend_schema(tags=["Hidden Companies"])
class HiddenCompaniesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hidden companies to be viewed or edited.
    """

    queryset = HiddenCompanies.objects.all().order_by("-created_at")
    serializer_class = HiddenCompaniesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user_id", "company_id"]
