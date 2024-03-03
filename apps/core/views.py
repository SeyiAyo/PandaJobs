from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.userprofile.models import UserProfile

from apps.jobs.models import Job

def frontpage(request):
    jobs = Job.objects.all()[0:10]
    
    
    return render(request, 'frontpage.html', {'jobs':jobs})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            
            account_type = request.POST.get('account_type', 'jobseeker')
            
            if account_type == 'employer':
                userprofile = UserProfile.objects.create(user=user, is_employer=True) 
                user.userprofile.save()
            else:
                userprofile = UserProfile.objects.create(user=user)
                userprofile.save()
            
            login(request, user)
            
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form':form})