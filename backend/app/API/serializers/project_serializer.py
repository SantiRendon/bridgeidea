
from rest_framework import serializers

from API.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'
        