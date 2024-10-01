from rest_framework import permissions, viewsets
from drf_spectacular.utils import extend_schema
from ..models import (Company, Position, Technology, Country,
                      City, Street, Location, EmploymentType)
from ..serializers import (CompanySerializer, PositionSerializer, TechnologySerializer, CountrySerializer,
                           CitySerializer, StreetSerializer, LocationSerializer, EmploymentTypeSerializer)
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=["Company"])
class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('-created_at')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']