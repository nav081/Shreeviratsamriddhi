from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Create',views.accountcreation ),
    path('Login',views.login ),
    path('Console',views.Console ),
    path('ForgetPassword',views.ForgetPassword ),
    path('EnterOTP',views.EnterOTP ),
    path('VerifyOTP',views.VerifyOTP ),
    path('Registration',views.Registration ),
    path('RefCreates/<slug:refid>',views.RefCreates ),
    path('Logout',views.Logout ),
    path('GetREfName',views.GetREfName )
]
