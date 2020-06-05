from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_apis.api.serializers import  Registeruser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_apis.api.serializers import ProjectSerializer
from rest_apis.models import projects, Skill_names

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_project(request):
    serial = ProjectSerializer(data=request.data)
    
    if serial.is_valid():
        serial.creating(request.user)
        return Response([{"success" : "Project has been added"}])
    else:
        return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_delete_project(request):
    pro = projects.objects.get(id=request.data['id'])
    pro.users.remove(request.user)
    return Response([{"success":"User is removed from this project"}])



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_project(request):
    pr =[]
    try:
        pro = projects.objects.filter(users=request.user)
        for new_pro in list(pro):
            pr.append({"info":new_pro.info,"starts":new_pro.starts,"ends":new_pro.ends,"description":new_pro.description,"status":new_pro.status,"id":new_pro.id})
        return Response(pr,status=status.HTTP_200_OK)
    except:
        return Response([{"failure":"User is not part of any project"}],status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_project(request):
    pro = projects.objects.get(id=request.data['id'])
    
    pro.info  = request.data['info']
    pro.starts  = request.data['starts']
    pro.ends = request.data['ends']
    pro.description = request.data['description']
    pro.status = request.data['status']
    pro.save()
    return Response([{"success":"project updated"}])

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_users_to_project(request):
    pro = projects.objects.get(id=request.data['id'])
    for people in request.data['users']:
        pro.users.add(User.objects.get(username=people['username']))
    return Response([{"success":"Selected users added to the project"}])



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_skills_to_project(request):
    pro = projects.objects.get(id=request.data['id'])
    for skill in request.data['skills']:
        try:
            ski=  Skill_names.objects.get(name=skill['name'])
            pro.skills.add(ski)
        except:
            ski = Skill_names(name=skill['name'])
            ski.save()
            pro.skills.add(ski)
    return Response([{"success":"Selected skills added to the project"}])

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_users_of_project(request):
    pro = projects.objects.get(id=request.data['id'])
    users=[]
    for user in list(pro.users.all()):
        users.append({"name":user.username})
    return Response(users,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_skills_of_project(request):
    pro = projects.objects.get(id=request.data['id'])
    skills=[]
    for skill in list(pro.skills.all()):
        skills.append({"name":skill.name})
    return Response(skills,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_all_available_skills(request):
    skills = []
    for skill in list(Skill_names.objects.all()):
        skills.append({"name":skill.name})
    return Response(skills,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_all_registered_users(request):
    users = []
    for user in list(User.objects.all()):
        users.append({"username":user.username})
    return Response(users,status=status.HTTP_200_OK)

    
    



     
    






    

    

    
    

    


    




