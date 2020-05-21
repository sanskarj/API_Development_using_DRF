from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import CommunicationSerializer
from rest_apis.models import communication
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_addcommunication(request):
    serial= CommunicationSerializer(data=request.data)
    if serial.is_valid():
        commu = serial.save(request.user)
        data={}
        data['success']  = "communication method is added successfully"
        return Response(data)
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def api_updatecommunication(request,medium):
    try:
        commu  = communication.objects.get(medium=medium,user=request.user)
        commu.delete()
        serial = CommunicationSerializer(data=request.data)
        if serial.is_valid():
            c= serial.save(request.user)
            return Response({"Success" : "Communication method Updated Successfully"})
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"failure": "Communication with given medium does not exist for this user"},status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_getcommunication(request):
    try:
        
        commu_methods = communication.objects.filter(user=request.user)
        
        serial = CommunicationSerializer(commu_methods,many=True)
        return Response(serial.data)
    except Exception as e:
        print(e)
        data = {}
        data['failure'] = "User doesn't have any methods of communication yet. try adding one"
        return Response(data)
    