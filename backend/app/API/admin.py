from django.contrib import admin

from .models import TicketImage, Ticket

admin.site.register(Ticket)
admin.site.register(TicketImage)