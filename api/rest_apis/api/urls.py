from rest_apis.api.authentication_view import api_register_user,api_logout_user,api_login_user

from django.urls import path
from  rest_framework.authtoken.views import obtain_auth_token
from rest_apis.api.userinfo_views import api_create_userinfo,api_update_userinfo,api_get_userinfo
from rest_apis.api.profileimageview import api_createprofile,api_updateprofile,api_getprofile
from rest_apis.api.communication_view import api_addcommunication,api_updatecommunication,api_getcommunication
from rest_apis.api.hobby_view import api_addhobby,api_deletehobby,api_gethobby
from rest_apis.api.project_view import api_create_project,api_delete_project,api_get_project,api_update_project
from rest_apis.api.achievements_view import api_create_achievement,api_get_achievement,api_update_achievement,api_delete_achievement
from rest_apis.api.skills_view import api_addskill,api_deleteskill,api_updateskill,api_getskill

app_name  = 'rest_apis'
urlpatterns = [

    path('registeruser',api_register_user,name="user_register"),
    path('login',api_login_user,name="user_login"),
    path('logout',api_logout_user,name="user_logout"),

    path('adduserinfo',api_create_userinfo,name="user_create"),
    path('updateuserinfo',api_update_userinfo,name="user_update"),
    path('getuserinfo',api_get_userinfo,name="user_get"),

    path('addprofileimage',api_createprofile,name="profile_create"),
    path('updateprofileimage',api_updateprofile,name="profile_update"),
    path('getprofileimage',api_getprofile,name="profile_get"),

    path('addcommunication',api_addcommunication,name="communication_create"),
    path('updatecommunication/<medium>',api_updatecommunication,name="communication_update"),
    path('getcommunication',api_getcommunication,name="communication_get"),

    path('addhobby',api_addhobby,name="hobby_create"),
    path('deletehobby',api_deletehobby,name="hobby_delete"),
    path('gethobby',api_gethobby,name="hobby_get"),

    path('addproject',api_create_project,name="project_create"),
    path('deleteproject/<info>',api_delete_project,name="project_delete"),
    path('updateproject/<info>',api_update_project,name="project_update"),
    path('getproject',api_get_project,name="project_get"),

    path('addachievement',api_create_achievement,name="achievement_create"),
    path('deleteachievement/<title>',api_delete_achievement,name="achievement_delete"),
    path('updateachievement/<title>',api_update_achievement,name="achievement_update"),
    path('getachievement',api_get_achievement,name="achievement_get"),


    path('addskill',api_addskill,name="skill_create"),
    path('deleteskill',api_deleteskill,name="skill_delete"),
    path('updateskill/<name>/<proficiency>',api_updateskill,name="skill_update"),
    path('getskill',api_getskill,name="skill_get"),   
]