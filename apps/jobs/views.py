from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Job
from .forms import AddJobForm, ApplicationForm

from apps.notifications.utulities import create_notification


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
def edit_job(request, job_id):
    job = Job.objects.get(pk=job_id, created_by=request.user)
    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)
        
        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()
            
            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)
    
    return render(request, 'edit_job.html', {'form':form, 'job':job})

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
            
            create_notification(request, job.created_by, 'application', extra_id=application.id)
            
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    
    return render(request, 'apply.html', {'form':form, 'job':job})


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        company_name = request.POST.get('company_name')
        company_location = request.POST.get('company_location')
        company_size = request.POST.get('company_size')

        return HttpResponseRedirect(reverse('api_search') + f'?query={query}&company_name={company_name}&company_location={company_location}&company_size={company_size}')

    return render(request, 'search.html')
