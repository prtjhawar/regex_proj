from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Create your models here.
class my_cv(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField( max_length=50)
    image=models.ImageField(upload_to='media')
    ability=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=50)
    dob=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    github=models.CharField(max_length=50)
    linkdin=models.CharField(max_length=50)
    address=models.CharField( max_length=50)
    degree_of_years=models.CharField(max_length=50)
    degree_name=models.CharField( max_length=50)
    clg_name=models.CharField(max_length=50)
    years12th=models.CharField(max_length=50)
    class_name12th=models.CharField( max_length=50)
    school_name12th=models.CharField(max_length=50)
    years10th=models.CharField(max_length=50)
    class_name10th=models.CharField( max_length=50)
    school_name10th=models.CharField(max_length=50)
    language=models.CharField( max_length=50)
    percent=models.CharField(max_length=50)
   

    working_in=models.CharField( max_length=50)
    working_years=models.CharField(max_length=50)
    company_name=models.CharField( max_length=50)
    designation1=models.CharField(max_length=50)
    working_in2=models.CharField( max_length=50)
    working_years2=models.CharField(max_length=50)
    company_name2=models.CharField( max_length=50)
    designation2=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    percents=models.CharField(max_length=50)
    interest=models.CharField(max_length=50)







