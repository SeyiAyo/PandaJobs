import os
import requests
from django.conf import settings

class JobSearchAPI:
    """Class to handle interactions with the JSearch API from RapidAPI"""
    
    def __init__(self):
        self.api_key = os.getenv('RAPIDAPI_KEY')
        self.base_url = "https://jsearch.p.rapidapi.com"
        
    def search_jobs(self, query, location=None, page=1):
        """
        Search for jobs using the JSearch API
        
        Args:
            query (str): Search query (e.g. "python developer")
            location (str, optional): Location to search in (e.g. "London, UK")
            page (int, optional): Page number for pagination
            
        Returns:
            dict: API response containing job listings
        """
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }
        
        params = {
            "query": f"{query} {location if location else ''}".strip(),
            "page": str(page),
            "num_pages": "1"
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/search",
                headers=headers,
                params=params
            )
            response.raise_for_status()
            data = response.json()
            
            # Transform the response to match our local job format
            jobs = []
            for job in data.get('data', []):
                transformed_job = {
                    'id': job.get('job_id'),
                    'title': job.get('job_title'),
                    'company_name': job.get('employer_name'),
                    'company_location': job.get('job_city'),
                    'description': job.get('job_description'),
                    'job_type': job.get('job_employment_type'),
                    'salary': job.get('job_salary_period'),
                    'url': job.get('job_apply_link'),
                    'source': 'external',
                    'posted_date': job.get('job_posted_at_datetime_utc'),
                }
                jobs.append(transformed_job)
                
            return {
                'jobs': jobs,
                'has_next': len(data.get('data', [])) == int(params['num_pages'])
            }
            
        except requests.RequestException as e:
            print(f"Error fetching jobs from external API: {str(e)}")
            return {
                'jobs': [],
                'has_next': False,
                'error': 'Failed to fetch external jobs'
            }
