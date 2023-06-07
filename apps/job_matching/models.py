from django.db import models
from django.contrib.postgres.fields import ArrayField
from resumate.apps.authentication.models import User

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    perks = models.TextField()
    description = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    application_email = models.EmailField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class UserJobPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_locations = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    location_proximity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.email}'s Job Preferences"