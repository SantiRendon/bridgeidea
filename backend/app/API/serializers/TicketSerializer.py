
from rest_framework import serializers
from API.models import Ticket

from API.serializers import TicketReadImageSerializer

class TicketCreateSerializer(serializers.ModelSerializer):
    
    state = serializers.SerializerMethodField()
    
    class Meta:
        model = Ticket
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}
        }
        
    def get_state(self, obj):
        return obj.get_state_display()
        
class TicketListSerializer(serializers.ModelSerializer):
    
    images = TicketReadImageSerializer(many=True)
    
    state = serializers.SerializerMethodField()
    
    class Meta:
        model = Ticket
        fields = ('id', 'user', 'state', 'num_images',
                    'description', 'created_at', 'images')
        
    def get_state(self, obj):
        return obj.get_state_display()