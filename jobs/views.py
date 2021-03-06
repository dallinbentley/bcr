from django.shortcuts import render, HttpResponse
from .models import JobListing, JobType, Skill, QuickApply
from accounts.models import Employer, Applicant

# Create your views here.
def similarJobsRecommender(jobTitle):
    #related job titles API
    import urllib
    # If you are using Python 3+, import urllib instead of urllib2

    import json 

    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["job_title"],
                        "Values": [ [ jobTitle ] ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/e9081862165e486e8849e3770b43317e/services/8b6c1c8061824bf2a0dc1e619725bed3/execute?api-version=2.0&details=true'
    api_key = '+zgVRAbU1B90gvAdMfjlydmCq3tVwZpg3loUdN9QrxF0uzOJutZBZLGJs+RH3xICo13tqSRGT75tnpWTkRKzXA=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)

    jobs = result['Results']['output1']['value']['Values'][0]

    return jobs
               

def indexPageView(request):
    return render(request, 'jobs/index.html')

def applicantHomepageView(request, applicantID):
    applicant = Applicant.objects.get(id=applicantID)
    context = {
        'applicantID':applicantID,
        'applicant': applicant
    }
    return render(request, 'jobs/applicant-homepage.html', context)

def employerHomepageView(request, employerID):
    employer = Employer.objects.get(id=employerID)
    context = {
        'employerID': employerID,
        'employer': employer
    }
    return render(request, 'jobs/employer-homepage.html', context)

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
    applicant = Applicant.objects.get(id=applicantID)
    joblisting = JobListing.objects.get(id=jobID)
    matching_skills = 0

    if joblisting.preferred_skill1 == applicant.skill_1 or joblisting.preferred_skill1 == applicant.skill_2 or joblisting.preferred_skill1 == applicant.skill_3 or joblisting.preferred_skill1 == applicant.skill_4 or joblisting.preferred_skill1 == applicant.skill_5:
        matching_skills += 1

    if joblisting.preferred_skill2 == applicant.skill_1 or joblisting.preferred_skill2 == applicant.skill_2 or joblisting.preferred_skill2 == applicant.skill_3 or joblisting.preferred_skill2 == applicant.skill_4 or joblisting.preferred_skill2 == applicant.skill_5:
        matching_skills += 1

    if joblisting.preferred_skill3 == applicant.skill_1 or joblisting.preferred_skill3 == applicant.skill_2 or joblisting.preferred_skill3 == applicant.skill_3 or joblisting.preferred_skill3 == applicant.skill_4 or joblisting.preferred_skill3 == applicant.skill_5:
        matching_skills += 1

    jobs = similarJobsRecommender(joblisting.job_title)

    context={
        'Job':joblisting,
        'applicantID':applicantID,
        'message': '',
        'matching_skills': matching_skills,
        'jobs': jobs
    }

    return render(request, 'jobs/jobinfo.html', context)

def empinfoPageView(request, applicantID, employerID):
    emp = Employer.objects.get(id=employerID)

    context = {
        'Employer' : emp,
        'applicantID' : applicantID,
        'message' : ''
    }

    return render(request, 'jobs/empinfo.html', context)

def availableJobsPageView(request, applicantID):
    data = JobListing.objects.all()
    context={
        'jobs': data,
        'applicantID': applicantID
    }
    return render(request, 'jobs/jobs.html', context)

def addJobListingPageView(request, employerID):
    skills = Skill.objects.all()
    jobtypes = JobType.objects.all()
    context={
        'employerID': employerID,
        'skills': skills,
        'jobtypes': jobtypes
    }
    return render(request, 'jobs/addjoblisting.html', context)

def addjobFunc(request, employerID):
    if request.method == 'POST':
        new_JobListing = JobListing()

        new_company = Employer.objects.get(id= employerID)
        new_JobListing.company_ID = new_company
        new_JobListing.job_title = request.POST.get('jobtitle')
        new_jobtype = JobType.objects.get(job_type_description=request.POST.get('jobtype'))
        if request.POST.get('wage') == '':
            new_JobListing.wage = None
        else:
            new_JobListing.wage= request.POST.get('wage')
        if request.POST.get('salary') == '':
            new_JobListing.salary = None   
        else:
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

        employer = Employer.objects.get(id=employerID)
        context = {
        'employerID': employerID,
        'employer': employer
        }

        return render(request, 'jobs/employer-homepage.html', context)

def updateJobListingPageView(request, employerID, listingID):
    listing = JobListing.objects.get(id=listingID)
    skills = Skill.objects.all()
    jobtypes = JobType.objects.all()

    context = {
        'employerID':employerID,
        'listing':listing,
        'listingID':listingID,
        'skills':skills,
        'jobtypes':jobtypes
    }
    return render(request, 'jobs/updatejoblisting.html', context)

def updateJobListing(request, listingID, employerID):
    if request.method =='POST':
        updated_JobListing = JobListing.objects.get(id=listingID)

        updated_JobListing.job_title = request.POST.get('jobtitle')
        updated_jobtype = JobType.objects.get(job_type_description=request.POST.get('jobtype'))
        if request.POST.get('wage') == '':
            updated_JobListing.wage = None
        else:
            updated_JobListing.wage= request.POST.get('wage')
        if request.POST.get('salary') == '':
            updated_JobListing.salary = None   
        else:
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

        context = {
            'listingID':listingID,
            'employerID':employerID
        }
        return render(request, 'jobs/mylistings.html', context)

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

def searchsimilarjobs(request, applicantID, jobtitle):
    data = JobListing.objects.filter(job_title = jobtitle )

    if data.count() > 0:
        context = {
            "search_jobs" : data,
            "applicantID": applicantID
        }
        return render(request, 'jobs/searchresultsjobs.html', context)
    else:
        return HttpResponse("Not found")

def searchEmployers(request, applicantID):
    searchString = request.GET['searchbar2']
    data = Employer.objects.filter(company_name=searchString)

    if data.count() > 0:
        context = {
            "search_employers" : data,
            "applicantID" : applicantID
        }
        return render(request, 'jobs/searchresultsemployers.html', context)
    else:
        return HttpResponse("Not found")

def deleteJobListing(request, employerID, jobID):
    JobListing.objects.get(id=jobID).delete() 
    data = JobListing.objects.filter(company_ID=employerID)
    employer = Employer.objects.get(id=employerID)

    context = {
        "our_jobs" : data,
        "employer" : employer,
        "employerID" : employerID
    }

    return render(request, 'jobs/employer-homepage.html', context)


def quickApply(request,jobID, applicantID):
    new_quickApply = QuickApply()

    applicant = Applicant.objects.get(id=applicantID)
    joblisting = JobListing.objects.get(id=jobID)
    matching_skills = 0

    if joblisting.preferred_skill1 == applicant.skill_1 or joblisting.preferred_skill1 == applicant.skill_2 or joblisting.preferred_skill1 == applicant.skill_3 or joblisting.preferred_skill1 == applicant.skill_4 or joblisting.preferred_skill1 == applicant.skill_5:
        matching_skills += 1

    if joblisting.preferred_skill2 == applicant.skill_1 or joblisting.preferred_skill2 == applicant.skill_2 or joblisting.preferred_skill2 == applicant.skill_3 or joblisting.preferred_skill2 == applicant.skill_4 or joblisting.preferred_skill2 == applicant.skill_5:
        matching_skills += 1

    if joblisting.preferred_skill3 == applicant.skill_1 or joblisting.preferred_skill3 == applicant.skill_2 or joblisting.preferred_skill3 == applicant.skill_3 or joblisting.preferred_skill3 == applicant.skill_4 or joblisting.preferred_skill3 == applicant.skill_5:
        matching_skills += 1

    jobs = similarJobsRecommender(joblisting.job_title)

    new_quickApply.matching_skills = matching_skills
    new_quickApply.applicant = applicant
    new_quickApply.job_listing = joblisting

    new_quickApply.save()

    context={
        'Job':joblisting,
        'applicantID':applicantID,
        'message': 'You Have Successfully Applied!',
        'matching_skills': matching_skills,
        'jobs': jobs
    }

    return render(request, 'jobs/jobinfo.html', context)


def myListingPageView(request, employerID):
    joblistings = JobListing.objects.filter(company_ID=employerID)

    context={
        'joblistings': joblistings,
        'employerID': employerID
    }
    return render(request, 'jobs/mylistings.html', context)


def viewAccountEmployerPageView(request, employerID):
    employer = Employer.objects.get(id=employerID)

    context = {
        'employer':employer,
        'employerID':employerID
    }
    
    return render(request, 'jobs/view-account-employer.html', context)


def employerUpdate(request, employerID):
    if request.method == 'POST':
        update_employer = Employer.objects.get(id=employerID)

        update_employer.company_name = request.POST.get('companyname')
        update_employer.company_address = request.POST.get('companyaddress')
        update_employer.company_city = request.POST.get('companycity')
        update_employer.company_state = request.POST.get('companystate')
        update_employer.company_zip = request.POST.get('companyzip')
        update_employer.company_zip = request.POST.get('companyzip')
        update_employer.company_url = request.POST.get('companyurl')
        update_employer.company_email = request.POST.get('companyemail')

        update_employer.company_image = request.FILES['image']

        update_employer.save()

        context = {
        'employer': update_employer,
        'employerID': employerID
        }

        return render(request, 'jobs/employer-homepage.html', context)

def applicationsPageView(request, employerID, listingID):
    employer = Employer.objects.get(id=employerID)
    listing = JobListing.objects.get(id=listingID)
    data = JobListing.objects.filter(id=listing.id)
    quick_apply = QuickApply.objects.filter(job_listing=listingID)
    context = {
        'quick_apply' : quick_apply,
        'listing' : data,
        'employerID' : employer.id
    }

    return render(request, 'jobs/applications.html', context)

def similarApplicantsRecommender(request, employerID, applicantID):
    #related users API
    import urllib
    # If you are using Python 3+, import urllib instead of urllib2

    import json 


    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["user_id"],
                        "Values": [ [ applicantID ] ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/e9081862165e486e8849e3770b43317e/services/3b41cd315ba747a2bc96e95390c1b54e/execute?api-version=2.0&details=true'
    api_key = '/MxCFxk0v1A4dPp2+X2+Cy8KMW4WY2zfsRFyLBSyXW5kqMvhbAL2Vyo3xR8kk/1YGQMmUqpCX0H+J2Unnwiryw=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)

    users = result['Results']['output1']['value']['Values'][0]

    liUsers=[]

    for user in users:
        user = int(user)
        applicant = Applicant.objects.get(id=user)
        liUsers.append(applicant)


    context = {
        'users':liUsers,
        'employerID':employerID
    }

    return render(request, 'jobs/similar-applicants.html', context)