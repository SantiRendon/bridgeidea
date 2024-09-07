
from django.urls import path
from rest_framework.routers import DefaultRouter
from API import views

router = DefaultRouter()

router.register(r'companies', views.CompanyViewSet, basename='companies')
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'solutions', views.SolutionViewSet, basename='solutions')

urlpatterns = [
] + router.urls
