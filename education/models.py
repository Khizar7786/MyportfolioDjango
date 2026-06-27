from django.db import models


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True, help_text='Leave blank if currently enrolled')
    grade = models.CharField(max_length=50, blank=True, help_text='e.g. 3.8 GPA or First Class Honours')
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_year']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return f'{self.degree} — {self.institution}'

    @property
    def duration(self):
        end = self.end_year if self.end_year else 'Present'
        return f'{self.start_year} – {end}'
