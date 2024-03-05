from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    SIZE_1_9 = 'size_1_9'
    SIZE_10_49 = 'size_10_49'
    SIZE_50_99 = 'size_50_99'
    SIZE_100 = 'size_100'
    
    SIZE_CHOICES = (
        (SIZE_1_9, '1-9'),
        (SIZE_10_49, '10-49'),
        (SIZE_50_99, '50-99'),
        (SIZE_100, '100+'),
    )
    
    title = models.CharField(max_length=100)
    summary = models.TextField()
    full_description = models.TextField()
    
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(max_length=20, choices=SIZE_CHOICES, default=SIZE_1_9)
    
    created_by= models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.job.title