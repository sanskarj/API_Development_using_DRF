from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import Profileimageserializer
from rest_apis.models import profileimage

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_createprofile(request):
    serial= Profileimageserializer(data=request.data)
    if serial.is_valid():
        image = serial.save(request.user)
        data={}
        data['success']  = "profile image is added successfully"
        return Response(data)
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def api_updateprofile(request):
    serial = Profileimageserializer(data=request.data)
    if serial.is_valid():
        image = serial.update(request.user)
        data = {}
        data['success']  = 'profile image is updated successfully'
        return Response(data)
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_getprofile(request):
    try:
        image = profileimage.objects.get(user=request.user)
        serial = Profileimageserializer(image)
        return Response(serial.data)
    except:
        data={}
        data['faliure']  ="u have not added any profile pic. please add one"
        return Response(data)

    

    
    
    


