from django.contrib.auth.models import User
from django.db import models

STATUS = (
    ('1', 'Queued'),
    ('2', 'Reviewed'),
    ('3', 'Reviewed and Needs Update'),
    ('4', 'Complete'),
)


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    status = models.CharField(max_length=3, choices=STATUS, default='1')


class Comments(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()


PREFIX_OPTIONS = (
    ("3","-"),
    ("0","Mr"),
    ("1","Mrs"),
    ("2","Ms"),
)

class Contact(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    prefix = models.CharField(max_length=1,choices=PREFIX_OPTIONS,default="3")
    first_name = models.CharField(max_length=20,blank=False,default=None)
    last_name = models.CharField(max_length=20,blank=False,default=None)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.BigIntegerField()
    phone_number = models.BigIntegerField()
    email = models.EmailField(unique=True)
    linked_in = models.URLField(unique=True)
    github = models.URLField(unique=True)


class About(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    summary = models.TextField()


PROFICIENCY_OPTIONS = (
    ("1","Basic"),
    ("2","Intermediate"),
    ("3","Advanced"),
    ("4","Expert"),
)
class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=1,choices=PROFICIENCY_OPTIONS,default="1")

STATUS = (
    ("1","Completed"),
    ("2","Pursuing"),
)
class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    joining_date = models.DateField()
    status = models.CharField(max_length=1,default="2",choices=STATUS)
    passing_date = models.DateField(null=True,blank=True)
    score = models.DecimalField(decimal_places=2,max_digits=5)

class Internship_Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    i_status = models.CharField(max_length=1,choices=STATUS,default="2")
    date_of_exit = models.DateField(null=True,blank=True)
    description = models.TextField()


class Training_Certification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    t_status = models.CharField(max_length=1,choices = STATUS,default="2")
    date = models.DateField(null=True)

PROJECT_STATUS = (
    ("1","Completed"),
    ("2","Ongoing"),
)
class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    p_status = models.CharField(choices = PROJECT_STATUS,max_length=1,default="2")
    end_date = models.DateField(null=True,blank=True)
    description = models.TextField()



class Extra(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField()


class Language(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=1,choices=PROFICIENCY_OPTIONS,default="0")

class Personal_Interest(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField()

class Achievement(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField()

class Declaration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    declaration = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date = models.DateField()


class Other(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,unique=False)
    heading = models.CharField(max_length=30)
    description = models.TextField()