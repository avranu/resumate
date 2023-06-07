from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from typing import List

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    preferred_locations = models.JSONField(default=list)
    location_proximity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self) -> str:
        return self.name

    def update_profile(self, name: str, address: str, phone_number: str, min_salary: int, max_salary: int, preferred_locations: List[str], location_proximity: int) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.preferred_locations = preferred_locations
        self.location_proximity = location_proximity
        self.save()