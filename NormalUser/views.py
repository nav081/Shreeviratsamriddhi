from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from Home.models import Users,Withdraws,BalanceHistory,KYC,EPINRequest,DeadMoney,Notifications
from django.forms.models import model_to_dict
from datetime import datetime
from datetime import date
from django.contrib import messages
from django.core import serializers
import json
from django.template import RequestContext
import random
from django.urls import resolve

current_month = datetime.now().month
todaydate=date.today()


def Home(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    Totalregistered=Users.objects.filter(HirarID__gt=a.HirarID).count()
    Thismonth=Users.objects.filter(HirarID__gt=a.HirarID,CreationDate__month=current_month).count()
    TodayRegistered=Users.objects.filter(HirarID__gt=a.HirarID,CreationDate=todaydate).count()
    Payed=Users.objects.filter(ReferenceID=a.ReferalID).count()
    current_url = resolve(request.path_info).url_name
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'total':Totalregistered,
    'today':TodayRegistered,
    'month':Thismonth,
    'payed':Payed,
    'RefreralID':a.ReferalID,
    'Pins':a.NumberOfAccounts,
    'ispayed':a.ispayed,
    'url':current_url,
    'NotificationCount':Notifications.objects.filter(MobileNumber=Number).count(),
    'Notifications':Notifications.objects.filter(MobileNumber=Number)
    }
    return render(request,'NormalUser/Main.html',param)

def Team(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'TotalTeam':Users.objects.filter(HirarID__gt=a.HirarID).count(),
    'TotalPINS':a.NumberOfAccounts,
    'ActivePINS':Users.objects.filter(ReferenceID=a.ReferalID).count(),
    'PendingPINS':a.NumberOfAccounts-Users.objects.filter(ReferenceID=a.ReferalID).count(),
    'AmountWithdraw':a.AmountWithdrawed,
    'TotalEarned':a.TotalMoney+a.AmountWithdrawed,
    'InAccount':a.TotalMoney-a.AmountWithdrawed,
    'RegDate':a.CreationDate,
    }
    return render(request,'NormalUser/Team.html',param)

def Activate(request,usrmob):
    a=Users.objects.get(MobileNumber=usrmob)
    Totralnumberofaccounts=a.NumberOfAccounts
    newpincount=Totralnumberofaccounts-1
    a.NumberOfAccounts=newpincount
    a.ispayed=True
    a.save()

    for e in DeadMoney.objects.filter(SenderUserMobile=usrmob):
        useradd=Users.objects.get(MobileNumber=e.ReceiverUserMobile)
        tempmoney=useradd.TotalMoney
        tempmoney=tempmoney+e.Amount
        useradd.TotalMoney=tempmoney
        useradd.save()
        newbal=BalanceHistory(UserMobile=e.ReceiverUserMobile,UserBalanceHirar=1,BalanceAdded=str(e.Amount),Date=todaydate,Description="Refral Income")
        newbal.save()
    messages.success(request, 'You are Successfully added to our Team')
    response = HttpResponseRedirect("/NormalUser/Home")
    return response


