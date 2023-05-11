from django.urls import path, include
from . import views
from rest_framework import routers
from .admin import admin_site

routers = routers.DefaultRouter()
routers.register(prefix='users', viewset=views.UserViewSet, basename='user')
routers.register(prefix='dangky', viewset=views.DangKyViewSet, basename='dangky')


urlpatterns = [
    path('', include(routers.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('admin/', admin_site.urls),
]