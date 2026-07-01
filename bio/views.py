from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill, SkillCategory
from experience.models import Experience, Project


def portfolio(request):
    bio = Bio.objects.first()
    educations = Education.objects.all().order_by('-start_year')
    skill_categories = SkillCategory.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all().order_by('-created_at')

    context = {
        'bio': bio,
        'educations': educations,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'projects': projects,
    }
    return render(request, 'portfolio.html', context)
