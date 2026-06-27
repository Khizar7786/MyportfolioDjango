from django.db import models


class Bio(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    description = models.TextField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Bio'
        verbose_name_plural = 'Bio'

    def __str__(self):
        return self.name
