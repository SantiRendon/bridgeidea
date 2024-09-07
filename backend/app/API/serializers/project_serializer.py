
from rest_framework import serializers

from API.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    state_name = serializers.CharField(max_length=300, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {'hash_id': {'required': False}}
        