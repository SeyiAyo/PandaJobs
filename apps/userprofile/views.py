from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.jobs.models import JobApplication, Job

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'userprofile':request.user.userprofile})

@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = JobApplication.objects.get(pk=application_id, job__created_by=request.user)
    else:
        application = JobApplication.objects.get(pk=application_id, created_by=request.user)

    return render(request, 'view_application.html', {'application':application})

@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    return render(request, 'view_dashboard_job.html', {'job':job})