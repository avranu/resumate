import { updateUserProfile, importFromLinkedIn } from './main';

document.addEventListener('DOMContentLoaded', () => {
  const saveProfileButton = document.getElementById('saveProfileButton');
  const linkedInButton = document.getElementById('linkedInButton');

  if (saveProfileButton) {
    saveProfileButton.addEventListener('click', () => {
      const nameInput = document.getElementById('nameInput') as HTMLInputElement;
      const addressInput = document.getElementById('addressInput') as HTMLInputElement;
      const phoneNumberInput = document.getElementById('phoneNumberInput') as HTMLInputElement;
      const minSalaryInput = document.getElementById('minSalaryInput') as HTMLInputElement;
      const maxSalaryInput = document.getElementById('maxSalaryInput') as HTMLInputElement;
      const preferredLocationsSelect = document.getElementById('preferredLocationsSelect') as HTMLSelectElement;
      const locationProximitySlider = document.getElementById('locationProximitySlider') as HTMLInputElement;

      const profileData = {
        name: nameInput.value,
        address: addressInput.value,
        phone_number: phoneNumberInput.value,
        min_salary: parseInt(minSalaryInput.value),
        max_salary: parseInt(maxSalaryInput.value),
        preferred_locations: Array.from(preferredLocationsSelect.selectedOptions).map(option => option.value),
        location_proximity: parseInt(locationProximitySlider.value),
      };

      updateUserProfile(profileData);
    });
  }

  if (linkedInButton) {
    linkedInButton.addEventListener('click', () => {
      importFromLinkedIn();
    });
  }
});