from django.contrib import admin

from .models import Company, Project, Solution

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Solution)