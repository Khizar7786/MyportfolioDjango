from django.db import models


class Experience(models.Model):
    TYPE_CHOICES = [
        ('professional', 'Professional'),
        ('academic', 'Academic'),
        ('volunteer', 'Volunteer'),
    ]

    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    experience_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='professional')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text='Leave blank if current')
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f'{self.title} at {self.organization}'

    @property
    def is_current(self):
        return self.end_date is None

    @property
    def duration(self):
        end = self.end_date.strftime('%b %Y') if self.end_date else 'Present'
        return f'{self.start_date.strftime("%b %Y")} – {end}'


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text='Comma-separated: Python, Django, React')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]
