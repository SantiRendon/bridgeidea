from django_filters import rest_framework as filters

from API.models import Ticket

class TicketFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='date__gte')
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='date__lte')

    class Meta:
        model = Ticket
        fields = {
            'user': ['exact'],
            'state': ['exact'],
        }