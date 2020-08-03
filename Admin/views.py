from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from Home.models import Users,Withdraws,BalanceHistory,KYC,EPINRequest,Offers,Notifications
from django.forms.models import model_to_dict
from datetime import datetime
from datetime import date,timedelta
from django.contrib import messages
from django.core import serializers
import json
from django.template import RequestContext
import random
current_month = datetime.now().month
todaydate=date.today()



def Home(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'TotalUsers':Users.objects.count(),
    'ThisMonthRegistered':Users.objects.filter(CreationDate__month=current_month).count(),
    'TodayRegistered':Users.objects.filter(CreationDate=date.today()).count(),
    'payes':Users.objects.filter(ispayed=True).count(),
    'withdrawrequest':Withdraws.objects.filter(Status="Pending").count(),
    'withdrawreq':Withdraws.objects.filter(Status="Pending").order_by('-WithdrawRequestDate')[:5],
    'kycrequest':KYC.objects.count(),
    'Allusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),isactive=False).count(),
    'kycreq':KYC.objects.filter().order_by('-RequestDate')[:5],
    'offerlisr':Offers.objects.all(),
    }
    return render(request,'Admin/Main.html',param)

def ExportData(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    
    'withdrawrequest':Withdraws.objects.filter(Status="Pending").count(),
    'withdrawreq':Withdraws.objects.filter(Status="Pending").order_by('-WithdrawRequestDate')[:5],
    'kycrequest':KYC.objects.count(),
    'Allusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),isactive=False).count(),
    'kycreq':KYC.objects.filter().order_by('-RequestDate')[:5],
    'offerlisr':Offers.objects.all(),
    'AllData':Users.objects.all()
    }
    return render(request,'Admin/ExportData.html',param)


def PLI(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    }
    return render(request,'Admin/PLI.html',param)

def KYCList(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'Allusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),isactive=False).count(),
    'kycrequest':KYC.objects.count(),
    'kycreq':KYC.objects.filter().order_by('-RequestDate'),
    }
    return render(request,'Admin/KYCList.html',param)

def WithdrawList(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'Withdrawsrequest':Withdraws.objects.count(),
    'Allusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),isactive=False).count(),
    'Withdrawsreq':Withdraws.objects.filter(Status="Pending").order_by('-WithdrawRequestDate'),
    }
    return render(request,'Admin/WithdrawList.html',param)


def Inactive(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    
    'Allusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),ispayed=False).count(),
    'Inactiveusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),ispayed=False),
    }
    return render(request,'Admin/Inactive.html',param)


def AddOffer(request):
    _image=request.FILES['image']
    _file=request.FILES['file']
    _desc=request.POST.get("dec", "")
    _data=Offers(Desc=_desc,Image=_image,File=_file)
    _data.save()
    return HttpResponseRedirect("/Admin/Home")

def Offerdel(request,id):
    _dbcontext=Offers.objects.get(id=id).delete()
    return HttpResponseRedirect("/Admin/Home")



def EPINRequests(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'Allusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),isactive=False).count(),
    'MobileNumber':a.MobileNumber,
    'Epins':EPINRequest.objects.filter(Purpose="Add"),
    }
    return render(request,'Admin/EPIN.html',param)

def EPINFroward(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")

    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'Allusers':Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),isactive=False).count(),
    'MobileNumber':a.MobileNumber,
    'Epins':EPINRequest.objects.filter(Purpose="Send"),
    }
    return render(request,'Admin/EPINForwardRequests.html',param)




def PayWithdraw(request):
    id=request.GET['Id']
    num=request.GET['Mob']
    a=Users.objects.get(MobileNumber=num)
    prewith=a.AmountWithdrawed    
    Totalbalance=a.TotalMoney
    req=Withdraws.objects.get(id=id)
    Amount=req.WithdrawAmount
    Remaining=Totalbalance-int(Amount)
    afterwith=prewith+int(Amount)
    a.TotalMoney=Remaining
    a.AmountWithdrawed=afterwith
    a.save()
    req.WithdrawFullfilledDate=date.today()
    req.Status="Completed"
    req.save()
    return JsonResponse("Success",safe=False)

def DeleteAllInactive(request):
    Users.objects.filter(CreationDate__lte=date.today()-timedelta(days=3),isactive=False).delete()
    return JsonResponse("Success",safe=False)

