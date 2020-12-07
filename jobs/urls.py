from django.urls import path
from .views import jobinfoPageView, availableJobsPageView, addJobListingPageView, employersListPageView, searchJobs, applicantHomepageView, employerHomepageView, searchEmployers, indexPageView, addjobFunc, deleteJobListing, updateJobListingPageView, updateJobListing

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', indexPageView, name='home'),
    path('applicant', applicantHomepageView, name='applicanthome'),
    path('employer', employerHomepageView, name='employerhome'),
    path('jobinfo/<int:jobID>/<int:applicantID>', jobinfoPageView, name='jobinfo'),
    path('jobs/<int:applicantID>', availableJobsPageView, name='jobs'),
    path('addlisting/', addJobListingPageView, name='addlisting' ),
    path('update-listing-view', updateJobListingPageView, name='updatelistingpage'),
    path('update-lisitng', updateJobListing, name='updatelisting'),
    path('employerlist/', employersListPageView, name='employerlist'),
    path('searchjob/', searchJobs, name='searchjob'),
    path('searchemployer/', searchEmployers, name='searchemployer'),
    path('addjobfunc/', addjobFunc, name='addjobfunc'),
    path('delete/<int:jobID>', deleteJobListing, name='deletejob'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)