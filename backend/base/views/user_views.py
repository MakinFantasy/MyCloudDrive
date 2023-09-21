from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from base.serializers import UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairSerializer):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def user_register(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['name'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {
            'detail': 'User with this email already exists'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_update_profile(request):
    ...


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_get_profile(request):
    ...


@api_view(['GET'])
@permission_classes([IsAdminUser])
def users_get(request):
    ...


@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_get_by_id(request):
    ...


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_update(request):
    ...


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def user_delete(request):
    ...
