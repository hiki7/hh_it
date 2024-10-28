from rest_framework import serializers
from .models import (
    Company,
    Technology,
    Vacancy,
    Country,
    City,
    Street,
    Location,
    Position,
    EmploymentType,
    HiddenCompanies,
    HiddenVacancies,
)
from django.contrib.auth.models import User

from .models.models import LikedVacancies


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name", "country"]


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ["id", "name"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "country", "city", "street"]


class CompanySerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Company
        fields = ["id", "name", "company_description", "website", "location"]


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "technology_name"]


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ["id", "name"]


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentType
        fields = ["id", "name"]


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    position_name = PositionSerializer()
    location = LocationSerializer()
    employment_type = EmploymentTypeSerializer(many=True)
    technology = TechnologySerializer(many=True)

    class Meta:
        model = Vacancy
        fields = [
            "id",
            "position_name",
            "salary_start",
            "salary_end",
            "currency",
            "get_salary_range",
            "required_experience_year_start",
            "required_experience_year_end",
            "position_description",
            "company",
            "location",
            "employment_type",
            "technology",
            "is_active",
        ]


class HiddenVacanciesSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    vacancy_id = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all())

    class Meta:
        model = HiddenVacancies
        fields = ["id", "user_id", "vacancy_id"]


class HiddenCompaniesSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = HiddenCompanies
        fields = ["id", "user_id", "company_id"]


class LikedVacanciesSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    vacancy_id = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all())

    class Meta:
        model = LikedVacancies
        fields = ["id", "user_id", "vacancy_id"]
