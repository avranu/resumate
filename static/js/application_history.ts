import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

interface Application {
  job: {
    id: number;
    title: string;
    company: string;
    location: string;
    salary: number;
    perks: string;
    description: string;
    score: number;
    application_email: string;
  };
  resume: string;
  cover_letter: string;
  applied_at: string;
}

@Component({
  selector: 'app-application-history',
  templateUrl: './application_history.component.html',
  styleUrls: ['./application_history.component.scss'],
})
export class ApplicationHistoryComponent implements OnInit {
  applications: Application[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchApplicationHistory();
  }

  fetchApplicationHistory(): void {
    this.http.get<Application[]>('/api/application/history').subscribe(
      (data) => {
        this.applications = data;
      },
      (error) => {
        console.error('Error fetching application history:', error);
      }
    );
  }
}