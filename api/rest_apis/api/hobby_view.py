from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import HobbySerializer
from rest_apis.models import hobby
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_addhobby(request):
    serial= HobbySerializer(data=request.data)
    if serial.is_valid():
        req_hobby = serial.save(request.user)
        data={}
        data['success']  = "hobby is added successfully"
        return Response([data])
    else:
        return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def api_deletehobby(request):
    serial = HobbySerializer(data=request.data)
    if serial.is_valid():
        serial.delete(request.user)
        data = {}
        data['success']  = 'hobby is deleted successfully'
        return Response([data])
    else:
        return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_gethobby(request):
    try:
        hobbies = hobby.objects.filter(users=request.user)
        print(hobbies)
        serial = HobbySerializer(hobbies,many=True)
        return Response(serial.data)
    except:
        data= {}
        data['failure']  =  'you do not have any hobbies yet, how about try adding one'
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_all_hobbies(request):
    all_hobby= hobby.objects.all()
    serial = HobbySerializer(all_hobby,many=True)
    return Response(serial.data)
  