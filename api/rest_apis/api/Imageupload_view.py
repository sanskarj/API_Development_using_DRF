from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  ImageUploadSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_apis.models import Imageupload

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_upload_image(request):
    serial = ImageUploadSerializer(data=request.data)
    if serial.is_valid():
        serial.create(request.user)
        return Response([{"success":"Image uploaded successfully"}],status=status.HTTP_200_OK)
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_image(request):
    try:
        img = Imageupload.objects.get(user=request.user)
        serial = ImageUploadSerializer(img)
        return Response(serial.data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response([{"failure":"User hasn't uploaded any image yet"}],status=status.HTTP_400_BAD_REQUEST)



