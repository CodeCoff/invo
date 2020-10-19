from rest_framework import serializers
from app.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'company_address', 'company_ph')