from django.contrib import admin
from .models import Job, JobApplication


admin.site.register(Job)
admin.site.register(JobApplication)


admin.site.site_header = 'Jobs Admin'


