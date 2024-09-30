from rest_framework import serializers
from .models import Company, Technology, Vacancy, Country, City, Street, Location, Position, EmploymentType


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'company_description', 'website', 'location']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'technology_name']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'id', 'position_name', 'salary_start', 'salary_end',
            'required_experience_year_start', 'required_experience_year_end',
            'position_description', 'company', 'location',
            'employment_type', 'technology'
        ]
