import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse

from .models import Job

@csrf_exempt
def api_search(request):
    """API endpoint for searching jobs with various filters."""
    jobslist = []
    try:
        # Get search parameters from request
        if request.method == 'GET':
            params = request.GET
        elif request.method == 'POST':
            try:
                if request.body:
                    params = json.loads(request.body)
                else:
                    params = request.POST
            except json.JSONDecodeError as e:
                return JsonResponse({
                    'error': 'Invalid JSON data',
                    'details': str(e)
                }, status=400)
        else:
            return JsonResponse({
                'error': f'Method {request.method} not allowed',
                'allowed_methods': ['GET', 'POST']
            }, status=405)

        # Extract search parameters
        query = params.get('query', '').strip()
        company_name = params.get('company_name', '').strip()
        company_location = params.get('company_location', '').strip()
        company_country = params.get('company_country', '').strip()
        company_size = params.get('company_size', '').strip()

        # Build the query
        jobs = Job.objects.filter(status=Job.OPEN)
        
        if query:
            jobs = jobs.filter(
                Q(title__icontains=query) | 
                Q(full_description__icontains=query) | 
                Q(company_name__icontains=query)
            )

        if company_name:
            jobs = jobs.filter(company_name__icontains=company_name)

        if company_location:
            jobs = jobs.filter(company_location__icontains=company_location)
            
        if company_country:
            jobs = jobs.filter(company_country=company_country)

        if company_size:
            jobs = jobs.filter(company_size=company_size)

        # Order by most recent
        jobs = jobs.order_by('-created_at')

        # Build response data
        for job in jobs:
            job_url = reverse('job_detail', kwargs={'job_id': job.id})
            jobslist.append({
                'id': job.id,
                'title': job.title,
                'summary': job.summary,
                'company_name': job.company_name,
                'company_location': job.company_location or '',
                'company_country': str(job.company_country),
                'company_size': job.company_size,
                'company_size_display': job.get_company_size_display(),
                'work_type': job.work_type,
                'work_type_display': job.get_work_type_display(),
                'salary_min': float(job.salary_min) if job.salary_min else None,
                'salary_max': float(job.salary_max) if job.salary_max else None,
                'created_at': job.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'status': job.status,
                'status_display': job.get_status_display(),
                'url': job_url  # Add the job detail URL
            })
        
        return JsonResponse({
            'count': len(jobslist),
            'jobs': jobslist
        })
    except Exception as e:
        return JsonResponse({
            'error': 'An error occurred while processing your request',
            'details': str(e)
        }, status=400)
