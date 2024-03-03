from django.contrib.auth.models import User
from django.db import models
from apps.jobs.models import JobApplication

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Message(models.Model):
    application = models.ForeignKey(JobApplication, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    
    created_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']