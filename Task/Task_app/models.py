from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.

class s_registration(models.Model):
    name=models.TextField(blank=True)
    reg_no=models.CharField(max_length=255)
    phone=models.IntegerField()
    address=models.CharField(max_length=255)
    paddress=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    dob=models.CharField(max_length=255)
    b_group=models.CharField(max_length=255)
    g_name=models.CharField(max_length=255)
    e_name=models.CharField(max_length=255)
    e_number=models.IntegerField()
    occupation=models.CharField(max_length=255)
    relation=models.CharField(max_length=255)
    g_number=models.IntegerField()
    course=models.CharField(max_length=255)
    course_fee=models.IntegerField()
    p_mode=models.CharField(max_length=255)
    n_emi=models.CharField(max_length=255,blank=True)
    s_user=models.ForeignKey(User,on_delete=models.CASCADE)
    student_Photo=models.ImageField(null=True,blank=True,upload_to='image/')
