from django.urls import path
from resumate.apps.authentication.views import RegisterView, LoginView, ForgotPasswordView
from resumate.apps.profile.views import UserProfileView, EditProfileView, LinkedInImportView
from resumate.apps.job_matching.views import JobListView, JobDetailsView
from resumate.apps.application.views import ApplicationHistoryView, ApplyForJobView, AutoApplySettingsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/linkedin-import/', LinkedInImportView.as_view(), name='linkedin_import'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/<int:job_id>/', JobDetailsView.as_view(), name='job_details'),
    path('applications/', ApplicationHistoryView.as_view(), name='application_history'),
    path('apply/<int:job_id>/', ApplyForJobView.as_view(), name='apply_for_job'),
    path('settings/auto-apply/', AutoApplySettingsView.as_view(), name='auto_apply_settings'),
]