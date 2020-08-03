from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from twilio.rest import Client
from Home.models import Users,DeadMoney
from datetime import date
from django.template import RequestContext
import random

def Registration(request):
    return render(request,'Account/Registration.html')

def RefCreates(request,refid):

    find=Users.objects.get(ReferalID=refid)
    param={
        'refid':refid,
        'name':find.First_Name+" "+find.Last_Name
    }
    return render(request,'Account/Refcreate.html',param)

def accountcreation(request):
    _First_Name=request.POST.get("firstname", "")
    _Middle_Name=request.POST.get("midname", "")
    _Last_Name=request.POST.get("lastname", "")
    _Email=request.POST.get("email", "")
    _MobNum=request.POST.get("number", "")
    AddressLine1=request.POST.get("House", "")
    AddressLine2=request.POST.get("Street", "")
    _Gender=request.POST.get("Gender", "")
    _PIN=request.POST.get("Block", "")
    _RefID=request.POST.get("RefID", "")
    _AdhaarID=request.POST.get("AdhaarID", "")
    City=request.POST.get("City", "")
    District=request.POST.get("District", "")
    _State=request.POST.get("state", "")
    _Country=request.POST.get("country", "")
    UsersCount=Users.objects.count()
    UsersCount=UsersCount+1
    UsersCount=str(UsersCount)
    deflen=7
    length=len(UsersCount)
    zerorequired=deflen-length
    zeroes=""
    if(_Middle_Name==''):
        _Middle_Name=' '
    for i in range(zerorequired):
        zeroes=zeroes+"0"    
    UserCode=zeroes+UsersCount
    _Username="MSB"+UserCode+_First_Name[0]+_Last_Name[0]
    _Password="MB_"+_Last_Name[0]+_MobNum[0:4]
    _CreationDate = date.today()
    _Address=AddressLine1+"@"+AddressLine2+","+City

    _RefreralID=_Username[-4:-1]+_First_Name[0:3]+_MobNum[0:6]
    try:
        a=Users.objects.get(MobileNumber=_MobNum)
        return render(request,'Account/AlreadyRegistered.html')
    except:        
        CreateAccount=Users(HirarID=0,First_Name=_First_Name+" "+_Middle_Name,District=District,KYC=False,Last_Name=_Last_Name,AmountWithdrawed=0,TotalMoney=0,ReferalID=_RefreralID,Username=_Username,NumberOfAccounts=0,MobileNumber=_MobNum,Password=_Password,Role="User",Gender=_Gender,Address=_Address,Email=_Email,AdhaarID=_AdhaarID,PIN=_PIN,State=_State,Country=_Country,isactive=True,ispayed=False,ReferenceID=_RefID,CreationDate=_CreationDate)
        CreateAccount.save()
        try:
            totalrefaccounts=Users.objects.filter(ReferalID=_RefID).count()
        except:
            totalrefaccounts=0
        if(totalrefaccounts>6):
            ref1=Users.objects.get(ReferalID=_RefID)
            receivertempmobile=ref1.MobileNumber
            newmoney=DeadMoney(ReceiverUserMobile=receivertempmobile,Amount=200,SenderUserMobile=_MobNum)
            newmoney.save()
        else:
            #Money Add
            try:
                ref1=Users.objects.get(ReferalID=_RefID)
                tempref1=ref1.ReferenceID
                receivertempmobile=ref1.MobileNumber
                newmoney=DeadMoney(ReceiverUserMobile=receivertempmobile,Amount=200,SenderUserMobile=_MobNum)
                newmoney.save()
                try:
                    ref2=Users.objects.get(ReferalID=tempref1)
                    tempref2=ref2.ReferenceID
                    receivertempmobile=ref2.MobileNumber
                    newmoney=DeadMoney(ReceiverUserMobile=receivertempmobile,Amount=50,SenderUserMobile=_MobNum)
                    newmoney.save()
                    try:
                        ref3=Users.objects.get(ReferalID=tempref2)
                        tempref3=ref3.ReferenceID
                        receivertempmobile=ref3.MobileNumber
                        newmoney=DeadMoney(ReceiverUserMobile=receivertempmobile,Amount=25,SenderUserMobile=_MobNum)
                        newmoney.save()
                        try:
                            ref4=Users.objects.get(ReferalID=tempref3)
                            tempref4=ref4.ReferenceID
                            receivertempmobile=ref4.MobileNumber
                            newmoney=DeadMoney(ReceiverUserMobile=receivertempmobile,Amount=15,SenderUserMobile=_MobNum)
                            newmoney.save()
                            try:
                                ref5=Users.objects.get(ReferalID=tempref4)
                                tempref5=ref5.ReferenceID
                                receivertempmobile=ref5.MobileNumber
                                newmoney=DeadMoney(ReceiverUserMobile=receivertempmobile,Amount=10,SenderUserMobile=_MobNum)
                                newmoney.save()
                                try:
                                    ref6=Users.objects.get(ReferalID=tempref5)
                                    tempref6=ref5.ReferenceID
                                    receivertempmobile=ref6.MobileNumber
                                    newmoney=DeadMoney(ReceiverUserMobile=receivertempmobile,Amount=5,SenderUserMobile=_MobNum)
                                    newmoney.save()
                                except:
                                    None
                            except:
                                None
                        except:
                            None
                    except:
                        None
                except:
                    None
            except:
                None

        
        

        # account_sid = "AC65e033c527dec0f2b09136885e404d64"
        # auth_token  = "cd23f5fe831e867290ab7f9042524f3a"
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     to="+91"+_MobNum, 
        #     from_="+12058517423",
        #     body="Your Username and Password for Shree virat samriddhi is "+_Username+"\n"+"Password is "+_Password)

        reguser=Users.objects.get(MobileNumber=_MobNum)
        reguser.HirarID=reguser.id
        reguser.save()
        akshay={'username':_Username,'Passsword' :_Password}
        return render(request,'Account/AccountCreated.html',akshay)
        
    
