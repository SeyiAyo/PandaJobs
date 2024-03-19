from django.urls import path
from .views import job_detail, add_job, apply, search
from .api import api_search


urlpatterns = [
    path('search/api/', api_search, name='api_search'),
    path('search/', search, name='search'),
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('add/', add_job, name='add_job'),
    path('<int:job_id>/apply/', apply, name='apply'),
]
