from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userData(models.Model):
    verificationCode = models.TextField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField()
    surname  = models.TextField()
    photo = models.TextField()
    idNumber = models.TextField()
    dob = models.TextField()
    gender = models.TextField()
    profilePhoto = models.ImageField(upload_to='profiles/')
    verified = models.BooleanField(default=False)
    credit = models.TextField(default="ZWL$0,00")


class stands(models.Model):
    owner = models.ForeignKey(userData,on_delete=models.CASCADE,default=None)
    address = models.TextField(primary_key=True)
    purchased = models.BooleanField(default=False)
    price = models.TextField()
    stage =models.TextField(default="Stands released")
