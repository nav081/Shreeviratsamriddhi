from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
urlpatterns = [
    #Dashboard
    path('Home',views.Home ),
    path('Activate/<slug:usrmob>',views.Activate),

    #Profile
    path('Profile',views.Profile ),
    path('ProfileKYC',views.ProfileKYC ),
    path('ChangePassword',views.ChangePassword ),
    path('TransactionPassword',views.TransactionPassword ),

    path('Profile/UpdateProfile',views.UpdateProfile ),
    path('ProfileKYC/SubmitKYC',views.SubmitKYC ),
    path('ChangePassword/SubmitPassword',views.SubmitPassword ),
    path('TransactionPassword/SubmitTransactionPassword',views.SubmitTransactionPassword ),

    #Team
    path('Team',views.Team),
    path('TeamDownline',views.TeamDownline),
    path('TeamGeonology',views.TeamGeonology),

    #SingleLegAchievement
    path('SIA',views.SIA),

    #E-PIN
    path('EPIN',views.EPIN),
    path('AddEPIN',views.AddEPIN),
    path('EPINForward',views.EPINForward),
    path('EPINHistory',views.EPINHistory),
    path('SendPINS',views.SendPINS),
    path('GetPriceList',views.GetPriceList),
    path('GetName',views.GetName),

    #Income
    path('Income',views.Income),

    #Withdraw
    path('Withdraw',views.Withdraw),
    path('WithdrawHistory',views.WithdrawHistory),
    path('WithdrawRequest',views.WithdrawRequest),

    #Pre-Launching Income
    path('PLI',views.PLI),

    #Payment
    path('Payment',views.SIA),
    
    #JasonData
    path('GetUserlist',views.GetUserlist ),
]

