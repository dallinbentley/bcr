from django.urls import path
from .views import homepageView, jobinfoPageView, availableJobsPageView, addJobListingPageView, employersListPageView, searchJobs, applicantHomepageView, employerHomepageView, searchEmployers, indexPageView, addjobFunc, deleteJobListing, deleteAccount, updateJobListingPageView, updateJobListing

urlpatterns = [
    path('', indexPageView, name='home'),
    path('applicant', applicantHomepageView, name='applicanthome'),
    path('employer', employerHomepageView, name='employerhome'),
    path('jobinfo/', jobinfoPageView, name='jobinfo'),
    path('applicants/', availableJobsPageView, name='jobs'),
    path('addlisting/', addJobListingPageView, name='addlisting' ),
    path('update-listing-view', updateJobListingPageView, name='updatelistingpage'),
    path('update-lisitng', updateJobListing, name='updatelisting'),
    path('employerlist/', employersListPageView, name='employerlist'),
    path('searchjob/', searchJobs, name='searchjob'),
    path('searchemployer/', searchEmployers, name='searchemployer'),
    path('addjobfunc/', addjobFunc, name='addjobfunc'),
    path('delete/<int:jobID>', deleteJobListing, name='deletejob'),
    path('delete-account/<int:employerID>', deleteAccount, name='deleteaccount')
]
