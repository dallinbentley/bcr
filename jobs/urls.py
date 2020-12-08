from django.urls import path
from .views import jobinfoPageView, availableJobsPageView, addJobListingPageView, employersListPageView, searchJobs, applicantHomepageView, employerHomepageView, searchEmployers, indexPageView, addjobFunc, deleteJobListing, updateJobListingPageView, updateJobListing, quickApply, applicationsPageView, applicantUpdatePageView, applicantUpdate, empinfoPageView,viewAccountEmployerPageView, employerUpdate
from django.conf import settings
from .views import myListingPageView, similarApplicantsRecommender
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
    path("applications/<int:employerID>/<listingID>/", applicationsPageView, name="applications"),
    path('applicant-update/<int:applicantID>', applicantUpdatePageView, name="applicant-update"),
    path('applicant-updated/<int:applicantID>', applicantUpdate, name="applicant-updated"),
    path('empinfo/<int:applicantID>/<int:employerID>/', empinfoPageView, name="empinfo"),
    path('mylistings/<int:employerID>', myListingPageView, name='mylistings'),
    path("view-employer/<int:employerID>", viewAccountEmployerPageView, name="view-employer"),
    path("update-employer/<int:employerID>", employerUpdate, name='employerupdate'),
    path("similar-applicants/<int:employerID>/<int:applicantID>", similarApplicantsRecommender, name='similarrecommender')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)