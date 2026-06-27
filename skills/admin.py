from django.contrib import admin
from .models import SkillCategory, Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3
    fields = ('name', 'proficiency', 'order')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
