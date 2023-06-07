from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path("create/", views.CreateProfileView.as_view(), name="create_profile"),
    path("edit/", views.EditProfileView.as_view(), name="edit_profile"),
    path("view/", views.ViewProfileView.as_view(), name="view_profile"),
    path("import_linkedin/", views.import_linkedin, name="import_linkedin"),
    path("upload_resume/", views.upload_resume, name="upload_resume"),
]