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


class developer(models.Model):
    registrationNumber = models.IntegerField(primary_key=True, null=False , auto_created=True, serialize=True)
    name = models.TextField(null=False)
    location = models.TextField(null=False)
    contactDetails = models.TextField(null=False)
    dateJoined = models.TextField(default="dd/mm/yyyy")
    standsSold = models.IntegerField(default=0)
    avaragePricing = models.TextField(default=0)
    rating = models.IntegerField(default=0)

class stands(models.Model):
    owner = models.ForeignKey(userData,on_delete=models.CASCADE,default=None)
    address = models.TextField(primary_key=True)
    purchased = models.BooleanField(default=False)
    price = models.TextField()
    stage =models.TextField(default="Stands released")
    image = models.ImageField(default="none.jpg", upload_to="standImages/", null=True)
    developer = models.ForeignKey(developer,on_delete=models.CASCADE, default=None)
    information = models.TextField(default="No information is set here")
    sitePlan = models.FileField(upload_to="docs/sitePlan/",default="img/notset")
    measurements = models.TextField(default="200 square metres")
    datePosted = models.TextField(default="dd/mm/yyyy")

class standImage(models.Model):
    image = models.ImageField(upload_to="standImages/")
    stand = models.ForeignKey(stands,on_delete=models.CASCADE)
    datePosted = models.TextField(default="mm/dd/yyyy")

class leases(models.Model):
    stand = models.ForeignKey(stands,on_delete=models.CASCADE)
    developer = models.ForeignKey(developer,on_delete=models.CASCADE)
    dateIssued = models.TextField(default="dd/mm/yy")
    agreementCode = models.IntegerField(auto_created=True)
    dateSigned = models.TextField(default="dd/mm/yyyy")
    governementLaw = models.TextField(default="Zimbabwe: Real Estate Laws and Regulations")





