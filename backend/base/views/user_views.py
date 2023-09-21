from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['POST'])
def user_register(request):
    ...


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
