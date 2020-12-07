from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from .models import Applicant, Employer
from jobs.models import Skill

# Create your views here.
def testview(request):
    print('this is a test.')
    return('the test worked')

def applicationsPageView(request):
    return render(request, 'accounts/applications.html')

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
        new_applicant.password = request.POST.get('password')
        new_applicant.first_name = request.POST.get('firstname')
        new_applicant.last_name = request.POST.get('lastname')
        new_applicant.birthdate = request.POST.get('birthdate')
        new_applicant.email = request.POST.get('email')
        new_applicant.phone = request.POST.get('phone')

        new_applicant.resume = request.FILES['resume']

        new_applicant.skill_1 = Skill.objects.get(request.POST.get('skill1'))
        new_applicant.skill_2 = Skill.objects.get(request.POST.get('skill2'))
        new_applicant.skill_3 = Skill.objects.get(request.POST.get('skill3'))
        new_applicant.skill_4 = Skill.objects.get(request.POST.get('skill4'))
        new_applicant.skill_5 = Skill.objects.get(request.POST.get('skill5'))

        new_applicant.save()

        context = {
        'applicant': new_applicant
        }
    return render(request, 'jobs/applicant-homepage.html', context)
    
def signupEmployerPageView(request):
    return render(request, 'accounts/signup-employer.html')
    
def signupEmployer(request):
    if request.method == 'POST':
        new_emp = Employer()
        
        new_emp.username = request.GET['username']
        new_emp.password = request.GET['psw']
        new_emp.company_name = request.GET['company_name']
        new_emp.company_email = request.GET['email']
        new_emp.company_address = request.GET['address']
        new_emp.city = request.GET['city']
        new_emp.state = request.GET['company_state']
        new_emp.zip = request.GET['zip']
        new_emp.url = request.GET['url']
        new_emp.image = request.FILES['image']


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

        context = {
            'applicant': applicant
        }

        return render(request, 'jobs/applicant-homepage.html',context)

    except:
        applicant=None 

    if  applicant==None :
        try:
            employer = Employer.objects.get(username=username, password=password)

            context = {
                'employer': employer
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
