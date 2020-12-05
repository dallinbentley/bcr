from django.contrib import admin
from .models import Skill, JobListing, JobType, QuickApply


# Register your models here.
admin.site.register(Skill)
admin.site.register(JobListing)
admin.site.register(JobType)
admin.site.register(QuickApply)