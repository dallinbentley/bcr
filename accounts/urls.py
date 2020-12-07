from django.urls import path
from .views import login_request, logout_request, signupApplicantPageView, signupEmployerPageView, applicationsPageView, deleteAccountPageView, viewAccountApplicantPageView, viewAccountEmployerPageView, loginPageView, signupEmployer


urlpatterns = [
    path("logout", logout_request, name="logout"),
    path("login", login_request, name="login"),
    path("userlogin", loginPageView, name="userlogin"),
    path("register-applicant/", signupApplicantPageView, name="register-applicant"),
    path("register-employer/", signupEmployerPageView, name="register-employer"),
    path("registered-employer", signupEmployer, name="registered-employer"),
    path("applications/", applicationsPageView, name="applications"),
    path("delete/", deleteAccountPageView, name="delete"),
    path("view-applicant/", viewAccountApplicantPageView, name="view-applicant"),
    path("view-employer/", viewAccountEmployerPageView, name="view-employer"),
]