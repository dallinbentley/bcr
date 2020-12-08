from django.shortcuts import render, HttpResponse
from .models import JobListing, JobType, Skill, QuickApply
from accounts.models import Employer, Applicant

# Create your views here.
def indexPageView(request):
    return render(request, 'jobs/index.html')

def applicantHomepageView(request, applicantID):
    applicant = Applicant.objects.get(id=applicantID)
    context = {
        'applicantID':applicantID,
        'applicant': applicant
    }
    return render(request, 'jobs/applicant-homepage.html', context)

def employerHomepageView(request):
    return render(request, 'jobs/employer-homepage.html')

def applicantUpdatePageView(request, applicantID):

    applicant = Applicant.objects.get(id=applicantID)
    skills = Skill.objects.all()

    context = {
        'applicant': applicant,
        'applicantID': applicantID,
        'skills': skills
    }

    return render(request, 'jobs/view-account-applicant.html', context)

def applicantUpdate(request, applicantID):
    if request.method == 'POST':
        update_applicant = Applicant.objects.get(id=applicantID)

        update_applicant.first_name = request.POST.get('firstname')
        update_applicant.last_name = request.POST.get('lastname')
        update_applicant.birthdate = request.POST.get('birthdate')
        update_applicant.email = request.POST.get('email')
        update_applicant.phone = request.POST.get('phone')

        update_applicant.resume = request.FILES['resume']
        update_skill1 = Skill.objects.get(skill_description=request.POST.get('skill1'))
        update_skill2 = Skill.objects.get(skill_description=request.POST.get('skill2'))
        update_skill3 = Skill.objects.get(skill_description=request.POST.get('skill3'))
        update_skill4 = Skill.objects.get(skill_description=request.POST.get('skill4'))
        update_skill5 = Skill.objects.get(skill_description=request.POST.get('skill5'))
        
        update_applicant.skill_1 = update_skill1
        update_applicant.skill_2 = update_skill2
        update_applicant.skill_3 = update_skill3
        update_applicant.skill_4 = update_skill4
        update_applicant.skill_5 = update_skill5

        update_applicant.save()

        context = {
        'applicant': update_applicant,
        'applicantID': applicantID
        }

        return render(request, 'jobs/applicant-homepage.html', context)

def jobinfoPageView(request, jobID, applicantID):
    currentjob = JobListing.objects.get(id=jobID)
    context={
        'Job':currentjob,
        'applicantID':applicantID,
        'message': ''
    }

    return render(request, 'jobs/jobinfo.html', context)

def availableJobsPageView(request, applicantID):
    data = JobListing.objects.all()
    context={
        'jobs': data,
        'applicantID': applicantID
    }
    return render(request, 'jobs/jobs.html', context)

def addJobListingPageView(request, employerID):
    context={
        'employerID': employerID
    }
    return render(request, 'jobs/addjoblisting.html', context)

def addjobFunc(request, employerID):
    if request.method == 'Post':
        new_JobListing = JobListing()

        new_company = JobListing.objects.get(company_ID=employerID)
        new_JobListing.company_ID = new_company
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

def employersListPageView(request, applicantID):
    data = Employer.objects.all()
    context = {
        'employerlist': data,
        'applicantID': applicantID
    }
    return render(request, 'jobs/employerslist.html', context)

def searchJobs(request, applicantID):
    searchString = request.GET['searchbar']
    data = JobListing.objects.filter(job_title=searchString)

    if data.count() > 0:
        context = {
            "search_jobs" : data,
            "applicantID": applicantID
        }
        return render(request, 'jobs/searchresultsjobs.html', context)
    else:
        return HttpResponse("Not found")

def searchEmployers(request):
    searchString = request.GET['searchbar2']
    data = Employer.objects.filter(company_name=searchString)

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


def quickApply(request,jobID, applicantID):
    new_quickApply = QuickApply()

    applicant = Applicant.objects.get(id=applicantID)
    joblisting = JobListing.objects.get(id=jobID)
    matching_skills = 0

    if applicant.skill_1 == joblisting.preferred_skill1 or applicant.skill_1 == joblisting.preferred_skill2 or applicant.skill_1 == joblisting.preferred_skill3:
        matching_skills += 1

    if  applicant.skill_2 == joblisting.preferred_skill1 or applicant.skill_2 == joblisting.preferred_skill2 or applicant.skill_2 == joblisting.preferred_skill3:
        matching_skills += 1

    if  applicant.skill_3 == joblisting.preferred_skill1 or applicant.skill_3 == joblisting.preferred_skill2 or applicant.skill_3 == joblisting.preferred_skill3:
        matching_skills += 1

    if  applicant.skill_4 == joblisting.preferred_skill1 or applicant.skill_4 == joblisting.preferred_skill2 or applicant.skill_4 == joblisting.preferred_skill3:
        matching_skills += 1

    if  applicant.skill_5 == joblisting.preferred_skill1 or applicant.skill_5 == joblisting.preferred_skill2 or applicant.skill_5 == joblisting.preferred_skill3:
        matching_skills += 1

    new_quickApply.matching_skills = matching_skills
    new_quickApply.applicant = applicant
    new_quickApply.job_listing = joblisting

    new_quickApply.save()

    context={
        'Job':joblisting,
        'applicantID':applicantID,
        'message': 'You Have Successfully Applied!'
    }

    return render(request, 'jobs/jobinfo.html', context)


def applicationsPageView(request, joblisting_id):
    return render(request, 'accounts/applications.html', context)

