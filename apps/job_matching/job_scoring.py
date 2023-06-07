from typing import List
from resumate.apps.job_matching.models import Job
from resumate.apps.profile.models import UserProfile


def calculate_job_score(job: Job, user_profile: UserProfile) -> float:
    score = 0.0

    # Salary score
    salary_score = 0.0
    if job.salary >= user_profile.min_salary and job.salary <= user_profile.max_salary:
        salary_score = 1.0
    elif job.salary >= user_profile.min_salary:
        salary_score = 0.5
    score += salary_score

    # Commute distance score
    commute_score = 0.0
    if job.location in user_profile.preferred_locations:
        commute_score = 1.0
    elif user_profile.location_proximity >= 100:
        commute_score = 0.5
    score += commute_score

    # Perks score
    perks_score = 0.0
    if job.perks:
        perks_score = 0.5
    score += perks_score

    # Normalize the score to a range of 0 to 100
    normalized_score = (score / 3.0) * 100

    return normalized_score


def update_job_scores(user_profile: UserProfile, jobs: List[Job]) -> List[Job]:
    for job in jobs:
        job.score = calculate_job_score(job, user_profile)
        job.save()

    return jobs