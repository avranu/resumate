import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationService } from '../shared/authentication.service';

@Component({
  selector: 'app-authentication',
  templateUrl: './authentication.component.html',
  styleUrls: ['./authentication.component.scss']
})
export class AuthenticationComponent implements OnInit {
  authForm: FormGroup;
  isLoginMode: boolean = true;
  errorMessage: string = '';

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthenticationService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.initForm();
  }

  initForm(): void {
    this.authForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['']
    });
  }

  onSwitchMode(): void {
    this.isLoginMode = !this.isLoginMode;
    this.errorMessage = '';
  }

  onSubmit(): void {
    if (this.authForm.invalid) {
      return;
    }

    const email = this.authForm.value.email;
    const password = this.authForm.value.password;

    if (this.isLoginMode) {
      this.authService.login(email, password).subscribe(
        () => {
          this.router.navigate(['/profile']);
        },
        (error) => {
          this.errorMessage = error;
        }
      );
    } else {
      const confirmPassword = this.authForm.value.confirmPassword;
      if (password !== confirmPassword) {
        this.errorMessage = 'Passwords do not match.';
        return;
      }

      this.authService.register(email, password).subscribe(
        () => {
          this.router.navigate(['/profile']);
        },
        (error) => {
          this.errorMessage = error;
        }
      );
    }
  }

  onForgotPassword(): void {
    const email = this.authForm.value.email;
    if (!email) {
      this.errorMessage = 'Please enter your email address.';
      return;
    }

    this.authService.forgotPassword(email).subscribe(
      () => {
        this.errorMessage = 'Password reset link sent to your email.';
      },
      (error) => {
        this.errorMessage = error;
      }
    );
  }
}