from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    title = models.CharField(max_length=100)

class Gender(models.Model):
    title = models.CharField(max_length=20)
    code = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class MedicationType(models.Model):
    title = models.CharField(max_length=20)
    code = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class DiabeticsType(models.Model):
    title = models.CharField(max_length=20)
    code = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=20)
    code = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class RegistrationPath(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.ForeignKey(User,null=True)
    registration_path = models.ForeignKey(RegistrationPath,null=True,blank=True)
    mobile_number = models.CharField(max_length=11,null=True,blank=True)
    otp_token = models.IntegerField(default=0)
    otp_valid = models.BooleanField(default=True)
    birth_day = models.IntegerField(default=0)
    birth_month = models.IntegerField(default=0)
    birth_year = models.IntegerField(default=0)
    national_code = models.CharField(max_length=12,null=True,blank=True)
    postal_code = models.CharField(max_length=12,null=True,blank=True)
    gender = models.ForeignKey(Gender,blank=True,null=True)
    education = models.ForeignKey(Education,blank=True,null=True)

    diagnosis_year = models.IntegerField(default=1300)
    height = models.IntegerField(default=0)
    fasting_blood_sugar = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    medication_type = models.ForeignKey(MedicationType,null=True,blank=True)
    diabetics_type = models.ForeignKey(DiabeticsType,null=True,blank=True)


    def __unicode__(self):
        return self.mobile_number


class Question(models.Model):
    title = models.CharField(max_length=1000)
    code = models.IntegerField(default=0)
    front_end_short_code = models.CharField(max_length=100,null=True,blank=True)

    def __unicode__(self):
        return self.title

class QuestionareItem(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.BooleanField(default=False)

    def __unicode__(self):
        return self.question.title  + "-" + self.user.username
