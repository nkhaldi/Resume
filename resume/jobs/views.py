from django.shortcuts import render
from .models import Job


def jobs(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}

    return render(request, 'jobs/jobs.html', context)


def job(request, pk):
    jobObj = Job.objects.get(id=pk)

    return render(request, 'jobs/single-job.html', {'job': jobObj})
