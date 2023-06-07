import { fetchJobs, calculateJobScore } from './utils';

document.addEventListener('DOMContentLoaded', () => {
  loadJobList();
});

async function loadJobList() {
  try {
    const jobs = await fetchJobs();
    const jobListElement = document.getElementById('job-list');

    jobs.forEach((job) => {
      const jobScore = calculateJobScore(job);
      const jobElement = createJobElement(job, jobScore);
      jobListElement.appendChild(jobElement);
    });
  } catch (error) {
    console.error('Error fetching jobs:', error);
  }
}

function createJobElement(job, jobScore) {
  const jobElement = document.createElement('div');
  jobElement.classList.add('job-item');

  const jobTitle = document.createElement('h3');
  jobTitle.textContent = job.title;
  jobElement.appendChild(jobTitle);

  const jobCompany = document.createElement('p');
  jobCompany.textContent = `Company: ${job.company}`;
  jobElement.appendChild(jobCompany);

  const jobLocation = document.createElement('p');
  jobLocation.textContent = `Location: ${job.location}`;
  jobElement.appendChild(jobLocation);

  const jobSalary = document.createElement('p');
  jobSalary.textContent = `Salary: ${job.salary}`;
  jobElement.appendChild(jobSalary);

  const jobScoreElement = document.createElement('p');
  jobScoreElement.textContent = `Score: ${jobScore}`;
  jobElement.appendChild(jobScoreElement);

  const applyButton = document.createElement('button');
  applyButton.textContent = 'Apply';
  applyButton.addEventListener('click', () => {
    applyForJob(job);
  });
  jobElement.appendChild(applyButton);

  return jobElement;
}

function applyForJob(job) {
  // Implement the applyForJob function from the shared dependencies
}