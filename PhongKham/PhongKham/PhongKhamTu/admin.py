from django.contrib import admin

# Register your models here.
from datetime import datetime


from django.contrib import admin
from .models import User
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count, Avg, Sum
from django.contrib.auth.models import Group
from datetime import date

class PhongKhamAdminSite(admin.AdminSite):
    site_header = 'PhongKhamTu'


admin_site = PhongKhamAdminSite('myadmin')

admin_site.register(User)