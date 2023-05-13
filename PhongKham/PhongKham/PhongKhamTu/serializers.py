from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *

class ThuocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thuoc
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    avatar_path = serializers.SerializerMethodField(source='avatar')
    def get_avatar_path(self, obj):
        request = self.context['request']
        if obj.avatar and not obj.avatar.name.startswith("/static"):

            path = '/static/%s' % obj.avatar.name

            return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'usertype', 'email',
                  'avatar', 'usertype' , 'avatar_path']
        extra_kwargs = {
            'password': {
                'write_only': True
            }, 'avatar_path': {
                'read_only': True
            }, 'avatar': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()

        return user

class DangKySerializer(serializers.ModelSerializer):
    ngay_kham = serializers.DateTimeField()
    class Meta:
        model = DangKy
        fields =  ['id', 'ho_bennhan', 'ten_benhnhan',
                  'email', 'phone', 'gioitinh', 'ngay_kham', 'active']

    def create(self, validated_data):
        validated_data['active'] = True
        ngay_kham = validated_data.pop('ngay_kham')
        dangky = DangKy.objects.create(ngay_kham=ngay_kham, **validated_data)
        return dangky

# class DangKyUpdateSerializer(serializers.Serializer):
#     active = serializers.BooleanField()
#
#     def update(self, instance, validated_data):
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

class DangKyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DangKy
        fields = ('active',)

    def update(self, instance, validated_data):
        active = validated_data.get('active', instance.active)
        instance.active = not instance.active  # Cập nhật giá trị ngược lại trong database
        instance.save()
        return instance

class DonKhamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonKham
        fields = ['id', 'dang_ky', 'Trieu_chung', 'ket_luan']

class ToaThuocSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToaThuoc
        fields = ['id', 'donkham', 'thuoc', 'so_luong']


