from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
urlpatterns = [
    #Dashboard
    path('Home',views.Home ),

    path('KYCList',views.KYCList ),
    path('WithdrawList',views.WithdrawList ),
    

    path('Inactive',views.Inactive ),

    path('EPINRequests',views.EPINRequests ),
    path('EPINFroward',views.EPINFroward ),
    path('AddOffer',views.AddOffer ),
    path('PLI',views.PLI),
    path('ExportData',views.ExportData ),
    path('Offerdel/<int:id>',views.Offerdel ),

    #JsonResoponse
    path('GetUserlist',views.GetUserlist ),
    path('UserDelete',views.UserDelete ),
    path('DeleteAllInactive',views.DeleteAllInactive ),
    path('GetKYCData',views.GetKYCData ),
    path('GETEPINData',views.GETEPINData ),
    path('GETEPINForwardData',views.GETEPINForwardData),
    path('PayWithdraw',views.PayWithdraw ),
    path('KYCVerified/<slug:userid>',views.KYCVerified ),
    path('PINVerified/<int:userid>',views.PINVerified ),
    path('PINForwardVerified/<int:userid>',views.PINForwardVerified ),
    path('KYCReject',views.KYCReject ),
    path('PINReject',views.PINReject ),
    path('PINForwardReject',views.PINForwardReject),
]

