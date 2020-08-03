from django.http import HttpResponse
from django.shortcuts import render
from Home.models import Offers
import re

def mobile(request):

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

def index(request):

    param={

        'offerlist':Offers.objects.all()
    }

    if mobile(request):
        return render(request,'Home/Mobile.html',param)
    else:
        return render(request,'Home/index.html',param)

    
    return render(request,'Home/index.html',param)



def Mobile(request):

    param={


        'offerlist':Offers.objects.all()
    }
    return render(request,'Home/Mobile.html',param)

def contactus(request):
    return render(request,'Home/ContactUs.html')

def Services(request):
    return render(request,'Home/Services.html')