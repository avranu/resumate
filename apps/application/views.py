from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Application
from .gpt4_integration import generate_cover_letter, review_documents
from resumate.apps.job_matching.models import Job
from resumate.apps.profile.models import UserProfile
from typing import Dict, Any

@login_required
def application_history(request):
    applications = Application.objects.filter(user=request.user)
    context = {'applications': applications}
    return render(request, 'application_history.html', context)

@csrf_exempt
@login_required
def apply_for_job(request, job_id: int):
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        user_profile = UserProfile.objects.get(user=request.user)
        resume = user_profile.resume
        cover_letter = generate_cover_letter(request.user, job)
        application_email = job.application_email

        if review_documents(resume, cover_letter, job.description):
            application = Application(user=request.user, job=job, resume=resume, cover_letter=cover_letter)
            application.save()
            send_application_email(application_email, resume, cover_letter)
            return JsonResponse({'message': 'JobApplySuccess'}, status=200)
        else:
            return JsonResponse({'message': 'JobApplyFailure'}, status=400)
    else:
        return JsonResponse({'message': 'InvalidRequestMethod'}, status=405)

def send_application_email(application_email: str, resume: Any, cover_letter: str) -> None:
    # Implement email sending logic here
    pass