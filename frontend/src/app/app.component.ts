import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Resumate';

  constructor(private router: Router) {}

  navigateToRegistration(): void {
    this.router.navigate(['/auth/register']);
  }

  navigateToLogin(): void {
    this.router.navigate(['/auth/login']);
  }

  navigateToProfile(): void {
    this.router.navigate(['/profile']);
  }

  navigateToJobMatching(): void {
    this.router.navigate(['/job']);
  }

  navigateToSettings(): void {
    this.router.navigate(['/settings']);
  }

  navigateToApplicationHistory(): void {
    this.router.navigate(['/history']);
  }
}