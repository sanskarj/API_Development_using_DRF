from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import ProjectSerializer
from rest_apis.models import projects

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_project(request):
    serial = ProjectSerializer(data=request.data)
    
    if serial.is_valid():
        serial.creating(request.user)
        return Response({"success" : "Project has been added"})
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_project(request,info):
    try:
        pro = projects.objects.get(info=info,user=request.user)
        pro.delete()
        return Response({"success":"Project deleted successfully"})
    except:
        return Response({"failure":"User doesn't have any project with the given info field"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_project(request):
    try:
        pro = projects.objects.filter(user=request.user)
        serial = ProjectSerializer(pro,many=True)
        return Response(serial.data)
    except:
        Response({"failure":"User doesn't have any project yet. try adding one"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_project(request,info):
    try:
        pro = projects.objects.get(info=info,user=request.user)
        pro.delete()
        serial  = ProjectSerializer(data=request.data)
        if serial.is_valid():
            serial.creating(request.user)
            return Response({"success":"Project updated successfully"})
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"failure" :"User does not have any prject with given info field"},status=status.HTTP_400_BAD_REQUEST)

    
    

    


    




