from django.contrib import admin

# Register your models here.
from datetime import datetime


from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count, Avg, Sum
from django.contrib.auth.models import Group
from datetime import date

class UserAdmin(admin.ModelAdmin):
    # ...

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        obj.save()

class ThuocAdmin(admin.ModelAdmin):
    # ...

    def save_model(self, request, obj, form, change):
        obj.save()

class ToaThuocAdmin(admin.ModelAdmin):
    # ...

    def save_model(self, request, obj, form, change):
        obj.save()

class PhongKhamAdminSite(admin.AdminSite):
    site_header = 'PhongKhamTu'


admin_site = PhongKhamAdminSite('myadmin')

admin_site.register(User, UserAdmin)
admin_site.register(ToaThuoc, ToaThuocAdmin)
admin_site.register(Thuoc, ThuocAdmin)