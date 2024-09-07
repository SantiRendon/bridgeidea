
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin

from API.models import Ticket
from API.filters import TicketFilter
from API.serializers import TicketCreateSerializer, TicketListSerializer


class TicketViewSet(viewsets.GenericViewSet, CreateModelMixin,
                        ListModelMixin, RetrieveModelMixin):
    
    queryset = Ticket.objects.all().prefetch_related('images')
    filterset_class = TicketFilter
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TicketCreateSerializer
        return TicketListSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)