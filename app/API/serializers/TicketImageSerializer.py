
from rest_framework import serializers

from API.models import TicketImage

class TicketImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TicketImage
        fields = '__all__'
        extra_kwargs = {
            'ticket': {'required': False},
        }
        
class TicketReadImageSerializer(serializers.ModelSerializer):
    
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = TicketImage
        fields = ('id', 'image_url')
        
    def get_image_url(self, obj):
        return obj.image.url
        