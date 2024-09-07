
from rest_framework import serializers

from API.models import Company

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'
        extra_kwargs = {'hash_id': {'required': False}}
        