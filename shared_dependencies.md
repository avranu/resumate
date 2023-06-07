the app is: Resumate

the files we have decided to generate are: 
- backend/models.py
- backend/views.py
- backend/urls.py
- backend/serializers.py
- backend/scrapers.py
- backend/tasks.py
- backend/utils.py
- frontend/src/app/app.component.ts
- frontend/src/app/app.component.html
- frontend/src/app/app.component.scss
- frontend/src/app/auth/auth.component.ts
- frontend/src/app/auth/auth.component.html
- frontend/src/app/auth/auth.component.scss
- frontend/src/app/profile/profile.component.ts
- frontend/src/app/profile/profile.component.html
- frontend/src/app/profile/profile.component.scss
- frontend/src/app/job/job.component.ts
- frontend/src/app/job/job.component.html
- frontend/src/app/job/job.component.scss
- frontend/src/app/settings/settings.component.ts
- frontend/src/app/settings/settings.component.html
- frontend/src/app/settings/settings.component.scss
- frontend/src/app/history/history.component.ts
- frontend/src/app/history/history.component.html
- frontend/src/app/history/history.component.scss

Shared dependencies:
- User model: id, email, password
- UserProfile model: user_id, name, address, phone_number, min_salary, max_salary, preferred_locations, location_proximity
- Job model: id, title, company, location, salary, perks, description, score, application_email
- Application model: user_id, job_id, resume, cover_letter, applied_at
- DOM element ids: emailInput, passwordInput, confirmPasswordInput, forgotPasswordLink, linkedInButton, nameInput, addressInput, phoneNumberInput, minSalaryInput, maxSalaryInput, preferredLocationsSelect, locationProximitySlider, resumeUpload, applyButton, autoApplyToggle, pauseIndexingToggle
- Message names: registrationSuccess, loginSuccess, profileUpdateSuccess, resumeUploadSuccess, jobApplySuccess, autoApplyEnabled, autoApplyDisabled, indexingPaused, indexingResumed
- Function names: registerUser, loginUser, forgotPassword, updateUserProfile, importFromLinkedIn, uploadResume, fetchJobs, calculateJobScore, applyForJob, viewApplicationHistory, toggleAutoApply, togglePauseIndexing, crawlJobBoards, evaluateJobWithAI, sendApplicationEmail, secureUserPassword, logErrors