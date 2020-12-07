from django.shortcuts import render, HttpResponse
from .models import JobListing, JobType, Skill
from accounts.models import Employer

# Create your views here.
def indexPageView(request):
    return render(request, 'jobs/index.html')

def applicantHomepageView(request):
    return render(request, 'jobs/applicant-homepage.html')

def employerHomepageView(request):
    return render(request, 'jobs/employer-homepage.html')

def jobinfoPageView(request, jobID, applicantID):
    currentjob = JobListing.objects.get(id=jobID)
    context={
        'Job':currentjob,
        'applicantID':applicantID
    }

    return render(request, 'jobs/jobinfo.html', context)

def availableJobsPageView(request, applicantID):
    data = JobListing.objects.all()
    context={
        'jobs': data,
        'applicantID': applicantID
    }
    return render(request, 'jobs/jobs.html', context)

def addJobListingPageView(request):
    return render(request, 'jobs/addjoblisting.html')

def addjobFunc(request):
    if request.method == 'Post':
        new_JobListing = JobListing()

        new_JobListing.job_title = request.POST.get('jobtitle')
        new_jobtype = JobType.objects.get(job_type_description=request.POST.get('jobtype'))
        new_JobListing.wage= request.POST.get('wage')
        new_JobListing.salary = request.POST.get('salary')
        new_JobListing.job_description = request.POST.get('jobdescription')
        new_skill1 = Skill.objects.get(skill_description=request.POST.get('preferredskill1'))
        new_skill2 = Skill.objects.get(skill_description=request.POST.get('preferredskill2'))
        new_skill3 = Skill.objects.get(skill_description=request.POST.get('preferredskill3'))

        new_JobListing.job_type = new_jobtype
        new_JobListing.preferred_skill1 = new_skill1
        new_JobListing.preferred_skill2 = new_skill2
        new_JobListing.preferred_skill3 = new_skill3
        
        new_JobListing.save()

def updateJobListingPageView(request, jobID):
    return render(request, 'jobs/updatejoblisting.html')

def updateJobListing(request, jobID):
    updated_JobListing = JobListing.object.get(id=jobID)

    updated_JobListing.job_title = request.POST.get('jobtitle')
    updated_jobtype = JobType.objects.get(job_type_description=request.POST.get('jobtype'))
    updated_JobListing.wage= request.POST.get('wage')
    updated_JobListing.salary = request.POST.get('salary')
    updated_JobListing.job_description = request.POST.get('jobdescription')
    updated_skill1 = Skill.objects.get(skill_description=request.POST.get('preferredskill1'))
    updated_skill2 = Skill.objects.get(skill_description=request.POST.get('preferredskill2'))
    updated_skill3 = Skill.objects.get(skill_description=request.POST.get('preferredskill3'))

    updated_JobListing.job_type = updated_jobtype
    updated_JobListing.preferred_skill1 = updated_skill1
    updated_JobListing.preferred_skill2 = updated_skill2
    updated_JobListing.preferred_skill3 = updated_skill3
    
    updated_JobListing.save()
    return render(request, 'jobs/jobinfo.html')

def employersListPageView(request):
    return render(request, 'jobs/employerslist.html')

def searchJobs(request):
    searchString = request.GET['searchbar'].lower()
    data = JobListing.objects.filter(job_title=searchString).lower()

    if data.count() > 0:
        context = {
            "search_jobs" : data
        }
        return render(request, 'jobs/searchresultsjobs.html', context)
    else:
        return HttpResponse("Not found")

def searchEmployers(request):
    searchString = request.GET['searchbar2'].lower()
    data = Employer.objects.filter(company_name=searchString).lower()

    if data.count() > 0:
        context = {
            "search_employers" : data
        }
        return render(request, 'jobs/searchresultsemployers.html', context)
    else:
        return HttpResponse("Not found")

def deleteJobListing(request, jobID):
    JobListing.objects.get(id=jobID).delete() 
    data = Game.objects.all()

    context = {
        "our_jobs" : data
    }

    return render(request, 'jobs.jobs.html', context)


