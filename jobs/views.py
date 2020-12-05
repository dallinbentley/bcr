from django.shortcuts import render

# Create your views here.
def homepageView(request):
    return render(request, 'jobs/homepage.html')

def jobinfoPageView(request):
    return render(request, 'jobs/jobinfo.html')


def availableJobsPageView(request):
    return render(request, 'jobs/jobs.html')