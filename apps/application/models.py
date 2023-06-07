from django.db import models
from django.contrib.auth.models import User
from resumate.apps.job_matching.models import Job

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')
        verbose_name_plural = 'Applications'

    def __str__(self):
        return f"{self.user.email} - {self.job.title}"