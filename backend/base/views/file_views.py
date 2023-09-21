from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.models import FileTb

from base.serializers import FileSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def file_create(request):
    user = request.user
    data = request.data

    if data and len(data) == 0:
        return Response(
            {
                'detail': 'No Files Uploaded'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        files = FileTb.objects.create(
            user_id=user,
            file_file=data['file_file'],
            file_name=data['file_name'],
            file_description=data['file_description'],
            file_size=data['file_size'],
            file_created_at=data['file_created_at'],
            file_type=data['file_type']
        )
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'detail': 'The file created successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def file_edit(request, pk):
    files = FileTb.objects.get(id=pk)
    serializer = FileSerializer(instance=files, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'detail':'The File was updated successfully!'},
            status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def file_delete(request, pk):
    product = FileTb.objects.get(id=pk)
    product.delete()
    return Response({
        'detail': 'The File delete successfully!'},
        status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def file_details(request, pk):
    try:
        files = FileTb.objects.get(id=pk)
        serializer = FileSerializer(files, many=False)

        return Response(serializer.data)
    except FileTb.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_files(request):
    user = request.user
    files = FileTb.objects.filter(user_id=user.id).order_by('-create_at')
    serializer = FileSerializer(files, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def files_list(request):
    files = FileTb.objects.all().order_by('-create_at')
    serializer = FileSerializer(files, many=True)

    return Response(serializer.data)
