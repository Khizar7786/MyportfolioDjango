from django.contrib import admin
from .models import Experience, Project


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'experience_type', 'start_date', 'end_date')
    list_filter = ('experience_type',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured',)
    filter_horizontal = ()
