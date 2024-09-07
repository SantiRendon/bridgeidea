
from rest_framework import viewsets

from API.serializers import CompanySerializer
from API.models import Company
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

@permission_classes([AllowAny])
class CompanyViewSet(viewsets.ModelViewSet):
    
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def perform_create(self, serializer):
        #TODO: create tokne in AVALANCHE
        serializer.save(ticket=self.ticket)