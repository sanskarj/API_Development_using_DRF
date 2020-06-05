from rest_apis.api.authentication_view import api_register_user,api_logout_user,api_login_user

from django.urls import path
from  rest_framework.authtoken.views import obtain_auth_token
from rest_apis.api.userinfo_views import api_create_userinfo,api_update_userinfo,api_get_userinfo
from rest_apis.api.profileimageview import api_createprofile,api_updateprofile,api_getprofile
from rest_apis.api.communication_view import api_addcommunication,api_updatecommunication,api_getcommunication
from rest_apis.api.hobby_view import api_add_hobbies,api_get_hobbies,api_delete_hobbies
from rest_apis.api.project_view import api_create_project,api_delete_project,api_get_project,api_update_project,api_add_users_to_project,api_add_skills_to_project,api_get_skills_of_project,api_get_users_of_project,api_get_all_available_skills,api_get_all_registered_users
from rest_apis.api.achievements_view import api_create_achievement,api_get_achievement,api_update_achievement,api_delete_achievement
from rest_apis.api.skills_view import api_add_skills,api_delete_skills,api_get_skills,api_update_skills

from rest_apis.api.Imageupload_view import api_upload_image,api_get_image
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

    
    path('addhobbies',api_add_hobbies,name="hobby_add"),
    path('gethobbies',api_get_hobbies,name="hobby_get"),
    path('deletehobbies',api_delete_hobbies,name="hobby_delete"),

    path('addproject',api_create_project,name="project_create"),
    path('deleteproject',api_delete_project,name="project_delete"),
    path('updateproject',api_update_project,name="project_update"),
    path('getproject',api_get_project,name="project_get"),
    path('adduserstoproject',api_add_users_to_project,name="add_users_to_project"),
    path('addskillstoproject',api_add_skills_to_project,name="add_skills_to_project"),
    path('getskillsofproject',api_get_skills_of_project,name="get_skills_of_project"),
    path('getusersofproject',api_get_users_of_project,name="get_user_of_project"),
    path('getallusers',api_get_all_registered_users,name="get_all_users"),
    path('getallskills',api_get_all_available_skills,name="get_all_skills"),

    path('addachievement',api_create_achievement,name="achievement_create"),
    path('deleteachievement/<title>',api_delete_achievement,name="achievement_delete"),
    path('updateachievement/<title>',api_update_achievement,name="achievement_update"),
    path('getachievement',api_get_achievement,name="achievement_get"),


    path('addskills',api_add_skills,name="skill_create"),
    path('deleteskills',api_delete_skills,name="skill_delete"),
    path('updateskills',api_update_skills,name="skill_update"),
    path('getskills',api_get_skills,name="skill_get"),   
    path('uploadimage',api_upload_image,name="image_upload"),
    path('getimage',api_get_image,name="image_get")


]