def login(request):
    try:
        Check  = request.COOKIES['MobileNumber']
        Semob = request.session['MobileNumber']
        Role = request.session['Role']
        if(str(Semob) is not Check):
            HttpResponseRedirect("/Account/Logout")
        a=Users.objects.get(MobileNumber=Check)
        if(Role=="User"):
            return HttpResponseRedirect("/NormalUser/Home")
        elif(Role=="Admin"):
            return HttpResponseRedirect("/Admin/Home")
    except:
        return render(request,'Account/Login.html')

def ForgetPassword(request):
    return render(request,'Account/ForgetPassword.html')

def EnterOTP(request):
    _MobileNumber=request.POST.get("MobileNumber", "")
    try:
        a=Users.objects.get(MobileNumber=_MobileNumber)
        name=a.First_Name+" "+a.Last_Name
        OTP = random.randint(0000,9999)
        StrMOb=str(a.MobileNumber)
        StrOTP=str(OTP)
        account_sid = ""
        auth_token  = "300918dcf8050b5b2b3c5ceba4f9aeb1"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+91"+StrMOb, 
            from_="+12055840677",
            body="Message From Mission Bharat \n Your OTP for Rsest Password is "+StrOTP)
        param={'MobileNumber':a.MobileNumber,'Name':name,'OTP':OTP}
        return render(request,'Account/EnterOTP.html',param)

    except Exception as e:
        param={'error':'Mobile Number could not be found !'}
        return render(request,'Account/ForgetPassword.html',param)

def VerifyOTP(request):
    _MobileNumber=request.POST.get("MobileNumber", "")
    _OTP=request.POST.get("OTP", "")
    _Name=request.POST.get("name", "")
    _UserOTP=request.POST.get("UserOTP", "")
    if(_OTP!=_UserOTP):
        param={'MobileNumber':_MobileNumber,'Name':_Name,'OTP':_OTP,'error':'Wrong OTP !'}
        return render(request,'Account/EnterOTP.html',param)
    else:
        a=Users.objects.get(MobileNumber=_MobileNumber)
        _Last_Name=a.Last_Name
        _MobNum=str(a.MobileNumber)
        _Password="MB_"+_Last_Name[0]+_MobNum[0:4]
        _Username=a.Username
        a.Passsword=_Password
        a.save()
        account_sid = "ACe595f0235bc002a8aa80a623576f57e3"
        auth_token  = "300918dcf8050b5b2b3c5ceba4f9aeb1"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+91"+_MobNum, 
            from_="+12055840677",
            body="Your New Username and Password for Mission Bharat is "+_Username+"\n"+"Password is "+_Password)
        return render(request,'Account/PasswordResetMessage.html')


def UserConsole(request):
    Number  = request.COOKIES['MobileNumber']
    Semob = request.session['MobileNumber']
    if(str(Semob) is not Number):
        return HttpResponseRedirect("/Account/Logout")    
    a=Users.objects.get(MobileNumber=Number)
    param={'Name':a.First_Name+" "+a.Last_Name,'MobileNumber':a.MobileNumber}
    return render(request,'NormalUser/Main.html',param)


    
def AdminConsole(request):
    Number  = request.COOKIES['MobileNumber']    
    a=Users.objects.get(MobileNumber=Number)
    param={'Name':a.First_Name+" "+a.Last_Name,'MobileNumber':a.MobileNumber}
    return render(request,'NormalUser/Main.html',param)


def Console(request):
    param={'error':'Username or Password could not be found !'}   
    response=render(request,'Account/Login.html',param)
    _Username=request.POST.get("Username", "")
    _Password=request.POST.get("Passsword", "")
    try:
        b=Users.objects.get(Username=_Username,Password=_Password)
        if(b.Role=="User"):
            response = HttpResponseRedirect("/Account/Login")    
            response.set_cookie('MobileNumber',b.MobileNumber)
            request.session['MobileNumber'] = b.MobileNumber
            request.session['Role'] = "User"
        elif(b.Role=="Admin"):
            response = HttpResponseRedirect("/Account/Login")
            response.set_cookie('MobileNumber',b.MobileNumber)
            request.session['MobileNumber'] = b.MobileNumber
            request.session['Role'] = "Admin"         
        return response
    except Exception as ex:
        return response
        
def Logout(request):
    response = HttpResponseRedirect("/Account/Login")
    response.delete_cookie('MobileNumber')
    try:
        del request.session['MobileNumber']
    except:
        None
    try:
        del request.session['Role']
    except:
        None
    return response


def GetREfName(request):
    ID=request.GET['ID']
    try:
        find=Users.objects.get(ReferalID=ID)
        data={
            'name':find.First_Name+" "+find.Last_Name           
        }
    except:
        data={
            'name':'No user Found'           
        }
    return JsonResponse(data,safe=False)

    

    
