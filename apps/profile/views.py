from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from typing import Any, Dict

@login_required
def profile(request) -> Any:
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context: Dict[str, Any] = {
        'form': form,
        'user_profile': user_profile
    }
    return render(request, 'resumate/apps/profile/templates/profile.html', context)

@login_required
def edit_profile(request) -> Any:
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context: Dict[str, Any] = {
        'form': form
    }
    return render(request, 'resumate/apps/profile/templates/edit_profile.html', context)

@login_required
def import_from_linkedin(request) -> Any:
    # Implement LinkedIn integration here
    pass

@login_required
def upload_resume(request) -> Any:
    # Implement resume upload functionality here
    pass