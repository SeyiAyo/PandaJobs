import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from .models import Job
from .external_api import JobSearchAPI

@csrf_exempt
def api_search(request):
    query = request.GET.get('query', '')
    location = request.GET.get('location', '')
    source = request.GET.get('source', 'local')  # 'local' or 'external'
    page = int(request.GET.get('page', '1'))
    
    if source == 'external':
        # Use external API
        api = JobSearchAPI()
        results = api.search_jobs(query, location, page)
        
        if 'error' in results:
            return JsonResponse({'error': results['error']}, status=400)
            
        # Transform the external API response to match our format
        jobs = []
        for job in results.get('data', []):
            jobs.append({
                'id': job.get('id'),
                'title': job.get('title'),
                'company_name': job.get('company_name'),
                'company_location': job.get('company_location'),
                'description': job.get('description'),
                'url': job.get('url'),
                'source': 'external',
                'job_type': job.get('job_type', ''),
                'posted_at': job.get('posted_at', ''),
                'salary': job.get('salary', '')
            })
            
        return JsonResponse({
            'jobs': jobs,
            'has_next': len(jobs) >= 10  # JSearch returns 10 results per page
        })
    
    else:
        # Use local database
        jobs_query = Job.objects.filter(status=Job.OPEN)
        
        if query:
            jobs_query = jobs_query.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(company_name__icontains=query)
            )
            
        if location:
            jobs_query = jobs_query.filter(
                Q(company_location__icontains=location)
            )
            
        # Order by most recent
        jobs_query = jobs_query.order_by('-created_at')
        
        # Paginate results
        start = (page - 1) * 10
        end = start + 10
        jobs_page = jobs_query[start:end]
        
        jobs = [{
            'id': job.id,
            'title': job.title,
            'company_name': job.company_name,
            'company_location': job.company_location,
            'description': job.description,
            'url': f'/jobs/{job.id}/',
            'source': 'local'
        } for job in jobs_page]
        
        return JsonResponse({
            'jobs': jobs,
            'has_next': jobs_query.count() > end
        })
