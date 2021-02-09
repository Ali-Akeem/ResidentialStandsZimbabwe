from django.shortcuts import render
from .models import userData , stands
from django.contrib.auth.models import User

# Create your views here.
def dashboard_page(request):
    try :
        #user object 
        user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
        #context
        context = {
           "name" : user.name,
            "surname" : user.surname,
            "profileImage" : user.profilePhoto.url
        }

        return render(request,'dashboard/dashboard.html',context)
    except :
        print("got exception")

    return render(request,'dashboard/dashboard.html')

def home_page(request):
    #user object 
    user = (userData.objects.get(username=User.objects.get(username=request.user.username)))

    #userStands = stands.objects.get(owner=user)
    userStands = stands.objects.filter(owner=user)

    #context
    context = {
        "username" : user.username,
        "name" : user.name,
        "surname" : user.surname,
        "profileImage" : user.profilePhoto.url,
        "verificationCode" : user.verificationCode,
        "verified" : user.verified,
        "userStands" : userStands,
        "credit" : user.credit,
        "standsCount" : len(stands.objects.filter(purchased=False))
    
    }
    return render(request,'home/home.html',context)