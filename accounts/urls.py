from django.urls import path
from .views import login_request, logout_request, signupApplicantPageView, signupEmployerPageView, deleteAccountPageView, viewAccountApplicantPageView, viewAccountEmployerPageView, loginPageView, signupEmployer, signupApplicant, deleteAccount

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("logout", logout_request, name="logout"),
    path("login", login_request, name="login"),
    path("userlogin", loginPageView, name="userlogin"),
    path("register-applicant/", signupApplicantPageView, name="register-applicant"),
    path("registered-applicant", signupApplicant, name='registered-applicant'),
    path("register-employer/", signupEmployerPageView, name="register-employer"),
    path("registered-employer", signupEmployer, name="registered-employer"),
    path("delete/", deleteAccountPageView, name="delete"),
    path("view-applicant/", viewAccountApplicantPageView, name="view-applicant"),
    path("view-employer/", viewAccountEmployerPageView, name="view-employer"),
    path('delete-account/<int:employerID>', deleteAccount, name='deleteaccount')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)