from django.urls import path, include
from . import views
from rest_framework import routers
from .admin import admin_site

routers = routers.DefaultRouter()
routers.register(prefix='users', viewset=views.UserViewSet, basename='user')
routers.register(prefix='dangky', viewset=views.DangKyViewSet, basename='dangky')
routers.register(prefix='dangky', viewset=views.DeactiveDangkyViewSet, basename='dangky')
routers.register(prefix='thuoc', viewset=views.ThuocViewSet, basename='thuoc')
routers.register(prefix='donkham', viewset=views.DonKhamViewSet, basename='donkham')
routers.register(prefix='toathuoc', viewset=views.ToaThuocViewSet, basename='toathuoc')

urlpatterns = [
    path('', include(routers.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('admin/', admin_site.urls),
]