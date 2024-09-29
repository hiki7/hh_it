from rest_framework import serializers
from .models.models import Company, Technology, Vacancy


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
            'position_description', 'company', 'location', 'posted_date',
            'employment_type', 'technology'
        ]