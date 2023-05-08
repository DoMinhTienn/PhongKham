from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(prefix='users', viewset=views.UserViewSet, basename='user')


urlpatterns = [
    path('', include(routers.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
]