def TeamDownline(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
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
    return render(request,'NormalUser/TeamDownline.html',param)

def SIA(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    _countChild=Users.objects.filter(HirarID__gt=a.HirarID).count()
    _active=Users.objects.filter(ReferenceID=a.ReferalID).count()

    if _countChild>150 and _active>0:
        Lev1Req=0
        Lev1Status="Achieved"
    else:
        Lev1Req=151-_countChild
        Lev1Status="Pending"
    if _countChild>350 and _active>0:
        Lev2Req=0
        Lev2Status="Achieved"
    else:
        Lev2Req=351-_countChild
        Lev2Status="Pending"
    if _countChild>850 and _active>0:
        Lev3Req=0
        Lev3Status="Achieved"
    else:
        Lev3Req=851-_countChild
        Lev3Status="Pending"
    if _countChild>1950 and _active>0:
        Lev4Req=0
        Lev4Status="Achieved"
    else:
        Lev4Req=1951-_countChild
        Lev4Status="Pending"
    if _countChild>4550 and _active>0:
        Lev5Req=0
        Lev5Status="Achieved"
    else:
        Lev5Req=4551-_countChild
        Lev5Status="Pending"
    if _countChild>9550 and _active>0:
        Lev6Req=0
        Lev6Status="Achieved"
    else:
        Lev6Req=9551-_countChild
        Lev6Status="Pending"
    if _countChild>19550 and _active>0:
        Lev7Req=0
        Lev7Status="Achieved"
    else:
        Lev7Req=19551-_countChild
        Lev7Status="Pending"
    if _countChild>44550 and _active>0:
        Lev8Req=0
        Lev8Status="Achieved"
    else:
        Lev8Req=44551-_countChild
        Lev8Status="Pending"
    if _countChild>95550 and _active>0:
        Lev9Req=0
        Lev9Status="Achieved"
    else:
        Lev9Req=95551-_countChild
        Lev9Status="Pending"
    if _countChild>195550 and _active>0:
        Lev10Req=0
        Lev10Status="Achieved"
    else:
        Lev10Req=195551-_countChild
        Lev10Status="Pending"
    if _countChild>445550 and _active>0:
        Lev11Req=0
        Lev11Status="Achieved"
    else:
        Lev11Req=445551-_countChild
        Lev11Status="Pending"
    if _countChild>945550 and _active>0:
        Lev12Req=0
        Lev12Status="Achieved"
    else:
        Lev12Req=945551-_countChild
        Lev12Status="Pending"
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'TotalTeam':Users.objects.filter(ReferenceID=a.ReferalID).count(),
    'TotalPINS':a.NumberOfAccounts,
    'ActivePINS':Users.objects.filter(ReferenceID=a.ReferalID).count(),
    'PendingPINS':a.NumberOfAccounts-Users.objects.filter(ReferenceID=a.ReferalID).count(),
    'AmountWithdraw':a.AmountWithdrawed,
    'TotalEarned':a.TotalMoney+a.AmountWithdrawed,
    'InAccount':a.TotalMoney,
    'RegDate':a.CreationDate,
    'Lev1Req':Lev1Req,
    'Lev2Req':Lev2Req,
    'Lev3Req':Lev3Req,
    'Lev4Req':Lev4Req,
    'Lev5Req':Lev5Req,
    'Lev6Req':Lev6Req,
    'Lev7Req':Lev7Req,
    'Lev8Req':Lev8Req,
    'Lev9Req':Lev9Req,
    'Lev10Req':Lev10Req,
    'Lev11Req':Lev11Req,
    'Lev12Req':Lev12Req,
    'Lev1Status':Lev1Status,    
    'Lev2Status':Lev2Status,
    'Lev3Status':Lev3Status,
    'Lev4Status':Lev4Status,
    'Lev5Status':Lev5Status,
    'Lev6Status':Lev6Status,
    'Lev7Status':Lev7Status,
    'Lev8Status':Lev8Status,
    'Lev9Status':Lev9Status,
    'Lev10Status':Lev10Status,
    'Lev11Status':Lev11Status,
    'Lev12Status':Lev12Status,    
    }
    return render(request,'NormalUser/SIA.html',param)

def TeamGeonology(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
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
    return render(request,'NormalUser/TeamGeonology.html',param)


def PLI(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
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
    return render(request,'NormalUser/PLI.html',param)

def TransactionPassword(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
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
    return render(request,'NormalUser/TransactionPassword.html',param)







def ChangePassword(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
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
    return render(request,'NormalUser/ChangePassword.html',param)

def ProfileKYC(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'KYCrejectmesg':a.KYCMsg
    }
    return render(request,'NormalUser/ProfileKYC.html',param)

def Withdraw(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'Pins':a.NumberOfAccounts,
    'ispayed':a.ispayed,
    'MobileNumber':a.MobileNumber,
    'TotalBalance':a.TotalMoney,

    }
    if(a.ispayed==False):
        return render(request,'NormalUser/StopWithdraw.html',param)

    return render(request,'NormalUser/Withdraw.html',param)

def WithdrawHistory(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'count':Withdraws.objects.filter(UserMobile=Number).count(),
    'WithdrawList':Withdraws.objects.filter(UserMobile=Number).order_by('-id')
    }
    return render(request,'NormalUser/WithdrawHistory.html',param)

def Income(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'WithdrawList':BalanceHistory.objects.filter(UserMobile=Number).order_by('-Date')
    }
    return render(request,'NormalUser/Income.html',param)

def EPIN(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'WithdrawList':BalanceHistory.objects.filter(UserMobile=Number).order_by('-Date')
    }
    return render(request,'NormalUser/EPIN.html',param)

def EPINForward(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'TotalPins':a.NumberOfAccounts
    }
    return render(request,'NormalUser/EPINForward.html',param)

def EPINHistory(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'Photo':Profilepic,
    'MobileNumber':a.MobileNumber,
    'Records':EPINRequest.objects.filter(UserMobile=a.MobileNumber).order_by('-id')
    }
    return render(request,'NormalUser/EPINHistory.html',param)


def WithdrawRequest(request):
    reqamount=request.POST.get("reqamount", "")
    _TPIN=request.POST.get("tpin", "")
    _MobileNumber  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(_MobileNumber)):
        return HttpResponseRedirect("/Account/Logout")
    _dbcontext=Users.objects.get(MobileNumber=_MobileNumber)
    if(_TPIN is not _dbcontext.TransactionPIN):
        messages.error(request, 'Wrong Transaction PIN !')
        return HttpResponseRedirect("/NormalUser/Withdraw")

    if(_dbcontext.TotalMoney<int(reqamount)):
        a=Withdraws(UserMobile=_MobileNumber,WithdrawAmount=reqamount,Status="Hold",WithdrawRequestDate=date.today())
        a.save()
    else:
        a=Withdraws(UserMobile=_MobileNumber,Name=_dbcontext.First_Name+" "+_dbcontext.Last_Name,WithdrawAmount=reqamount,Status="Pending",WithdrawRequestDate=date.today())
        a.save()    
    messages.success(request, 'Request Sent !')
    response = HttpResponseRedirect("/NormalUser/Withdraw")
    return response


def SubmitKYC(request):
    try:
        _Photo=request.FILES['photo']
    except:
        _Photo=None
    try:        
        _AdhaarFront=request.FILES['adhaarfront']
    except:
        _AdhaarFront=None
    try:        
        _AdhaarBack=request.FILES['adhaarback']
    except:
        _AdhaarBack=None
    try:    
        _PANCard=request.FILES['pancard']
    except:
        _PANCard=None
    try:    
        _Passbook=request.FILES['passbook']
    except:
        _Passbook=None
    _Name=""
    _MobileNumber  = request.COOKIES['MobileNumber']
    _dbcontext=Users.objects.get(MobileNumber=_MobileNumber)
    _dbcontext.Photo=_Photo
    _Name=_dbcontext.First_Name+" "+_dbcontext.Last_Name
    _dbcontext.Adhaar_Front=_AdhaarFront
    _dbcontext.Adhaar_Back=_AdhaarBack
    _dbcontext.PANCard=_PANCard
    _dbcontext.Passbook=_Passbook
    _dbcontext.save()
    kyccontext=KYC(UserMobile=_MobileNumber,Name=_Name,RequestDate=date.today())
    kyccontext.save()
    messages.success(request, 'Files Uploaded !')
    response = HttpResponseRedirect("/NormalUser/ProfileKYC")
    return response

def SubmitPassword(request):
    _OldPW=request.POST.get("oldpassword", "")
    _NewPW=request.POST.get("newpassword", "")
    _MobileNumber  = request.COOKIES['MobileNumber']
    _dbcontext=Users.objects.get(MobileNumber=_MobileNumber)
    if(_dbcontext.Password==_OldPW):        
        _dbcontext.Password=_NewPW
        _dbcontext.save()
        messages.success(request, 'Password Changed !')
    else:
        messages.error(request, 'Incorrect old Password !')
    response = HttpResponseRedirect("/NormalUser/ChangePassword")
    return response


def SubmitTransactionPassword(request):
    _OldPW=request.POST.get("password", "")
    _NewPW=request.POST.get("pin", "")
    _MobileNumber  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(_MobileNumber)):
        return HttpResponseRedirect("/Account/Logout")
    _dbcontext=Users.objects.get(MobileNumber=_MobileNumber)
    if(_dbcontext.Password==_OldPW):        
        _dbcontext.TransactionPIN=_NewPW
        _dbcontext.save()
        messages.success(request, 'Transaction PIN Updated !')
    else:
        messages.error(request, 'Incorrect old Password !')
    response = HttpResponseRedirect("/NormalUser/TransactionPassword")
    return response



def UpdateProfile(request):
    _First_Name=request.POST.get("firstname", "")
    _Last_Name=request.POST.get("lastname", "")
    _DOB=request.POST.get("DOB", "")
    _Gender=request.POST.get("gender", "")
    _MaritalStatus=request.POST.get("MaritalStatus", "")
    _MobileNumber  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(_MobileNumber)):
        return HttpResponseRedirect("/Account/Logout")
    _Email= request.POST.get("email", "")
    adline1=request.POST.get("adline1", "")
    adline2=request.POST.get("adline2", "")
    _District=request.POST.get("district", "")
    _Address=adline1+"@"+adline2    
    _State=request.POST.get("state", "")
    _Country=request.POST.get("country", "")
    _Pincode=request.POST.get("pincode", "")
    _Nomineename=request.POST.get("nomineename", "")
    _Nomineerelation=request.POST.get("nomineerelation", "")
    _Bankname=request.POST.get("bankname", "")
    _Bankbranch=request.POST.get("bankbranch", "")
    _Accnummber=request.POST.get("Accnum", "")
    _IFSCcode=request.POST.get("IFSC", "")
    _Adhaarnumber=request.POST.get("adhaar", "")
    _PANnumber=request.POST.get("PAN", "")
    _FName=request.POST.get("fname", "")
    _dbcontext=Users.objects.get(MobileNumber=_MobileNumber)
    _dbcontext.First_Name=_First_Name
    _dbcontext.Last_Name=_Last_Name
    _dbcontext.Gender=_Gender
    _dbcontext.Address=_Address
    _dbcontext.Email=_Email
    _dbcontext.District=_District
    _dbcontext.AdhaarID=_Adhaarnumber
    _dbcontext.PIN=_Pincode
    _dbcontext.State=_State
    _dbcontext.Country=_Country
    _dbcontext.DateOfBirth=_DOB
    _dbcontext.MaritalStatus=_MaritalStatus
    _dbcontext.NomineeName=_Nomineename
    _dbcontext.NomineeRelation=_Nomineerelation
    _dbcontext.BankName=_Bankname
    _dbcontext.BankBranch=_Bankbranch
    _dbcontext.AccountNummber=_Accnummber
    _dbcontext.IFSCcode=_IFSCcode
    _dbcontext.PANNumber=_PANnumber
    _dbcontext.FatherName=_FName
    _dbcontext.save()
    messages.success(request, 'Profile details updated.')
    response = HttpResponseRedirect("/NormalUser/Profile")
    return response

def Profile(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    a=Users.objects.get(MobileNumber=Number)
    addlines=a.Address
    refid=a.ReferenceID
    if(refid == None or refid==""):
        refid="MSB00000001"
    x=addlines.split("@")
    try:
        addline1=x[0]
        addline2=x[1]
    except:
        addline1=x[0]
        addline2=""
    try:
        Profilepic=a.Photo.url
    except:
        Profilepic="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSZtdPzPVZYhtNPE9kHEXQEaMW9v3RG9nN3svcLrIXrHBfnoPdx&usqp=CAU"
    
    param={
    'Name':a.First_Name+" "+a.Last_Name,
    'FirstName':a.First_Name,
    'Photo':Profilepic,
    'LastName':a.Last_Name,
    'FName':a.FatherName,
    'MobileNumber':a.MobileNumber,
    'Gender':a.Gender,
    'Addline1':addline1,
    'Addline2':addline2,
    'Email':a.Email,
    'District':a.District,
    'Adhaar':a.AdhaarID,
    'pincode':a.PIN,
    'State':a.State,
    'Country':a.Country,
    'DOB':a.DateOfBirth,
    'MaritalStatus':a.MaritalStatus,
    'NomineeName':a.NomineeName,
    'Nomerel':a.NomineeRelation,
    'BankName':a.BankName,
    'BankBranch':a.BankBranch,
    'AccountNummber':a.AccountNummber,
    'IFSCcode':a.IFSCcode,
    'PANNumber':a.PANNumber,
    'REfID':refid
    }

    return render(request,'NormalUser/Profile.html',param)

def AddEPIN(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    _Amount=request.POST.get("Price", "")
    _PINS=request.POST.get("PINS", "")
    _TransactionNumber=request.POST.get("Transc","")
    _Screenshot=request.FILES['Screenshot']
    a=Users.objects.get(MobileNumber=Number)

    _epincontext=EPINRequest(
    PINCount=_PINS,
    UserName=a.Username,
    UserMobile=str(Number),
    RequestDate=date.today(),
    Amount=_Amount,
    TransactionID=_TransactionNumber,
    To="Self",
    Screenshot=_Screenshot,
    Status="Requested",
    Purpose="Add"
    )
    _epincontext.save()
    messages.success(request, 'Request Forwarded !')
    response = HttpResponseRedirect("/NormalUser/EPIN")
    return response

def SendPINS(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) != str(Number)):
        return HttpResponseRedirect("/Account/Logout")
    _ReceiverID=request.POST.get("userid", "")
    _PINS=request.POST.get("count", "")

    a=Users.objects.get(MobileNumber=Number)

    _epincontext=EPINRequest(
    PINCount=_PINS,
    UserName=a.Username,
    UserMobile=str(Number),
    RequestDate=date.today(),
    To=_ReceiverID,
    Status="Requested",
    Purpose="Send"
    )
    _epincontext.save()
    messages.success(request, 'Request Forwarded !')
    response = HttpResponseRedirect("/NormalUser/EPINForward")
    return response

def GetPriceList(request):
    ID=request.GET['ID']
    ReqID=int(ID)
    if(ReqID==1):
        data={
            'pins':'10+1',
            'count':11,
            'price':10010
        }
    elif(ReqID==2):
       data={
            'pins':'20+2',
            'count':22,
            'price':20010
        }
    elif(ReqID==3):
        data={
            'pins':'30+5',
            'count':35,
            'price':30010
        }
    elif(ReqID==4):
        data={
            'pins':'50+7',
            'count':57,
            'price':50010
        }
    elif(ReqID==5):
        data={
            'pins':'1',
            'count':1,
            'price':1001
        }
    else:
        data={
            'pins':'--Select Set--',
            'price':'--Select Set--'
        }
    return JsonResponse(data,safe=False)

def GetName(request):
    ID=request.GET['ID']
    try:
        find=Users.objects.get(Username=ID)
        data={
            'name':find.First_Name+" "+find.Last_Name           
        }
    except:
        data={
            'name':'No user Found'           
        }
    return JsonResponse(data,safe=False)



def GetUserlist(request):
    res=request.GET['ID']
    num=request.GET['Mob']
    if(res=="1"):
        a=Users.objects.get(MobileNumber=num)
        ListUser=serializers.serialize('json', Users.objects.filter(HirarID__gt=a.HirarID), fields=('First_Name','Last_Name','CreationDate','Username','MobileNumber'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    elif(res=="2"):
        a=Users.objects.get(MobileNumber=num)
        ListUser=serializers.serialize('json', Users.objects.filter(HirarID__gt=a.HirarID,CreationDate__month=current_month), fields=('First_Name','Last_Name','CreationDate','Username'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    elif(res=="3"):
        a=Users.objects.get(MobileNumber=num)
        ListUser=serializers.serialize('json', Users.objects.filter(CreationDate=todaydate,HirarID__gt=a.HirarID), fields=('First_Name','Last_Name','CreationDate','Username'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    elif(res=="4"):
        a=Users.objects.get(MobileNumber=num)
        ListUser=serializers.serialize('json', Users.objects.filter(ReferenceID=a.ReferalID), fields=('First_Name','Last_Name','CreationDate','Username'))
        Result=json.loads(ListUser)
        return JsonResponse(Result,safe=False)
    return JsonResponse("No data",safe=False)
