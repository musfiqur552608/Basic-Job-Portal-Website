from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application
from .forms import JobForm, ApplicationForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_details.html', {'job': job})


def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_post.html', {'form': form})

def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('job_details', job_id)
        else:
            print(form.errors)
    else:
        form = ApplicationForm()
    return render(request, 'apply_job.html', {'form': form, 'job': job})
