from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Job(models.Model):
    STATUS_CHOICES = [
        ("APPLIED", "Applied"),
        ("INTERVIEW", "Interview Scheduled"),
        ("OFFER", "Offer Received"),
        ("REJECTED", "Rejected"),
        ("GHOSTED", "No Response"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    job_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="APPLIED")
    date_applied = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    follow_up_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.follow_up_date and self.status == "APPLIED":
            self.follow_up_date = timezone.now().date() + timedelta(days=7)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company} - {self.role}"



class HR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)

    def __str__(self):
        return f"HR - {self.company}"
