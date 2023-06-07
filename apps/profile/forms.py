from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Name")
    address = forms.CharField(max_length=255, required=True, label="Address")
    email = forms.EmailField(required=True, label="Email")
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
    min_salary = forms.IntegerField(required=True, label="Minimum Salary Expectation")
    max_salary = forms.IntegerField(required=True, label="Maximum Salary Expectation")
    preferred_locations = forms.MultipleChoiceField(choices=UserProfile.LOCATION_CHOICES, required=True, label="Preferred Job Locations")
    location_proximity = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], required=True, label="Job Location Proximity")

    class Meta:
        model = UserProfile
        fields = ['name', 'address', 'email', 'phone_number', 'min_salary', 'max_salary', 'preferred_locations', 'location_proximity']

class ResumeUploadForm(forms.Form):
    resume = forms.FileField(allow_empty_file=False, required=True, label="Upload Resume", widget=forms.FileInput(attrs={'accept': '.pdf,.doc,.docx'}))