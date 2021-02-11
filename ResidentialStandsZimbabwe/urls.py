"""ResidentialStandsZimbabwe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from Lands.views import dashboard_page , home_page, celebrate_page ,confirm_purchase_page, myStands_page , focus_stand_page , standDetail_page , residential_stands_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #dashboard
    path('',dashboard_page,name='dashboard'),
    #authentication
    path('',include("django.contrib.auth.urls")),

    #home 
    path('home/',home_page,name="home"),

    #my stands
    path('myStands/',myStands_page,name="myStands"),

    #standDetail
    path('standDetail/',standDetail_page,name='standDetail'),

    #residential stands 
    path('residentialStands/', residential_stands_page,name="residential_stands"),

    #focus stand
    path('focusStand/', focus_stand_page,name="focus_stands"),

    #confirm purchase
    path('confirmPurchase/', confirm_purchase_page,name="confirm_purchase"),

    #celebrate purchase
    path('celebrate/', celebrate_page,name="celebrate")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
