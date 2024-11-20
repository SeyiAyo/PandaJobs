from django.urls import path
from .views import job_detail, add_job, edit_job, apply, search, job_list
from .api import api_search


urlpatterns = [
    path('', job_list, name='job_list'),
    path('api/search/', api_search, name='api_search'),  # Changed to match frontend expectation
    path('search/', search, name='search'),
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('add/', add_job, name='add_job'),
    path('<int:job_id>/edit/', edit_job, name='edit_job'),
    path('<int:job_id>/apply/', apply, name='apply'),
]
