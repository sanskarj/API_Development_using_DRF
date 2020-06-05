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
def api_add_skills(request):
    errors=[]
    for skill in request.data['skills']:
        serial = SkillsSerializer(data=skill)
        if serial.is_valid():
            serial.add(request.user)
        else:
            errors.append({skill['name']:serial.errors})
    if(len(errors)==0):
        return Response([{"success":"All new skills are added successfully"}],status=status.HTTP_200_OK)
    else:
        return Response(errors,status=status.HTTP_400_BAD_REQUEST)        
    

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def api_delete_skills(request):
    for id in request.data['ids']:
        h = skills.objects.get(id=id)
        h.users.remove(request.user)
    return Response([{"success" : "User is removed from the skills with given ids"}],status=status.HTTP_200_OK)
        
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_get_skills(request):
   skills_list =[]
   try:
       skills_All = skills.objects.filter(users=request.user)
       for h in list(skills_All):
           skills_list.append({"name":h.name,"competancy":h.competancy,"id":h.id})
       return Response(skills_list,status=status.HTTP_200_OK)
   except:
       return Response([{"failure":"User with given id doesn't have any skill. try adding one"}],status=status.HTTP_400_BAD_REQUEST)

    
    

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def api_update_skills(request):
    for skill in request.data['updated_skills']:
        desired_skill = skills.objects.get(id=skill['id'])
        desired_skill.competancy = skill['competancy']
        desired_skill.save()
    return Response([{"success" : "Selected skills updated"}])
    
    



        
    
    
    


        


