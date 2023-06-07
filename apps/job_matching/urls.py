from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('jobs/apply/<int:pk>/', views.apply_for_job, name='apply_for_job'),
]