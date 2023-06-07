import openai
from typing import Dict, Tuple
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def evaluate_job_with_ai(job: Dict, user_profile: Dict) -> Tuple[float, str, str, str]:
    prompt = f"Using GPT-4, evaluate the suitability of the following job for the user with the given qualifications:\n\nJob:\n{job}\n\nUser Qualifications:\n{user_profile}\n\nDetermine the suitability score (0-100), application email address, salary range, and geographical location."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    score, email, salary_range, location = answer.split("\n")

    return float(score), email, salary_range, location

def review_documents_with_ai(resume: str, cover_letter: str, job_description: str) -> Tuple[str, str]:
    prompt = f"Using GPT-4, review and improve the following resume and cover letter to align with the job description:\n\nResume:\n{resume}\n\nCover Letter:\n{cover_letter}\n\nJob Description:\n{job_description}\n\nProvide the improved resume and cover letter."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    improved_resume, improved_cover_letter = answer.split("\n\n")

    return improved_resume, improved_cover_letter