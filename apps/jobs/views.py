from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Job, JobApplication
from .forms import AddJobForm, ApplicationForm

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    
    return render(request, 'job_detail.html', {'job':job})


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            
            return redirect('dashboard')
    else:
        form = AddJobForm()
    
    return render(request, 'add_job.html', {'form':form})


@login_required
def apply(request, job_id):
    job = Job.objects.get(pk=job_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()
            
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    
    return render(request, 'apply.html', {'form':form, 'job':job})