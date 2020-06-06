from rest_apis.api.authentication_view import api_register_user,api_logout_user,api_login_user

from django.urls import path
from  rest_framework.authtoken.views import obtain_auth_token
from rest_apis.api.userinfo_views import Userinfo

from rest_apis.api.communication_view import Communications
from rest_apis.api.hobby_view import Hobbies
from rest_apis.api.project_view import Projects
from rest_apis.api.achievements_view import Achievements
from rest_apis.api.skills_view import Skills




  
app_name  = 'rest_apis'
urlpatterns = [

    path('registeruser',api_register_user,name="user_register"),
    path('login',api_login_user,name="user_login"),
    path('logout',api_logout_user,name="user_logout"),

    
    path('userinfo',Userinfo.as_view(),name="userinfo_view"),

    path('communications',Communications.as_view(),name="communications_view"),
    path('communications/<medium>',Communications.as_view(),name="communications_view"),
    
    path('hobbies',Hobbies.as_view(),name="hobbies_view"),

    path('project',Projects.as_view(),name="projects_view"),
    path('project/<int:number>',Projects.as_view(),name="projects_view"),

    path('achievements',Achievements.as_view(),name="achieve_view"),
    path('achievements/<title>',Achievements.as_view(),name="achieve_view"),

    path('skills',Skills.as_view(),name="skills_api"),
    




]