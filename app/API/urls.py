
from django.urls import path
from rest_framework.routers import DefaultRouter
from API import views

router = DefaultRouter()

router.register(r'tickets', views.TicketViewSet, basename='tickets')
router.register(r'tickets/(?P<ticket_id>\d+)/images', views.TicketImageViewSet, basename='ticket_images')

urlpatterns = [
] + router.urls
