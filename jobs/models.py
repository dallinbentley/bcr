from django.db import models

# Create your models here.

class JobType(models.Model):
    job_type_description = models.CharField(max_length=20)

    def __str__(self):
        return self.job_type_description


class Skill(models.Model):
    skill_description = models.CharField(max_length=20)

    def __str__(self):
        return self.skill_description


class JobListing(models.Model):
    company_ID = models.ForeignKey('accounts.Employer', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    wage = models.FloatField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    job_description = models.CharField(max_length=2000)
    preferred_skill1 = models.ForeignKey(Skill, related_name='preferredSkill1', on_delete=models.DO_NOTHING, blank=True, null=True)
    preferred_skill2 = models.ForeignKey(Skill, related_name='preferredSkill2', on_delete=models.DO_NOTHING, blank=True, null=True)
    preferred_skill3 = models.ForeignKey(Skill, related_name='preferredSkill3', on_delete=models.DO_NOTHING, blank=True, null=True)

    application = models.ManyToManyField('accounts.Applicant', through='QuickApply')

    def __str__(self):
        return (self.job_title)

class QuickApply(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applicant = models.ForeignKey('accounts.Applicant', on_delete=models.CASCADE)
    matching_skills = models.SmallIntegerField()

    def __str__(self):
      return  (self.job_listing.job_title + ', '+ self.applicant.first_name + ' ' + self.applicant.last_name + ', ' + str(self.matching_skills))

