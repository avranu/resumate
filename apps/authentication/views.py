from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.views.decorators.csrf import csrf_exempt

from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("profile:create_profile"))
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = RegistrationForm()
        return render(request, "authentication/registration.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("job_matching:index"))
        else:
            return JsonResponse({"error": "Invalid email or password"}, status=401)
    else:
        return render(request, "authentication/login.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("authentication:login"))

@csrf_exempt
def forgot_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = request.build_absolute_uri(reverse("authentication:reset_password", args=[uid, token]))
                send_mail("Password Reset", f"Click the link to reset your password: {reset_link}", "noreply@resumate.com", [user.email])
                return JsonResponse({"message": "Password reset email sent"})
            else:
                return JsonResponse({"error": "User not found"}, status=404)
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        return render(request, "authentication/forgot_password.html")