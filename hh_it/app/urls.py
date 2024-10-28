from rest_framework import routers
from django.urls import include, path
from .views import (
    VacancyViewSet,
    CompanyViewSet,
    PositionViewSet,
    TechnologyViewSet,
    CountryViewSet,
    CityViewSet,
    StreetViewSet,
    LocationViewSet,
    EmploymentTypeViewSet,
    HiddenVacanciesViewSet,
    HiddenCompaniesViewSet,
    LikedVacanciesViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = routers.DefaultRouter()
router.register(r"vacancy", VacancyViewSet)
router.register(r"company", CompanyViewSet)
router.register(r"position", PositionViewSet)
router.register(r"technology", TechnologyViewSet)
router.register(r"country", CountryViewSet)
router.register(r"city", CityViewSet)
router.register(r"street", StreetViewSet)
router.register(r"location", LocationViewSet)
router.register(r"employment_type", EmploymentTypeViewSet)
router.register(r"hidden_vacancies", HiddenVacanciesViewSet)
router.register(r"hidden_companies", HiddenCompaniesViewSet)
router.register(r"liked_vacancies", LikedVacanciesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += router.urls
