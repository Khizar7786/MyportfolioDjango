from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'field_of_study', 'start_year', 'end_year')
    list_filter = ('start_year',)
