import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

interface Application {
  job_id: number;
  job_title: string;
  company: string;
  applied_at: Date;
  resume: string;
  cover_letter: string;
}

@Component({
  selector: 'app-application',
  templateUrl: './application.component.html',
  styleUrls: ['./application.component.scss']
})
export class ApplicationComponent implements OnInit {
  applications: Application[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchApplicationHistory();
  }

  fetchApplicationHistory(): void {
    this.http.get<Application[]>(`${environment.apiUrl}/applications`).subscribe(
      (data) => {
        this.applications = data;
      },
      (error) => {
        console.error('Error fetching application history:', error);
      }
    );
  }
}