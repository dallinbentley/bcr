from django.db import models

# Create your models here.
class Employer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=50)
    company_city = models.CharField(max_length=50)
    company_state = models.CharField(max_length=50)
    company_zip = models.CharField(max_length=10)
    company_url = models.CharField(max_length=50)
    company_email = models.CharField(max_length=50)
    company_image = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.company_name

class Applicant(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    resume = models.FileField(upload_to="resume")
    skill_1 = models.ForeignKey('jobs.Skill', related_name="skill_1", on_delete=models.DO_NOTHING)
    skill_2 = models.ForeignKey('jobs.Skill', related_name="skill_2", on_delete=models.DO_NOTHING)
    skill_3 = models.ForeignKey('jobs.Skill', related_name="skill_3", on_delete=models.DO_NOTHING)
    skill_4 = models.ForeignKey('jobs.Skill', related_name="skill_4", on_delete=models.DO_NOTHING)
    skill_5 = models.ForeignKey('jobs.Skill', related_name="skill_5", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.last_name + ', ' + self.first_name + ': ' + self.username