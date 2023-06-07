from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator, MinLengthValidator

from resumate.apps.authentication.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        validators=[EmailValidator()],
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )
    password1 = forms.CharField(
        validators=[MinLengthValidator(8)],
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        validators=[MinLengthValidator(8)],
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        validators=[EmailValidator()],
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )
    password = forms.CharField(
        validators=[MinLengthValidator(8)],
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        validators=[EmailValidator()],
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )