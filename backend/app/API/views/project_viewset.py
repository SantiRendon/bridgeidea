
from rest_framework import viewsets

from API.serializers import ProjectSerializer
from API.models import Project
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

@permission_classes([AllowAny])
class ProjectViewSet(viewsets.ModelViewSet):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    # def perform_create(self, serializer):
    #     #TODO: create tokne in AVALANCHE
    #     serializer.save(ticket=self.ticket)