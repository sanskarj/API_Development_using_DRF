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
        return Response([{"success" : "Project has been added"}])
    else:
        return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_project(request,info):
    try:
        pro = projects.objects.get(info=info)
        try:
            pro.users.remove(request.user)
            return Response([{"success": "You have been successfully removed from this project"}],status=status.HTTP_200_OK)
        except:
            return Response([{"failure":"user is not the part of this project"}],status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response([{"failure":" The project with given info doesn't exist"}],status=status.HTTP_400_BAD_REQUEST)

   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_project(request):
    try:
        pro = projects.objects.filter(users=request.user)
        serial = ProjectSerializer(pro,many=True)
        return Response(serial.data)
    except:
        return Response([{"failure":"User doesn't have any project yet. try adding one"}],status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_project(request,info):
    serial =    ProjectSerializer(data=request.data)
    if serial.is_valid():
        serial.update(info)
        return Response([{"success" : "project updated"}],status=status.HTTP_200_OK)
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_all_projects(request):
    all_pro = projects.objects.all()
    serial = ProjectSerializer(all_pro,many=True)
    return Response(serial.data)



    

    

    
    

    


    




