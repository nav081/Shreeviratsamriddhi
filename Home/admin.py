from django.contrib import admin
from .models import Withdraws,BalanceHistory,KYC,Users,EPINRequest,Offers,DeadMoney,Notifications


# Register your models here.
admin.site.register(Users)
admin.site.register(Withdraws)
admin.site.register(BalanceHistory)
admin.site.register(KYC)
admin.site.register(EPINRequest)
admin.site.register(Offers)
admin.site.register(DeadMoney)
admin.site.register(Notifications)