def UserDelete(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    Role=request.session['Role']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/AdminLogout")
    elif(Role!="Admin"):
        return HttpResponseRedirect("/Account/AdminLogout")
    num=request.GET['Mob']
    Users.objects.filter(MobileNumber=num).delete()
    return JsonResponse("Success",safe=False)

def KYCReject(request):
    num=request.GET['Mob']
    reason=request.GET['Reason']
    a=Users.objects.get(MobileNumber=num)
    a.KYCMsg=reason
    a.save()
    Notify=Notifications(MobileNumber=num,Desc=reason,Header="KYC Rejected",icon="ban",isviewed=False)
    Notify.save()
    KYC.objects.filter(UserMobile=num).delete()
    return JsonResponse("Success",safe=False)

def KYCVerified(request,userid):
    num=int(userid)
    a=Users.objects.get(MobileNumber=num)
    a.KYCMsg=""
    a.KYC=True
    a.save()
    Notify=Notifications(MobileNumber=num,Desc="Your KYC Request is Accepted",Header="KYC Accepted",icon="check",isviewed=False)
    Notify.save()
    KYC.objects.filter(UserMobile=num).delete()
    response = HttpResponseRedirect("/Admin/KYCList")
    return response

def GetUserlist(request):
    res=request.GET['ID']
    num=request.GET['Mob']
    if(res=="1"):
        
        ListUser=serializers.serialize('json', Users.objects.filter().order_by('-HirarID'), fields=('First_Name','Last_Name','CreationDate','Username','MobileNumber'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    elif(res=="2"):
       
        ListUser=serializers.serialize('json', Users.objects.filter(CreationDate__month=current_month), fields=('First_Name','Last_Name','CreationDate','Username'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    elif(res=="3"):
        
        ListUser=serializers.serialize('json', Users.objects.filter(CreationDate=todaydate), fields=('First_Name','Last_Name','CreationDate','Username'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    elif(res=="4"):        
        ListUser=serializers.serialize('json', Users.objects.filter(ispayed=True), fields=('First_Name','Last_Name','CreationDate','Username'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    return JsonResponse("No data",safe=False)

def GetKYCData(request):
    num=request.GET['Mob']
    a=Users.objects.filter(MobileNumber=num)
    ListUser=serializers.serialize('json', Users.objects.filter(MobileNumber=num), fields=('First_Name','Last_Name','AdhaarID','PANNumber','AccountNummber','Username','MobileNumber','Adhaar_Front','Adhaar_Back','PANCard','Passbook'))
    Result=json.loads(ListUser)
    return JsonResponse(Result,safe=False)

def GETEPINData(request):
    num=request.GET['Mob']
    id=request.GET['ID']
    a=Users.objects.get(MobileNumber=num)
    EpinDetails=EPINRequest.objects.get(id=id)
    data={
            'name':a.First_Name+" "+a.Last_Name,
            'PINCount':EpinDetails.PINCount,
            'Amount':EpinDetails.Amount,
            'TransactionID':EpinDetails.TransactionID,
            'Screenshot':EpinDetails.Screenshot.url            
        }
    return JsonResponse(data,safe=False)

def PINVerified(request,userid):
    epinid=int(userid)
    req=EPINRequest.objects.get(id=epinid)
    Pins=req.PINCount
    Usernumber=req.UserMobile
    req.Status="Completed"
    req.Purpose="Done"
    req.save()
    a=Users.objects.get(MobileNumber=Usernumber)
    previouspin=a.NumberOfAccounts
    newpins=previouspin+Pins
    a.NumberOfAccounts=newpins
    a.save()
    Notify=Notifications(MobileNumber=Usernumber,Desc="Your EPIN is Added",Header="EPIN Added",icon="plus",isviewed=False)
    Notify.save()
    response = HttpResponseRedirect("/Admin/EPINRequests")
    return response

def PINForwardVerified(request,userid):
    epinid=int(userid)
    req=EPINRequest.objects.get(id=epinid)
    Sender=Users.objects.get(MobileNumber=req.UserMobile)
    Receiver=Users.objects.get(Username=req.To)
    PIN_to_give=req.PINCount
    Sender_TotalPins=Sender.NumberOfAccounts
    if(Sender_TotalPins-PIN_to_give<0):
        req.Status="Insufficient Pins"
        req.Purpose="Done"
        req.save()
    else:
        Sender_Have_pins=Sender_TotalPins-PIN_to_give
        Sender.NumberOfAccounts=Sender_Have_pins
        Sender.save()
        Receiver_total_pins=Receiver.NumberOfAccounts
        Receiver_havepins=Receiver_total_pins+PIN_to_give
        Receiver.NumberOfAccounts=Receiver_havepins
        Receiver.save()
        req.Status="Completed"
        req.Purpose="Done"
        req.save()
    Notify=Notifications(MobileNumber=req.UserMobile,Desc="Your EPIN is Forwarded",Header="EPIN Forwarded",icon="forward",isviewed=False)
    Notify.save()
    Notify1=Notifications(MobileNumber=Receiver.MobileNumber,Desc="You Received EPIN",Header="EPIN Received",icon="backward",isviewed=False)
    Notify1.save()
    response = HttpResponseRedirect("/Admin/EPINFroward")
    return response

def PINReject(request):
    id=request.GET['Mob']
    reason=request.GET['Reason']
    req=EPINRequest.objects.get(id=id)
    req.Status=reason
    req.Purpose="Done"
    req.save()
    Notify=Notifications(MobileNumber=req.UserMobile,Desc=reason,Header="EPIN Rejected",icon="exclamation",isviewed=False)
    Notify.save()
    return JsonResponse("Success",safe=False)


def PINForwardReject(request):
    id=request.GET['Mob']
    reason=request.GET['Reason']
    req=EPINRequest.objects.get(id=id)
    req.Status=reason
    req.Purpose="Done"
    req.save()
    Notify=Notifications(MobileNumber=req.UserMobile,Desc=reason,Header="EPIN Forward Failed",icon="ban",isviewed=False)
    Notify.save()
    return JsonResponse("Success",safe=False)

def GETEPINForwardData(request):
    num=request.GET['Mob']
    id=request.GET['ID']
    a=Users.objects.get(MobileNumber=num)
    
    EpinDetails=EPINRequest.objects.get(id=id)
    b=Users.objects.get(Username=EpinDetails.To)
    data={
            'name':a.First_Name+" "+a.Last_Name,
            'total':a.NumberOfAccounts,
            'PINCount':EpinDetails.PINCount,
            'recname':b.First_Name+" "+b.Last_Name,
            'username':EpinDetails.To            
        }
    return JsonResponse(data,safe=False)

#commited
