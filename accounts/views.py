from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from .models import Applicant, Employer
from jobs.models import Skill, JobListing

# Create your views here.

def signupApplicantPageView(request):
    skills = Skill.objects.all()
    context = {
        'skills':skills
    }
    return render(request, 'accounts/signup-applicant.html', context)

def signupApplicant(request):   
    if request.method == 'POST':
        new_applicant = Applicant()

        new_applicant.username = request.POST.get('username')
        new_applicant.password = request.POST.get('psw')
        new_applicant.first_name = request.POST.get('firstname')
        new_applicant.last_name = request.POST.get('lastname')
        new_applicant.birthdate = request.POST.get('birthdate')
        new_applicant.email = request.POST.get('email')
        new_applicant.phone = request.POST.get('phone')

        new_applicant.resume = request.FILES['resume']
        new_skill1 = Skill.objects.get(skill_description=request.POST.get('skill1'))
        new_skill2 = Skill.objects.get(skill_description=request.POST.get('skill2'))
        new_skill3 = Skill.objects.get(skill_description=request.POST.get('skill3'))
        new_skill4 = Skill.objects.get(skill_description=request.POST.get('skill4'))
        new_skill5 = Skill.objects.get(skill_description=request.POST.get('skill5'))
        
        new_applicant.skill_1 = new_skill1
        new_applicant.skill_2 = new_skill2
        new_applicant.skill_3 = new_skill3
        new_applicant.skill_4 = new_skill4
        new_applicant.skill_5 = new_skill5

        new_applicant.save()

        applicantID = new_applicant.id
        
        context = {
        'applicant': new_applicant,
        'applicantID': applicantID
        }
        return render(request, 'jobs/applicant-homepage.html', context)
    
def signupEmployerPageView(request):
    return render(request, 'accounts/signup-employer.html')
    
def signupEmployer(request):
    if request.method == 'POST':
        new_emp = Employer()
        
        new_emp.username = request.POST.get('username')
        new_emp.password = request.POST.get('psw')
        new_emp.company_name = request.POST.get('company_name')
        new_emp.company_email = request.POST.get('email')
        new_emp.company_address = request.POST.get('address')
        new_emp.city = request.POST.get('city')
        new_emp.state = request.POST.get('company_state')
        new_emp.zip = request.POST.get('zip')
        new_emp.url = request.POST.get('url')
        new_emp.company_image = request.FILES['image']


        new_emp.save()

        context = {
        'employer' : new_emp
        }

    return render(request, 'jobs/employer-homepage.html', context)

def deleteAccountPageView(request):
    return render(request, 'accounts/delete-account.html')

def viewAccountApplicantPageView(request):
    return render(request, 'accounts/view-account-applicant.html')

def viewAccountEmployerPageView(request):
    return render(request, 'accounts/view-account-employer.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")
    


def login_request(request):
    username= request.POST.get('username')
    password= request.POST.get('psw')

    try:
        applicant = Applicant.objects.get(username=username, password=password)
        applicantid = applicant.id

        context = {
            'applicantID': applicantid,
            'applicant': applicant
        }

        return render(request, 'jobs/applicant-homepage.html',context)

    except:
        applicant=None 

    if  applicant==None :
        try:
            employer = Employer.objects.get(username=username, password=password)
            employerID = employer.id
            context = {
                'employer': employer,
                'employerID': employerID
            }

            return render(request, 'jobs/employer-homepage.html',context)
    
        except:
            employer=None
    
    if applicant==None and employer== None :
        context={
            'message': 'Either your username or password was entered incorrectly.'
        }
        return render(request, 'accounts/login.html', context)
   
def loginPageView(request):
    context={
        'message':''
    }
    return render(request, 'accounts/login.html', context)

def deleteAccount(request, employerID):
    Employer.objects.get(id=employerID).delete()

    JobListing.objects.filter(id=employerID).delete()

    return render(request, 'jobs/index.html')
