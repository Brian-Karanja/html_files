# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contractor,Foreman,KYM,client

# Register your models here.
class ContractorAdmin(admin.ModelAdmin):
	list_display=('name','location','qualification','email','phone_number')

class ForemanAdmin(admin.ModelAdmin):
	list_display=('name','location1','qualification','email','phone_number')

class KYMAdmin(admin.ModelAdmin):
	list_display=('name','location2','email','phone_number')


class clientAdmin(admin.ModelAdmin):
	list_display=('name','location3','email')
admin.site.register(Contractor,ContractorAdmin)
admin.site.register(Foreman,ForemanAdmin)
admin.site.register(KYM,KYMAdmin)
admin.site.register(client,clientAdmin)

