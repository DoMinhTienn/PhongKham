from django.shortcuts import render
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .models import *
import datetime
from .serializers import UserSerializer, DangKySerializer, DangKyUpdateSerializer, ThuocSerializer, DonKhamSerializer, ToaThuocSerializer

class AuthInfo(APIView):

    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path="current-user", detail=False)
    def current_user(self, request):
        return Response(self.serializer_class(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class DangKyViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = DangKy.objects.all()
    serializer_class = DangKySerializer
    parser_classes = [MultiPartParser, ]

    def dangky(self, request, format=None):
        serializer = DangKySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Không truyền giá trị ngày khám vào hàm save của serializer
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def list(self, request):
        # GET method
        dangky_list = DangKy.objects.all()
        q = self.request.query_params.get('date')
        if q:
            ngay = datetime.datetime.strptime(q, '%Y-%m-%d').date()
            dangky_list = dangky_list.filter(ngay_kham__date=ngay)
        serializer = DangKySerializer(dangky_list, many=True)
        return Response(serializer.data)

class DeactiveDangkyViewSet(viewsets.ViewSet):
    queryset = DangKy.objects.all()

    def partial_update(self, request, pk=None):
        instance = get_object_or_404(DangKy, pk=pk)
        serializer = DangKyUpdateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThuocViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Thuoc.objects.filter(active=True)
        serializer = ThuocSerializer(queryset, many=True)
        return Response(serializer.data)

class DonKhamViewSet(viewsets.ModelViewSet):
    serializer_class = DonKhamSerializer
    queryset = DonKham.objects.all()

    def create(self, request):
        serializer = DonKhamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py
class ToaThuocViewSet(viewsets.ModelViewSet):
    queryset = ToaThuoc.objects.all()
    serializer_class = ToaThuocSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     toathuoc = serializer.save()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

