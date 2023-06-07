import { Component, OnInit } from '@angular/core';
import { JobService } from '../services/job.service';
import { Job } from '../models/job.model';

@Component({
  selector: 'app-job-matching',
  templateUrl: './job_matching.component.html',
  styleUrls: ['./job_matching.component.scss']
})
export class JobMatchingComponent implements OnInit {
  jobs: Job[] = [];

  constructor(private jobService: JobService) { }

  ngOnInit(): void {
    this.fetchJobs();
  }

  fetchJobs(): void {
    this.jobService.getJobs().subscribe(jobs => {
      this.jobs = jobs.map(job => {
        job.score = this.calculateJobScore(job);
        return job;
      });
    });
  }

  calculateJobScore(job: Job): number {
    // Implement the scoring algorithm here
    // This is a placeholder implementation, replace with the actual algorithm
    return Math.floor(Math.random() * 100);
  }

  applyForJob(job: Job): void {
    this.jobService.applyForJob(job).subscribe(response => {
      if (response.success) {
        alert('Job application submitted successfully.');
      } else {
        alert('Failed to submit job application.');
      }
    });
  }
}