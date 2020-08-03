from django.db import models

class Users(models.Model):
    HirarID=models.IntegerField()
    First_Name=models.CharField(max_length=30)    
    Last_Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    TransactionPIN=models.CharField(max_length=30,null=True, blank=True)
    MobileNumber=models.BigIntegerField()
    Role=models.CharField(max_length=30)
    Gender=models.CharField(max_length=30)
    Address=models.CharField(max_length=300)
    Email=models.CharField(max_length=300)
    District=models.CharField(max_length=300)
    AdhaarID=models.CharField(max_length=300)
    PIN=models.CharField(max_length=300)
    State=models.CharField(max_length=300)
    Country=models.CharField(max_length=300)
    isactive=models.BooleanField()
    ispayed=models.BooleanField()
    KYC=models.BooleanField()
    NumberOfAccounts=models.IntegerField()
    AmountWithdrawed=models.IntegerField()
    TotalMoney=models.IntegerField()
    ReferenceID=models.CharField(max_length=30,null=True, blank=True)
    ReferalID=models.CharField(max_length=30,null=True, blank=True)
    CreationDate=models.DateField(null=True, blank=True)

    CurrentLevel=models.IntegerField(null=True, blank=True)
    lastMoneyAddedDate=models.DateField(null=True, blank=True)
    TotaldaysLeft1=models.IntegerField(null=True, blank=True)
    TotaldaysLeft2=models.IntegerField(null=True, blank=True)
    TotaldaysLeft3=models.IntegerField(null=True, blank=True)
    TotaldaysLeft4=models.IntegerField(null=True, blank=True)
    TotaldaysLeft5=models.IntegerField(null=True, blank=True)
    TotaldaysLeft6=models.IntegerField(null=True, blank=True)
    TotaldaysLeft7=models.IntegerField(null=True, blank=True)
    TotaldaysLeft8=models.IntegerField(null=True, blank=True)
    TotaldaysLeft10=models.IntegerField(null=True, blank=True)
    TotaldaysLeft11=models.IntegerField(null=True, blank=True)
    TotaldaysLeft12=models.IntegerField(null=True, blank=True)
    

    Photo = models.ImageField(upload_to='UsersPhoto',null=True, blank=True)
    DateOfBirth=models.TextField(max_length=300,null=True, blank=True)
    MaritalStatus=models.TextField(max_length=300,null=True, blank=True)
    NomineeName=models.TextField(max_length=300,null=True, blank=True)
    NomineeRelation=models.TextField(max_length=300,null=True, blank=True)
    BankName=models.TextField(max_length=300,null=True, blank=True)
    BankBranch=models.TextField(max_length=300,null=True, blank=True)
    AccountNummber=models.TextField(max_length=300,null=True, blank=True)
    IFSCcode=models.TextField(max_length=300,null=True, blank=True)
    PANNumber=models.TextField(max_length=300,null=True, blank=True)
    FatherName=models.TextField(max_length=300,null=True, blank=True)
    Adhaar_Front = models.ImageField(upload_to='UsersPhoto',null=True, blank=True)
    Adhaar_Back = models.ImageField(upload_to='UsersPhoto',null=True, blank=True)
    PANCard = models.ImageField(upload_to='UsersPhoto',null=True, blank=True)
    Passbook = models.ImageField(upload_to='UsersPhoto',null=True, blank=True)
    KYCMsg=models.TextField(max_length=300,null=True, blank=True)


class Withdraws(models.Model):
    UserMobile=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    WithdrawAmount=models.IntegerField()
    Status=models.CharField(max_length=50)
    WithdrawRequestDate=models.DateField()
    WithdrawFullfilledDate=models.DateField(null=True, blank=True)

class BalanceHistory(models.Model):
    UserMobile=models.CharField(max_length=50)
    UserBalanceHirar=models.IntegerField()
    BalanceAdded=models.CharField(max_length=50)
    Date=models.DateField()
    Description=models.TextField()

class KYC(models.Model):
    UserMobile=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    RequestDate=models.DateField()

class EPINRequest(models.Model):
    UserMobile=models.CharField(max_length=50)
    UserName=models.CharField(max_length=200,null=True,blank=True)
    PINCount=models.IntegerField()
    RequestDate=models.DateField()
    Amount=models.CharField(max_length=50,null=True, blank=True)
    TransactionID=models.CharField(max_length=100,null=True, blank=True)
    To=models.CharField(max_length=50,null=True, blank=True)
    Screenshot=models.ImageField(upload_to='PINRequests',null=True, blank=True)
    Status=models.CharField(max_length=50)
    Purpose=models.CharField(max_length=50)

class DeadMoney(models.Model):
    ReceiverUserMobile=models.CharField(max_length=50)
    Amount=models.IntegerField()
    SenderUserMobile=models.CharField(max_length=50)

class Offers(models.Model):
    Desc=models.TextField()
    Image=models.ImageField(upload_to='Offers',null=True, blank=True)
    File=models.FileField(upload_to='Offers',null=True, blank=True)

class Notifications(models.Model):
    MobileNumber=models.BigIntegerField()
    Desc=models.TextField()
    Header=models.CharField(max_length=200,null=True,blank=True)
    icon=models.CharField(max_length=200,null=True,blank=True)
    isviewed=models.BooleanField()




