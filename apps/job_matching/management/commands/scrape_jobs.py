from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from resumate.apps.job_matching.models import Job

class Command(BaseCommand):
    help = "Scrape job listings from specified job boards and store them in the database."

    def handle(self, *args, **options):
        self.stdout.write("Starting job scraping process...")
        job_listings = self.scrape_ny_state_jobs()
        self.save_job_listings(job_listings)
        self.stdout.write("Job scraping process completed.")

    def scrape_ny_state_jobs(self) -> List[Dict]:
        url = "https://statejobs.ny.gov/public/vacancyTable.cfm"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"class": "stripeMe"})
        rows = table.find_all("tr")[1:]

        job_listings = []

        for row in rows:
            cells = row.find_all("td")
            grade = int(cells[4].text.strip())

            if grade >= 18:
                job_listings.append({
                    "title": cells[0].text.strip(),
                    "company": "New York State",
                    "location": cells[1].text.strip(),
                    "salary": grade * 1000,
                    "perks": "",
                    "description": cells[2].text.strip(),
                    "application_email": "",
                })

        return job_listings

    def save_job_listings(self, job_listings: List[Dict]):
        for job_data in job_listings:
            job, created = Job.objects.get_or_create(
                title=job_data["title"],
                company=job_data["company"],
                location=job_data["location"],
                defaults={
                    "salary": job_data["salary"],
                    "perks": job_data["perks"],
                    "description": job_data["description"],
                    "application_email": job_data["application_email"],
                }
            )

            if created:
                self.stdout.write(f"New job listing added: {job.title} at {job.company}")
            else:
                self.stdout.write(f"Job listing already exists: {job.title} at {job.company}")