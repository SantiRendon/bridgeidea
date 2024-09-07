
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

from API.serializers import TicketImageSerializer
from API.models import TicketImage, Ticket
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

class TicketImageViewSet(viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    
    queryset = TicketImage.objects.all()
    serializer_class = TicketImageSerializer
    
    def initial(self, request, *args, **kwargs):
        """
        Runs anything that needs to occur prior to calling the method handler.
        """
        self.ticket = get_object_or_404(Ticket, pk=self.kwargs.get('ticket_id', 0))
        if self.ticket.user != request.user:
            raise PermissionDenied({'error': 'El usuario no tiene permisos para realizar esta accion.'})
        return super().initial(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(ticket=self.ticket)