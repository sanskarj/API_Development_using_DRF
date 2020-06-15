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
from rest_framework.views import APIView

class Projects(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def create(self,request):
        serial = ProjectSerializer(data=request.data)
    
        if serial.is_valid():
            serial.creating(request.user)
            return Response([{"success" : "Project has been added"}])
        else:
            return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)
    def add_users(self,request):
        pro = projects.objects.get(id=request.data['id'])
        for people in request.data['users']:
            pro.users.add(User.objects.get(username=people['username']))
        return Response([{"success":"Selected users added to the project"}])
    def add_skills(self,request):
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
    def get_project(self,request):
        pr =[]
        try:
            pro = projects.objects.filter(users=request.user)
            for new_pro in list(pro):
                pr.append({"info":new_pro.info,"starts":new_pro.starts,"ends":new_pro.ends,"description":new_pro.description,"status":new_pro.status,"id":new_pro.id})
            return Response(pr,status=status.HTTP_200_OK)
        except:
            return Response([{"failure":"User is not part of any project"}],status=status.HTTP_400_BAD_REQUEST)

    def get_skills(self,request):
        pro = projects.objects.get(id=request.data['id'])
        skills=[]
        for skill in list(pro.skills.all()):
            skills.append({"name":skill.name})
        return Response(skills,status=status.HTTP_200_OK)
    def get_users(self,request):
        pro = projects.objects.get(id=request.data['id'])
        users=[]
        for user in list(pro.users.all()):
            users.append({"name":user.username})
        return Response(users,status=status.HTTP_200_OK)
    def get_all_skills(self,request):
        skills = []
        for skill in list(Skill_names.objects.all()):
            skills.append({"name":skill.name})
        return Response(skills,status=status.HTTP_200_OK)
    def get_all_users(self,request):
        users = []
        for user in list(User.objects.all()):
            users.append({"username":user.username})
        return Response(users,status=status.HTTP_200_OK)







    def post(self,request,number):
        if(number==0):
            return self.create(request)
        elif(number==1):
            return self.add_users(request)
        else:
            return self.add_skills(request)
            


            
    def delete(self,request,number):
        pro = projects.objects.get(id=number)
        pro.users.remove(request.user)
        return Response([{"success":"User is removed from this project"}])
    def get(self,request,number):
        if(number==0):
            return self.get_project(request)
        elif(number==1):
            return self.get_skills(request)
        elif(number==2):
            return self.get_users(request)
        elif(number==3):
            return self.get_all_skills(request)
        else:
            return self.get_all_users(request)
        
         

        

        
    def put(self,request):
        pro = projects.objects.get(id=request.data['id'])
    
        pro.info  = request.data['info']
        pro.starts  = request.data['starts']
        pro.ends = request.data['ends']
        pro.description = request.data['description']
        pro.status = request.data['status']
        pro.client_name = request.data['client_name']
        pro.client_location  = request.data['client_location']
        pro.location_of_project_execution = request.data['location_of_project_execution']
        pro.Industry_of_the_client = request.data['Industry_of_the_client']
        pro.Role = request.data['Role']
        pro.team_size  = request.data['team_size']
        pro.case_study_submitted  = request.data['case_study_submitted']
        
        pro.save()
        return Response([{"success":"project updated"}])


    














    









