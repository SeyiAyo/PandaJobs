from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Job
from .forms import AddJobForm, ApplicationForm
from django_countries import countries

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
    
    return render(request, 'add_job.html', {'form':form, 'countries':countries})

@login_required
def edit_job(request, job_id):
    job = Job.objects.get(pk=job_id, created_by=request.user)
    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)
        
        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.company_name = request.POST.get('company_name')
            job.save()
            
            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)
    
    return render(request, 'edit_job.html', {'form':form, 'job':job, 'countries':countries})

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

def job_list(request):
    """View function for listing all jobs with search and filtering."""
    jobs = Job.objects.filter(status=Job.OPEN).order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def search(request):
    """Handle both GET and POST requests for job search."""
    if request.method in ['GET', 'POST']:
        # Get parameters from either GET or POST
        query = request.GET.get('query') or request.POST.get('query')
        company_name = request.GET.get('company_name') or request.POST.get('company_name')
        company_location = request.GET.get('company_location') or request.POST.get('company_location')
        company_size = request.GET.get('company_size') or request.POST.get('company_size')

        # If any search parameters are provided, redirect to API search
        if any([query, company_name, company_location, company_size]):
            return HttpResponseRedirect(reverse('api_search') + 
                f'?query={query or ""}&company_name={company_name or ""}&company_location={company_location or ""}&company_size={company_size or ""}')

    # If no search parameters or initial page load, render the search form
    return render(request, 'search.html', {'countries':countries})
