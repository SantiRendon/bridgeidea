
from rest_framework import viewsets

from API.serializers import SolutionSerializer
from API.models import Solution

from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

@permission_classes([AllowAny])
class SolutionViewSet(viewsets.ModelViewSet):
    
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    
    # def perform_create(self, serializer):
    #     #TODO: create tokne in AVALANCHE
    #     serializer.save(ticket=self.ticket)