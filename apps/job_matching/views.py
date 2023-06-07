from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Job
from .job_scoring import calculate_job_score
from resumate.apps.profile.models import UserProfile

@method_decorator(login_required, name='dispatch')
class JobListView(View):
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        jobs = Job.objects.filter(
            location__in=user_profile.preferred_locations,
            salary__range=(user_profile.min_salary, user_profile.max_salary)
        )

        for job in jobs:
            job.score = calculate_job_score(job, user_profile)
            job.save()

        jobs = jobs.order_by('-score')

        context = {
            'jobs': jobs
        }
        return render(request, 'resumate/apps/job_matching/templates/job_list.html', context)

@method_decorator(login_required, name='dispatch')
class JobDetailView(View):
    def get(self, request, job_id):
        job = Job.objects.get(id=job_id)
        user_profile = UserProfile.objects.get(user=request.user)
        job.score = calculate_job_score(job, user_profile)
        job.save()

        context = {
            'job': job
        }
        return render(request, 'resumate/apps/job_matching/templates/job_details.html', context)

@login_required
def fetch_jobs(request):
    user_profile = UserProfile.objects.get(user=request.user)
    jobs = Job.objects.filter(
        location__in=user_profile.preferred_locations,
        salary__range=(user_profile.min_salary, user_profile.max_salary)
    )

    for job in jobs:
        job.score = calculate_job_score(job, user_profile)
        job.save()

    jobs = jobs.order_by('-score')

    job_data = []
    for job in jobs:
        job_data.append({
            'id': job.id,
            'title': job.title,
            'company': job.company,
            'location': job.location,
            'salary': job.salary,
            'perks': job.perks,
            'description': job.description,
            'score': job.score,
            'application_email': job.application_email
        })

    return JsonResponse({'jobs': job_data})