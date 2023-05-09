from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from ckeditor.fields import RichTextField
from enum import Enum

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserType(Enum):
    ADMIN = 'admin'
    BACSI = 'bacsi'
    YTA = 'yta'
    BENHNHAN = 'benhnhan'

class User(AbstractUser):
    usertype = models.CharField(max_length=10 , choices=[(type.value, type.name) for type in UserType], default=UserType.BENHNHAN.value)
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')

class ThuocType(Enum):
    VI = 'vi'
    CHAI = 'chai'
    VIEN = 'vien'
    LO = 'lo'
    HOP = 'hop'

class Thuoc(BaseModel):
    name = models.CharField(max_length=255, null=False, unique=True)
    donvi = models.CharField(max_length=10 , choices=[(type.value, type.name) for type in ThuocType], default=ThuocType.VIEN.value)

    def __str__(self):
        return self.name

class DangKy(BaseModel):
    ho_bennhan = models.CharField(max_length=255)
    ten_benhnhan = models.CharField(max_length=255, null=False, unique=True)
    email = models.CharField(max_length=255, null=False, unique=True)
    phone = models.CharField(max_length=255, null=False, unique=True)

