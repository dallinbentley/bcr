from django.urls import path
from .views import homepageView, jobinfoPageView, availableJobsPageView

urlpatterns = [
    path('', homepageView, name='home'),
    path('jobinfo/', jobinfoPageView, name='jobinfo'),
    path('applicants/', availableJobsPageView, name='jobs'),
]
