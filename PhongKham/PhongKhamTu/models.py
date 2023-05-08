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





