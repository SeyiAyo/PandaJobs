import json

from django.db.models import Q
from django.http import JsonResponse

from .models import Job

def api_search(request):
    jobslist = []
    data = json.loads(request.body)
    query = data['query']
    company_name = data['company_name']
    company_location = data['company_location']
    company_size = data['company_size']

    jobs = Job.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query) | Q(company_name__icontains=query) | Q(company_location__icontains=query) | Q(company_size__icontains=query))

    if company_name:
        jobs = jobs.filter(company_name=company_name)

    if company_location:
        jobs = jobs.filter(company_location=company_location)

    if company_size:
        jobs = jobs.filter(company_size=company_size)

    for job in jobs:
        obj = {
            'id': job.id,
            'title': job.title,
            'summary': job.summary,
            'company_name': job.company_name,
            'url': '/jobs/%s' % job.id
        }
        jobslist.append(obj)
        
    return JsonResponse({'jobs': jobslist})