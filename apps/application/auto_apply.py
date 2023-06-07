from typing import List
from django.core.mail import send_mail
from django.conf import settings
from resumate.apps.job_matching.models import Job
from resumate.apps.application.models import Application, User
from resumate.apps.application.gpt4_integration import generate_cover_letter, tailor_resume
from resumate.apps.job_matching.job_scoring import calculate_job_score


def auto_apply(user: User, max_applications: int = 5) -> None:
    if not user.profile.auto_apply_enabled:
        return

    jobs = Job.objects.filter(score__gte=settings.AUTO_APPLY_MIN_SCORE).order_by('-score')[:max_applications]
    applied_jobs = apply_to_jobs(user, jobs)

    if applied_jobs:
        send_summary_email(user, applied_jobs)


def apply_to_jobs(user: User, jobs: List[Job]) -> List[Job]:
    applied_jobs = []

    for job in jobs:
        if not Application.objects.filter(user=user, job=job).exists():
            cover_letter = generate_cover_letter(user, job)
            tailored_resume = tailor_resume(user.profile.resume, job)

            application = Application(user=user, job=job, cover_letter=cover_letter, resume=tailored_resume)
            application.save()

            send_application_email(user, job, cover_letter, tailored_resume)
            applied_jobs.append(job)

    return applied_jobs


def send_application_email(user: User, job: Job, cover_letter: str, tailored_resume: str) -> None:
    subject = f"Application for {job.title} at {job.company}"
    message = f"Dear Hiring Manager,\n\n{cover_letter}\n\nBest regards,\n{user.profile.name}"
    from_email = settings.EMAIL_HOST_USER
    to_email = [job.application_email]

    send_mail(subject, message, from_email, to_email, fail_silently=False, html_message=None)


def send_summary_email(user: User, applied_jobs: List[Job]) -> None:
    subject = "Resumate Weekly Auto-Apply Summary"
    message = f"Dear {user.profile.name},\n\nHere is a summary of the jobs you automatically applied for this week:\n\n"

    for job in applied_jobs:
        message += f"{job.title} at {job.company}\n"

    message += "\nBest of luck with your job search!\n\nThe Resumate Team"

    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]

    send_mail(subject, message, from_email, to_email, fail_silently=False, html_message=None)