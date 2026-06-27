from django.db import models


class SkillCategory(models.Model):
    name = models.CharField(max_length=100, help_text='e.g. Languages, Frameworks, Tools')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Skill Category'
        verbose_name_plural = 'Skill Categories'

    def __str__(self):
        return self.name


class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        (25, 'Beginner'),
        (50, 'Intermediate'),
        (75, 'Advanced'),
        (90, 'Expert'),
    ]

    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=PROFICIENCY_CHOICES, default=75)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.name} ({self.category})'
