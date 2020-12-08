from django.urls import path
from .views import jobinfoPageView, availableJobsPageView, addJobListingPageView, employersListPageView, searchJobs, applicantHomepageView, employerHomepageView, searchEmployers, indexPageView, addjobFunc, deleteJobListing, updateJobListingPageView, updateJobListing, quickApply, applicationsPageView, applicantUpdatePageView, applicantUpdate, empinfoPageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', indexPageView, name='home'),
    path('applicant/<int:applicantID>', applicantHomepageView, name='applicanthome'),
    path('employer/<int:employerID>', employerHomepageView, name='employerhome'),
    path('jobinfo/<int:jobID>/<int:applicantID>', jobinfoPageView, name='jobinfo'),
    path('jobs/<int:applicantID>', availableJobsPageView, name='jobs'),
    path('addlisting/<int:employerID>', addJobListingPageView, name='addlisting' ),
    path('update-listing-view', updateJobListingPageView, name='updatelistingpage'),
    path('update-lisitng', updateJobListing, name='updatelisting'),
    path('employerlist/<int:applicantID>/', employersListPageView, name='employerlist'),
    path('searchjob/<int:applicantID>', searchJobs, name='searchjob'),
    path('searchemployer/<int:applicantID>/', searchEmployers, name='searchemployer'),
    path('addjobfunc/<int:employerID>', addjobFunc, name='addjobfunc'),
    path('delete/<int:jobID>', deleteJobListing, name='deletejob'),
    path('quickapply/<int:jobID>/<int:applicantID>',quickApply, name='quickapply' ),
    path("applications/", applicationsPageView, name="applications"),
    path('applicant-update/<int:applicantID>', applicantUpdatePageView, name="applicant-update"),
    path('applicant-updated/<int:applicantID>', applicantUpdate, name="applicant-updated"),
    path('empinfo/<int:applicantID>/<int:employerID>/', empinfoPageView, name="empinfo"),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)