from rest_framework import routers
from django.urls import include, path
from .views import (VacancyViewSet, CompanyViewSet, PositionViewSet, TechnologyViewSet,
                    CountryViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = routers.DefaultRouter()
router.register(r'vacancy', VacancyViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'position', PositionViewSet)
router.register(r'technology', TechnologyViewSet)
router.register(r'country', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += router.urls
