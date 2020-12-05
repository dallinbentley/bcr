from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("register-applicant/", views.signupApplicantPageView, name="register-applicant"),
    path("register-employer/", views.signupEmployerPageView, name="register-employer"),
    path("applications/", views.applicationsPageView, name="applications"),
    path("delete/", views.deleteAccountPageView, name="delete"),
    path("view-applicant/", views.viewAccountApplicantPageView, name="view-applicant"),
    path("view-employer/", views.viewAccountEmployerPageView, name="view-employer"),
]