from django.shortcuts import render
from .models import userData , stands , standImage
from django.contrib.auth.models import User
from time import gmtime, strftime

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

def myStands_page(request):
    #user object 
    user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
    #userStands = stands.objects.get(owner=user)
    userStands = stands.objects.filter(owner=user)
    context = {
        "userStands" : userStands,
        "time" : strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
    return render(request,"myStands/myStands.html",context)
    

def residential_stands_page(request):
    print(request.method)
    if (request.method == "GET"):
        print("Get")
        user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
        #userStands = stands.objects.get(owner=user)
        standsAll = stands.objects.filter(purchased=False)
        context = {
            "stands" : standsAll,
        }
        return render(request,"residentialStands/residentialStands.html",context)
    else :
        print("Post")
        user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
        #userStands = stands.objects.get(owner=user)
        standsAll = stands.objects.filter(purchased=False)
        context = {
            "stands" : standsAll,
        }
        return render(request,"residentialStands/residentialStands.html")


def standDetail_page(request):
    stand  = request.GET.get("variable1")
    context = {
        "data" : stands.objects.get(address=stand)
    }
    return render(request,"myStands/standDetail.html" , context)