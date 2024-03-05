from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.jobs.models import JobApplication, Job
from .models import Message

from apps.notifications.utulities import create_notification


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'userprofile':request.user.userprofile})

@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = JobApplication.objects.get(pk=application_id, job__created_by=request.user)
    else:
        application = JobApplication.objects.get(pk=application_id, created_by=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')
        
        if content:
            message = Message.objects.create(application=application, content=content, created_by=request.user)
            
            create_notification(request, application.created_by, 'message', extra_id=application.id)
            
            return redirect('view_application', application_id=application.id)
    return render(request, 'view_application.html', {'application':application})

@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    return render(request, 'view_dashboard_job.html', {'job':job})