import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserProfileService } from '../services/user-profile.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  profileForm: FormGroup;
  resumeFile: File | null = null;

  constructor(private formBuilder: FormBuilder, private userProfileService: UserProfileService) {
    this.profileForm = this.formBuilder.group({
      name: ['', Validators.required],
      address: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      phoneNumber: ['', Validators.required],
      minSalary: ['', Validators.required],
      maxSalary: ['', Validators.required],
      preferredLocations: ['', Validators.required],
      locationProximity: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.userProfileService.getUserProfile().subscribe(profile => {
      this.profileForm.patchValue(profile);
    });
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      this.userProfileService.updateUserProfile(this.profileForm.value).subscribe(() => {
        // Handle success message
      });
    }
  }

  onFileSelected(event: Event): void {
    const target = event.target as HTMLInputElement;
    const files = target.files;
    if (files && files.length > 0) {
      this.resumeFile = files[0];
    }
  }

  onUploadResume(): void {
    if (this.resumeFile) {
      this.userProfileService.uploadResume(this.resumeFile).subscribe(() => {
        // Handle success message
      });
    }
  }

  onImportFromLinkedIn(): void {
    this.userProfileService.importFromLinkedIn().subscribe(profile => {
      this.profileForm.patchValue(profile);
    });
  }
}