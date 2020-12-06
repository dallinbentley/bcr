from django.urls import path
from .views import login_request, logout_request, signupApplicantPageView, signupEmployerPageView, applicationsPageView, deleteAccountPageView, viewAccountApplicantPageView, viewAccountEmployerPageView


urlpatterns = [
    path("logout", logout_request, name="logout"),
    path("login", login_request, name="login"),
    path("register-applicant/", signupApplicantPageView, name="register-applicant"),
    path("register-employer/", signupEmployerPageView, name="register-employer"),
    path("applications/", applicationsPageView, name="applications"),
    path("delete/", deleteAccountPageView, name="delete"),
    path("view-applicant/", viewAccountApplicantPageView, name="view-applicant"),
    path("view-employer/", viewAccountEmployerPageView, name="view-employer"),
]