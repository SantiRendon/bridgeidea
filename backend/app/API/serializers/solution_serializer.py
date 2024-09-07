
from rest_framework import serializers

from API.models import Solution

class SolutionSerializer(serializers.ModelSerializer):
    
    state_name = serializers.CharField(max_length=300, read_only=True)
    
    class Meta:
        model = Solution
        fields = '__all__'
        extra_kwargs = {'hash_id': {'required': False}}
        