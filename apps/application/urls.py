from django.urls import path
from . import views

app_name = "application"

urlpatterns = [
    path("apply/<int:job_id>/", views.apply_for_job, name="apply_for_job"),
    path("history/", views.view_application_history, name="application_history"),
]