from django.urls import path
from .views import homepageView, jobinfoPageView, availableJobsPageView, addJobListingPageView, employersListPageView

urlpatterns = [
    path('', homepageView, name='home'),
    path('jobinfo/', jobinfoPageView, name='jobinfo'),
    path('applicants/', availableJobsPageView, name='jobs'),
    path('addlisting/', addJobListingPageView, name='addlisting' ),
    path('employerlist/', employersListPageView, name='employerlist'),
]
