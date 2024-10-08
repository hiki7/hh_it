from rest_framework import permissions, viewsets
from drf_spectacular.utils import extend_schema
from ..models import Vacancy
from ..models.models import HiddenVacancies, HiddenCompanies
from ..serializers import VacancySerializer
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
