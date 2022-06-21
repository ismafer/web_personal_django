from django.contrib import admin
from .models import Project

# Register your models here.
class Projectadmin(admin.ModelAdmin):
    readonly_fields = ('create','update')

admin.site.register(Project, Projectadmin)
