from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def file_create(request):
    ...


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def file_edit(request):
    ...


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def file_delete(request):
    ...


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def file_details(request):
    ...


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_files(request):
    ...


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def files_list(request):
    ...
