from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import SkillsSerializer
from rest_apis.models import skills
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_addskill(request):
    serial= SkillsSerializer(data=request.data)
    if serial.is_valid():
        serial.add(request.user)
        return Response({"success" : "skill added successfully"})

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def api_deleteskill(request):
    serial = SkillsSerializer(data=request.data)
    if serial.is_valid():
        serial.delete(request.user)
        return Response({"success":"skill deleted"})

        
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_getskill(request):
    try:
        skill = skills.objects.filter(users=request.user)
        
        serial = SkillsSerializer(skill,many=True)
        return Response(serial.data)
    except:
        data= {}
        data['failure']  =  "You don't have any skills yet, why are u hiding your talent let the world know your skill"
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def api_updateskill(request,name,proficiency):
    serial = SkillsSerializer(data=request.data)
    if serial.is_valid():
        serial.update(request.user,name,proficiency)
        return Response({"success":"skill updated"})
    else:
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    

        
    
    
    


        


