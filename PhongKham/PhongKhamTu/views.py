from django.shortcuts import render
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .models import *
from .serializers import UserSerializer, DangKySerializer

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
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def list(self, request):
        # GET method
        dangky_list = DangKy.objects.all()
        serializer = DangKySerializer(dangky_list, many=True)
        return Response(serializer.data)