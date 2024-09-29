from rest_framework import serializers
from .models.models import Company, Technology, Vacancy


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'company_description', 'website', 'location']
